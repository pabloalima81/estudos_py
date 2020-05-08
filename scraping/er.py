#busca usando expressoes regulares
import re

padrao = "texto" #texto a ser procurado
texto = "Este e um exemplo de texto para busca da palavra texto"
resultado = re.findall(padrao,texto)

if resultado:
	print(resultado) #localizacao do obj
	#print(resultado.group()) #imprime o objeto
else:
	print("Nao Encontrado")