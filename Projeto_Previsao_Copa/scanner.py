import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print("Carregando o primeiro jogo do Brasil...")
with open('banco_selecoes.json', 'r', encoding='utf-8') as f:
    banco = json.load(f)

# Pega o ID do Brasil (4748) e seleciona a primeira partida da lista
id_primeiro_jogo = list(banco["4748"].keys())[0]

print(f"Investigando as métricas ocultas do jogo: {id_primeiro_jogo}\n")

driver = webdriver.Chrome()
url_stats = f"https://api.sofascore.com/api/v1/event/{id_primeiro_jogo}/statistics"

driver.get(url_stats)
time.sleep(2)

conteudo = driver.find_element(By.TAG_NAME, "pre").text
json_stats = json.loads(conteudo)
driver.quit()

print("=== MÉTRICAS ENCONTRADAS NESTA PARTIDA ===")
estatisticas_gerais = json_stats['statistics'][0]['groups']

for grupo in estatisticas_gerais:
    print(f"\n[{grupo.get('groupName', 'Geral')}]")
    for item in grupo.get('statisticsItems', []):
        print(f"- {item['name']}")