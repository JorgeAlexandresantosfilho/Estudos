import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

#aqui vou passar dados (ficticios)

dados = {
    "idade": [10,12,20, 25,30,35,40,50,60],
    "horas_jogando": [3,5,4,2,1,1,0.5,0.2,0],
    "gosta": [1, 1, 1, 1, 0, 0, 0, 0, 0]  # 1 ta representando se gosta e 0 se nao
}

#criando o df

df = pd.DataFrame(dados)


#dividir variaveis

x = df[["idade", "horas_jogando"]]
y = df["gosta"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)


#modelo
modelo = LogisticRegression()

#treinando o modelo
modelo.fit(x_train, y_train)

#teste do modelo
print("acuracia:", modelo.score(x_test, y_test))


#previsao
idade = 20
horas = 3
previsao = modelo.predict([[idade, horas]])
print(f"Com {idade} anos e {horas}h de jogo/dia {'Gosta' if previsao[0] == 1 else 'Não gosta'}")