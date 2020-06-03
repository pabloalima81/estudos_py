# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: pabloalima81

Rodando naive bayes na base de dados de risco crédito
"""
import pandas as pd

base = pd.read_csv('risco_credito.csv') #carrega a base
previsores = base.iloc[:,0:4].values #var previsores
classe = base.iloc[:,4].values #var classe

#transforma de string para int
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
previsores[:,0] = labelencoder.fit_transform(previsores[:,0])
previsores[:,1] = labelencoder.fit_transform(previsores[:,1])
previsores[:,2] = labelencoder.fit_transform(previsores[:,2])
previsores[:,3] = labelencoder.fit_transform(previsores[:,3])

from sklearn.naive_bayes import GaussianNB

classificador = GaussianNB()
classificador.fit(previsores, classe) #treinamento, gera a tabela de probabilidades

# história boa, dívida alta, garantias nenhuma, renda > 35
# história ruim, dívida alta, garantias adequada, renda < 15
resultado = classificador.predict([[0,0,1,2], [3, 0, 0, 0]]) #insere 2 registros
#predict faz a estimativa de probabilidade

print(classificador.classes_) #mostra as classes
print(classificador.class_count_) #numero de cada classes
print(classificador.class_prior_) #probabilidades apriori
