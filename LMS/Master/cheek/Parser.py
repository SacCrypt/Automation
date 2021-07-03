from html.parser import HTMLParser
from html.entities import name2codepoint
import mammoth
from bs4 import BeautifulSoup
from Nest import var

jsonlist = []
jsonlistenglish = []
jsonlisthindi = []
mydict = {}

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        self.starttag = tag

    def handle_data(self, data):
        if "?" in data:
            data = data.strip("\n")
            mydict["question"] = data
            diccopy = mydict.copy()
            jsonlist.append(diccopy)




parser = MyHTMLParser()

with open(var, "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    html = result.value 
    
soup  = BeautifulSoup(html, "lxml")

soupper = soup.prettify()
parser.feed(soupper)

for i in range(len(jsonlist)):
    if i%2 == 0:
        jsonlistenglish.append(jsonlist[i])
    else:
        jsonlisthindi.append(jsonlist[i])









        








      



