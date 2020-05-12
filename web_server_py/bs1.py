from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://localhost/index.html")
bsObj = BeautifulSoup(html.read(), "html.parser")

print(bsObj.h1) #mostra o primeiro h1
print(bsObj.title) #mostra o título
print(bsObj.html) #mostra todo html
print(bsObj.find_all("h1")) #imprime todos os h1 em lista
print(bsObj.find_all("a")) #imprime todos os links

#retorno dos hrefs usando for
for links in bsObj.find_all("a"):
	print(links)

#retorno somente dos links
for links in bsObj.find_all("a"):
	print(links.get("href"))