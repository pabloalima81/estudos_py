# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 20:46:31 2020

@author: pabloalima81

Rodando naive bayes na base de dados de credit data

"""

import pandas as pd
import numpy as np

base = pd.read_csv('credit_data.csv') #importa a base de dados
base.loc[base.age < 0, 'age'] = 40.92 # insere a média nos valores zero
               
previsores = base.iloc[:, 1:4].values #cria os previsores
classe = base.iloc[:, 4].values #cria as classes

#trata os valores não informados
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputer = imputer.fit(previsores[:, 1:4])
previsores[:, 1:4] = imputer.transform(previsores[:, 1:4])

#Faz o scaler, converter os atributos numericos na mesma escala
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

#divide a base de previsores e classes em treinamento e teste
from sklearn.model_selection import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.25, random_state=0)

from sklearn.naive_bayes import GaussianNB
classificador = GaussianNB()
classificador.fit(previsores_treinamento, classe_treinamento) #treinamento, gera a tabela de probabilidades

previsoes = classificador.predict(previsores_teste)#resultado da previsao


from sklearn.metrics import confusion_matrix, accuracy_score
precisao = accuracy_score(classe_teste, previsoes) #percentual de acerto do alg
matriz = confusion_matrix(classe_teste, previsoes) #monta a matrix de confusao
