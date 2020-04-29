"""Exemplo de pesquisa em seite"""
from selenium import webdriver


class Site:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://www.tribunadopampa.com.br/' #site de busca
        self.search_bar = 's'  # id da barra de busca
        self.btn_search = 'search-image'  # id do botao 

    def navigate(self):
        self.driver.get(self.url) #navega ate a url

    def search(self, word='Nome'):
        self.driver.find_element_by_id(
            self.search_bar).send_keys(word) #insere o texto
        self.driver.find_element_by_id( 
            self.btn_search).click() #clica no botao

    
ff = webdriver.Firefox()
g = Site(ff)
g.navigate()
g.search('Unipampa') # palavra que deseja pesquisar
ff.quit()