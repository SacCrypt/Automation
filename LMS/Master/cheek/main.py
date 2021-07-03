import json
from time import sleep

from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
    
from config import (ADD_BUTTON, ADD_OPTION, CHECKBOXES, CLOSE_BUTTON,
                DATA_FILE, JAVASCRIPT_TO_EXECUTE, OPTIONS, QUESTION, SOLUTION)
from testbooklogin import testbook_login
from utils import change_xpath, sanitize_html


with open(DATA_FILE, encoding = "utf-8") as f:
    data_string = json.load(f)

driver = testbook_login()  # type: webdriver

driver.implicitly_wait(10)

WebDriverWait(driver, 15).until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[3]/div[1]/div/div[3]/button')
))
try:
    driver.get(WEBSITE_URL)
except:
    pass
sleep(5)  # for that weird loading animation to dissappear

# Find and click `Add new Question` button
WebDriverWait(browser, 15).until(EC.presence_of_element_located((
    By.ID, 'addQuestionCHK')
)).click()

try:
    # Start data loop here
    for data in data_string:
        print(f"{Fore.RED}Processing:{Fore.YELLOW} {data['question']}{Style.RESET_ALL}")
        mcq = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[3]/div/div[8]/div[5]/button")
        ))
        mcq.click()

        modal = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
            (By.XPATH, "//p[contains(text(),'Add Multiple Choice Question')]")
        ))

        xpath_to_mcq = driver.execute_script(JAVASCRIPT_TO_EXECUTE, modal)

        # Fill the question correctly
        question = WebDriverWait(modal, 15).until(EC.presence_of_element_located(
            (By.XPATH, change_xpath(xpath_to_mcq, QUESTION))
        ))
        driver.execute_script(sanitize_html(data['question']), question)

        option_values = data['choices']
        
        for _ in range(len(option_values) - 4):
            # Add an option if there are more than 4 options
            WebDriverWait(modal, 15).until(EC.presence_of_element_located(
                (By.XPATH, change_xpath(xpath_to_mcq, ADD_BUTTON))
            )).click()
            WebDriverWait(modal, 15).until(EC.presence_of_element_located(
                (By.XPATH, change_xpath(xpath_to_mcq, ADD_OPTION))
            )).click()

        for option_val, option in zip(data['choices'].values(), OPTIONS):
            # Fill in the options correctly
            option_element = modal.find_element_by_xpath(
                change_xpath(xpath_to_mcq, option))
            driver.execute_script(sanitize_html(option_val), option_element)

        correct_option = int(data['answer'])

        # Check the correct box determine which box is to be ticked
        for index, option in enumerate(CHECKBOXES, 1):
            if index == correct_option:
                # Click the checkbox when the option is matched
                modal.find_element_by_xpath(change_xpath(xpath_to_mcq, option)).click()

        solution = data['solution']

        # Fill in the solution in the correct element
        solution_element = modal.find_element_by_xpath(
            change_xpath(xpath_to_mcq, SOLUTION))
        driver.execute_script(sanitize_html(solution), solution_element)

        sleep(1)  # unneeded but added it just in case the buttons aren't loaded yet

        # Click the close button, later to be replaced by the save button. Comment
        # these lines when you need to save.
        close_button = WebDriverWait(modal, 15).until(EC.presence_of_element_located(
            (By.XPATH, change_xpath(xpath_to_mcq, CLOSE_BUTTON))
        ))
        close_button.click()

        # Uncomment these lines when you need to save
        # close_button = WebDriverWait(modal, 15).until(EC.presence_of_element_located(
        #     (By.XPATH, change_xpath(xpath_to_mcq, SAVE_BUTTON))
        # ))
        # close_button.click()

finally:
    sleep(3)
    driver.quit()
