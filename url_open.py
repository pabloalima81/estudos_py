from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://www.google.com")
res = BeautifulSoup(html.read(),"html5lib");
print(res.title)