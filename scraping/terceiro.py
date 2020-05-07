import requests
import bs4

response = requests.get("https://www.google.com/")
soup = bs4.BeautifulSoup(response.text, "html.parser")

print(soup.find_all('title')) #retorna o título da página
