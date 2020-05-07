import requests
pagina = requests.get("https://google.com/")
print(pagina.text) #print(pagina.content)

#usando request
