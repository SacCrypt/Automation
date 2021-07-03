import json
import re

from docx2python import docx2python
from config import DATA_FILE, DOCX_FILE


from lxml import html
from bs4 import BeautifulSoup
import json
import mammoth

url = r"C:\Users\10PRO\Desktop\Python Programs\output.html"

f = open(url, encoding="utf8")     
soup = BeautifulSoup(f, "lxml")
f.close()


with open(url, "r", encoding="utf8") as f:
    page = f.read()

tree = html.fromstring(page)
hindiq = []
_list = []

def splitEnglishQuestionAndAnswer(questWithOpts, options, answers, hindi, solution):
    choices = [val.contents for val in options.findAll("li")]
    #print("Choices : ", choices)
    questWithOpts.find("ol").clear()
    #print("questWithOpts:", questWithOpts)
    result.append({
        "question": questWithOpts.text,
        "choices": formatChoices(choices),
        "answer": answers[i],
        "solution": solution[i]
    })
    result[i]["question"].append(hindi[i])

def formatChoices(choices):
    formattedChoices = {}
    for index, choice in enumerate(choices):
        formattedChoices[index+1] = chr(ord('`')+1+index) + ")" + choice[0]
        #print("Formattedchoices : ", formattedChoices)
    return formattedChoices

bulleted = soup.findAll("ul")
strong = soup.findAll("strong")
root = soup.findAll("ol")
xd = soup.findAll("p")

for i in strong:
        i = i.text.strip()
        if i.isdigit() is True:
            _list.append(i)

for hind in xd:
    if hind.strong is None:
        hindiq.append(hind.text)
        
result = []
#solution ko correct option lagana hai
for i in range(len(root)):
    try:
        splitEnglishQuestionAndAnswer(root[i], root[i+1], _list, hindiq, bulleted)
    except Exception as e:
        pass       

soupper = soup.prettify()

for i in range(len(result)):
    result[i]["solution"] = str(result[i]["solution"])
     
jsonD = json.dumps(result, indent = 2)

with open("DATA_FILE", "w+", encoding = "utf-8") as f:
    write = json.loads(jsonD)
    json.dump(write, f, indent = 4, ensure_ascii = False)
'''def parse_data():  # sourcery skip: hoist-statement-from-loop
    docx_data = docx2python(DOCX_FILE, html=True)
    with open(TEXT_FILE, 'w', encoding = "utf-8") as f:
        f.write(docx_data.text)

    with open(TEXT_FILE, 'r', encoding = "utf-8") as text_file:
        data_complete = text_file.read()

    data_complete = data_complete.splitlines()
    data_complete = [data for data in data_complete if data]
    data_complete = iter(data_complete)

    json_data = []
    for data in data_complete:
        search = re.search(r'^\d+\).*', data)
        to_append = {}
        if search is not None:
            output = data[search.start():search.end()]
            print(output)
            number = re.search(r'^\d+', output)
            to_add = {'question': output, 'id': output[number.start():number.end()]}
            choices = {}
            for num in range(5):
                choices.update({num + 1: next(data_complete)})
            answer = next(data_complete)
            answer = re.search(r'\d+', answer).group()
            to_add.update({'choices': choices, 'answer': int(answer)})
            to_append.update(to_add)

            new_data_complete = data_complete
            actual_solution = ''
            while True:
                solution = re.search(r'--\t', next(new_data_complete))
                if solution:
                    actual_solution += solution.string
                else:
                    to_append.update({'solution': actual_solution})
                    break
        if to_append:
            json_data.append(to_append)

    json_data = json.dumps(json_data)
    json_data = json_data.replace(r'\t', '')
    json_data = json_data.replace(r'\u2019', "'")
    json_data = json_data.replace(r'\u20b9', "₹")
    json_data = json.loads(json_data)

    with open(DATA_FILE, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)'''

def change_xpath(xpath, xpath_to_change):
    import re
    match = re.search(r'\d+', xpath)
    return xpath_to_change.replace(r'{target}', f"{match.group()}")


def sanitize_html(data):
    data = data.replace(r"'", r"\'")
    return f"arguments[0].innerHTML = '{data}'"
