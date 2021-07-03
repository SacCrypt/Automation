import json
from bs4 import BeautifulSoup
import mammoth
import re
import pdb

with open(r"C:\Users\10PRO\Downloads\Uploading_Assignment_Ras_chhand_alankar_Sarita_19Jan2021_30Qs.docx", "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    html = result.value

with open("Deepika.html", "w+", encoding = "utf-8") as htmlmaker:
    htmlmaker.write(html)

html_file = r"Deepika.html"

with open(html_file, "r+", encoding = "utf-8") as f:
    soup = BeautifulSoup(f, "lxml")

tables = soup.findAll("table")
prettify = soup.prettify()

var = 0

def count_iterable(i):
    return sum(1 for e in i)


sol_pattern = re.compile(r'Solution:')
sol_matches = sol_pattern.finditer(prettify)

q_pattern = re.compile(r'Q\d{1,2}\.')
q_matches = q_pattern.finditer(prettify)

#print(count_iterable(sol_matches))



#print((soup.getText))

paras = soup.findAll("p")
strong = soup.findAll("strong")

messedqs = []
questions = []
answers = []
solutions = []
spans = []


for sol_match, q_match in zip(sol_matches, q_matches):
    #print(sol_match.span()[1], q_match.span()[1])
    spans.append(sol_match.span()[1])
    spans.append(q_match.span()[1])

spans.sort()
spans.pop(0)

for i in range(0, len(spans) - 1, 2):
    #print(spans[i])
    #pdb.set_trace()
    solutions.append(prettify[spans[i]:spans[i+1]].lstrip().lstrip(":").rstrip().rstrip("Q1234567890.").lstrip("</p>").rstrip())

solutions.append(prettify[spans[-1] : len(prettify)])

solutions = [x.replace("\n", "").strip() for x in solutions]
solutions = [x.replace("<table>", '<table border="1" style="width:350px;"') for x in solutions]    


solutions = [x.replace("</table>", "</table></br>", 1).rstrip("<p>") for x in solutions]

for x in paras:
    if x.strong == None:
        '''for i in range(1,6):
            i = str(i)
            if i + ')' in x.text:
                choices.append(x.contents[0].lstrip(i + ')'))'''

Ordered = soup.findAll("ol")

choices = [y.text for x in Ordered for y in x.contents]


for i in paras:
    #pdb.set_trace()
    if "Ans." in i.text:
        answers.append(i.text.lstrip(" Ans."))
    if len(i.contents) == 2:
        try:
            if "Q" in i.contents[0].extract().text:
                messedqs.append(i.contents[0].lstrip("-"))
        except Exception as e:
            print(e)
            continue


questions = messedqs


result = []

def append(questions, choices, answers, solutions, var):
    #pdb.set_trace()
    result.append({"questions" : questions[i],
                   "choices" : choices[var : var + 4],
                   "answers" : answers[i],
                   "solutions" : solutions[i],
                   })

for i in range(0, 30):
    append(questions, choices, answers, solutions, var)
    var += 4

jsonD = json.dumps(result, indent = 2)

with open("Deepika.json", "w+", encoding = "utf-8") as f:
    write = json.loads(jsonD)
    json.dump(write, f, indent = 4, ensure_ascii = False)


