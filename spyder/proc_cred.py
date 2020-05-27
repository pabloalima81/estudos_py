# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script tratamento de base de dados.
"""

import pandas as pd
base = pd.read_csv('credit_data.csv') #carrega a base
base.describe()
base.loc[base['age']<0] #localiza registros menores que zero

#apagar a coluna
base.drop('age',1,inplace=True)

#apaga somente os registros (linhas) com problema
base.drop(base[base.age<0].index, inplace=True)

#preencher os valores manualmente com a media

base['age'].mean() #retorna a média
base['age'][base.age > 0].mean() #retorna a médida dos registros >0
base.loc[base.age <0, 'age']=40.92 #localiza reg < 0 e altera para 40.92

pd.isnull(base['age']) #mostra valores nulos
base.loc[pd.isnull(base['age'])] #loc valores nulos

previsores = base.iloc[:,1:4].values #todas linhas das colunas 1 a 3
classe = base.iloc[:,4].values #todas linhas da ultima coluna

#escalonamento de valores
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)
