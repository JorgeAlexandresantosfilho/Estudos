import requests
import pandas as pd

def temporada_resultado(season, round):
    url = f'http://api.jolpi.ca/ergast/f1/{season}/{round}/results.json'
    response = requests.get(url)
    response.raise_for_status()
    dados = response.json()
    races = dados['MRData']['RaceTable']['Races']
    return races

rounds = [1, 2, 3, 4, 5]

todos_dados = []

for r in rounds:
  races = temporada_resultado(2025, r)
  for race in races:
    nome_gp = race['raceName']
    round_gp = race['round']
    data_gp = race['date'] 
    circuito = race['Circuit']['circuitName']  
    for resultado in race['Results']:
        todos_dados.append({
            'gp': nome_gp,
            'round': round_gp,
            'data': data_gp,
            'circuito': circuito,
            'posicao': resultado['position'],      
            'piloto': resultado['Driver']['familyName'],
            'equipe': resultado['Constructor']['name'],
            'tempo': resultado.get('Time', {}).get('time', None)
        })
df = pd.DataFrame(todos_dados)
print(df.head(20))
print(df)