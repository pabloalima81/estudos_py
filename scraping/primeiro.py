
from urllib.request import urlopen

html = urlopen("http://www.google.com") 
print(html.read()) #printa o read do site

#primeiro scrap usando urlopen