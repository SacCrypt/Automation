import mammoth
from bs4 import BeautifulSoup
from itertools import chain

array = []
_list = []
reallist = []
Dict = {"questions" : "",
        "questionno" : "",
        "choices" : "",
        "answer" : "",
        "solution" : ""}

var = r"C:\Users\10PRO\Downloads\Today's current affairs 2nd Jan 2021.docx"

result = mammoth.convert_to_html(var)
html = result.value
soup = BeautifulSoup(html, 'lxml')    
ol = soup.findAll("ol")
choices = []  


for x in ol:
    if len(x.li) == 1:
        choices.append(x.contents)

output = []
another = []
another1 = []

test = []
test1 = []


def reemovNestings(l): 
    for i in l: 
        if type(i) == list: 
            reemovNestings(i) 
        else: 
            output.append(i.contents) 
reemovNestings(choices)

def reemovNestings1(l): 
    for i in l: 
        if type(i) == list: 
            reemovNestings1(i) 
        else: 
            another.append(i)
            
reemovNestings1(output)



test = [another[i:i+5] for i in range(len(another) - 5) if i%5==0]



choicesenglish = list(chain.from_iterable(another[i:i+5] for i in range(0, len(another), 10)))
choiceshindi = list(chain.from_iterable(another[i:i+5] for i in range(5, len(another), 10)))


