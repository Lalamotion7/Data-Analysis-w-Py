import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Lista corrigida e padronizada com o banco do Sofascore
selecoes_copa = [
    "Iraq", "Norway", "Austria", "DR Congo", "Bosnia & Herzegovina"
]

dicionario_ids = {}

print("Iniciando o tanque de guerra (Selenium) para driblar o Cloudflare...\n")
driver = webdriver.Chrome()

for pais in selecoes_copa:
    # Endpoint da barra de pesquisa do Sofascore
    url = f"https://api.sofascore.com/api/v1/search/all?q={pais}"
    
    try:
        driver.get(url)
        # Pausa de 2 segundos. É o tempo de carregar a página e não tomar ban por excesso de velocidade.
        time.sleep(2) 
        
        conteudo = driver.find_element(By.TAG_NAME, "pre").text
        dados = json.loads(conteudo)
        encontrou = False
        
        # Varre os resultados da pesquisa
        for resultado in dados.get('results', []):
            if resultado.get('type') == 'team':
                entidade = resultado.get('entity', {})
                esporte = entidade.get('sport', {}).get('slug')
                nacional = entidade.get('national')
                
                # Exige que seja futebol e que seja seleção oficial (evita pegar time com nome de país)
                if esporte == 'football' and nacional == True:
                    id_selecao = str(entidade['id'])
                    dicionario_ids[id_selecao] = pais
                    print(f"[OK] {pais} -> ID: {id_selecao}")
                    encontrou = True
                    break 
                    
        if not encontrou:
            print(f"[AVISO] Não encontrou a seleção de: {pais}")
            
    except Exception as e:
        print(f"Erro ao buscar {pais}: O Chrome não encontrou o JSON na tela.")

driver.quit()

print("\n=== COPIE E COLE O DICIONÁRIO ABAIXO NO SCRIPT DO BOLÃO ===")
print("mapeamento_selecoes = " + json.dumps(dicionario_ids, indent=4))