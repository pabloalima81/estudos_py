#busca usando expressoes regulares
import re

padrao = "texto" #texto a ser procurado
texto = "Este e um exemplo de texto para busca da palavra texto"
resultado = re.search(padrao,texto)

print(resultado) #localizacao do obj
print(resultado.group()) #imprime o obj
