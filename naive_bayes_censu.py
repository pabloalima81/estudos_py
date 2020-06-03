# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 21:16:11 2020

@author: escobar

Rodando naive bayes na base de dados do censu

"""

import pandas as pd

base = pd.read_csv('census.csv')

previsores = base.iloc[:, 0:14].values
classe = base.iloc[:, 14].values
                
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
labelencoder_previsores = LabelEncoder()

onehotencorder = ColumnTransformer(transformers=[("OneHot", OneHotEncoder(), [1,3,5,6,7,8,9,13])],remainder='passthrough')
previsores = onehotencorder.fit_transform(previsores).toarray()

labelencorder_classe = LabelEncoder()
classe = labelencorder_classe.fit_transform(classe)

#Faz o scaler, converter os atributos numericos na mesma escala
#percentual de acerto sem o scaler é melhor
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