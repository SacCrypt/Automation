from pyotp import *  # NOQA
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def testbook_login():

    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("https://lms.testbook.com/manage/live-courses")
    browser.find_element_by_id("email").send_keys("sachin.fulsunge@testbook.com")
    try:
        WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.ID, "passwd")))
        browser.find_element_by_id("passwd").send_keys("8329272168")
    except Exception as Except:
        print(Except)
    totp = TOTP(  # NOQA
        "KZLCCQBDIFAUAJBGKBHCKJRKKJBHGYLDNBUW4LTGOVWHG5LOM5SUA5DFON2GE33PNMXGG33NGQZDINBWGM2TONQ"  # NOQA
    )
    token = totp.now()
    browser.find_element_by_id("otp").send_keys(token)
    browser.find_element_by_xpath(
        "/html/body/div/div/div/div/div[2]/div/form/div[4]/button"
    ).click()
    return browser


