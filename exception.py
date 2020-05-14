from urllib.request import urlopen
from urllib.error import HTTPError, HTMLError
from bs4 import BeautifulSoup

def getTitulo (url):
	
	#trata o erro do urlopen
	try:
		html = urlopen(url)
	except HTTPError as erro:
		print("Ocorreu um erro HTTP:{erro}")
		return None

	except URLError as erro:
		print("Ocorreu um erro URL:{erro}")
		return None

	except:
		print("Ocorreu um erro na pagina")
		return None

	#Trata o erro do atributo de bsObj obtido pelo bs4
	try:
		bsObj = BeautifulSoup(html.read(), "html.parser")
		titulo = bsObj.body.h1	
	except AttributeError as erro:
		print("Ocorreu um erro de atributo ao acessar a tag h1: {erro}")
		return None
	except:
		print("Ocorreu um erro ao acessar o conteudo da pagina")
		return None
	return titulo

titulo = getTitulo(input("Informe a URL do site: "))

if titulo is not None:
	print("A h1 da pagina informada e {titulo}")
else:
	print("Nao foi encontrado um H1 na url informada")


