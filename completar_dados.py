import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

"""BaseDados = pd.read_csv('canais.csv', delimiter=';', encoding='cp1252')


#foi preciso separar as colunas numericas
colunas_numericas = BaseDados.select_dtypes(include=[np.number]).columns
#nao numericas (strings)
colunas_categoricas = BaseDados.select_dtypes(exclude=[np.number]).columns


imputer = SimpleImputer(strategy='mean')
BaseDados[colunas_numericas] = imputer.fit_transform(BaseDados[colunas_numericas])

print(BaseDados)"""


baseDeDados = pd.read_csv('canais.csv', delimiter=';',  encoding='cp1252')
X = baseDeDados.iloc[:,:].values

imputer = SimpleImputer(missing_values=np.nan, strategy='median')
imputer = imputer.fit(X[:,1:3])
X = imputer.transform(X[:,1:3]).astype(str)
X = np.insert(X, 0, baseDeDados.iloc[:,0].values, axis=1)

print(X)