import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print("Carregando o seu banco de dados atual...")
with open('banco_selecoes.json', 'r', encoding='utf-8') as f:
    banco_dados = json.load(f)

# Dicionário rápido para colocar o nome no arquivo final
mapeamento_selecoes = {
    "4748": "Brasil", "4819": "Argentina", "4481": "França", "4713": "Inglaterra", 
    "4698": "Espanha", "4711": "Alemanha", "4704": "Portugal", "4705": "Holanda", 
    "4725": "Uruguai", "4820": "Colômbia", "4724": "EUA", "4781": "México",
    "4752": "Canadá", "4770": "Japão", "4735": "Coreia do Sul", "4741": "Austrália", 
    "4739": "Senegal", "4778": "Marrocos", "4715": "Croácia", "4717": "Bélgica", 
    "4699": "Suíça", "4757": "Equador", "4834": "Arábia Saudita", "4792": "Catar",
    "4766": "Irã", "4729": "Tunísia", "4758": "Egito", "4691": "Argélia", 
    "4764": "Gana", "4768": "Costa do Marfim", "4736": "África do Sul", 
    "4753": "Cabo Verde", "4723": "Uzbequistão", "4771": "Jordânia", 
    "4784": "Nova Zelândia", "4789": "Paraguai", "5164": "Panamá", "7229": "Haiti", 
    "55827": "Curaçao", "4695": "Escócia", "4700": "Turquia", "4714": "República Tcheca", 
    "4688": "Suécia"
}

driver = webdriver.Chrome()
print("\nIniciando a cirurgia de atualização tática...")

for id_selecao, jogos in banco_dados.items():
    print(f"\nAtualizando intensidade de: {mapeamento_selecoes.get(id_selecao, id_selecao)}")
    
    for id_jogo, stats in jogos.items():
        # Se o jogo já tem a chave de bolas recuperadas, o robô pula para o próximo!
        if "bolas_recuperadas" in stats:
            continue

        try:
            url_stats = f"https://api.sofascore.com/api/v1/event/{id_jogo}/statistics"
            driver.get(url_stats)
            time.sleep(1.2)
            
            conteudo_stats = driver.find_element(By.TAG_NAME, "pre").text
            json_stats = json.loads(conteudo_stats)
            
            if 'statistics' not in json_stats or len(json_stats['statistics']) == 0:
                continue
                
            estatisticas_gerais = json_stats['statistics'][0]['groups']
            
            coluna_alvo = "home"
            
            # 1. HACK DE INTELIGÊNCIA: Descobre quem é o time cruzando os chutes
            for grupo in estatisticas_gerais:
                for item in grupo.get('statisticsItems', []):
                    if item['name'] == "Total shots":
                        chutes_home = int(item.get("home", 0))
                        # Se os chutes baterem com o banco, achamos a coluna certa
                        if chutes_home == stats["chutes_feitos"]:
                            coluna_alvo = "home"
                        else:
                            coluna_alvo = "away"
                            
            # 2. COLETA AS MÉTRICAS DE INTENSIDADE (BLINDADO)
            recuperacoes = 0
            desarmes = 0
            
            for grupo in estatisticas_gerais:
                for item in grupo.get('statisticsItems', []):
                    if item['name'] == "Recoveries":
                        # Pega o valor, converte pra texto, corta no espaço e arranca a porcentagem
                        valor_rec = str(item.get(coluna_alvo, "0")).split()[0].replace('%', '')
                        recuperacoes = int(valor_rec)
                        
                    elif item['name'] == "Tackles won":
                        valor_des = str(item.get(coluna_alvo, "0")).split()[0].replace('%', '')
                        desarmes = int(valor_des)
                        
            # Grava no JSON
            banco_dados[id_selecao][id_jogo]["bolas_recuperadas"] = recuperacoes
            banco_dados[id_selecao][id_jogo]["desarmes_certos"] = desarmes
            
            print(f"-> Jogo {id_jogo} | Recuperadas: {recuperacoes} | Desarmes: {desarmes}")
            
        except Exception as e:
            print(f"-> Aviso: Falha no jogo {id_jogo} - {e}")

    # Salva o arquivo local a cada país concluído
    with open('banco_selecoes.json', 'w', encoding='utf-8') as f:
        json.dump(banco_dados, f, ensure_ascii=False, indent=4)

driver.quit()

# =========================================================================
# RECONSTRUÇÃO DO ARQUIVO FINAL DO SITE
# =========================================================================
print("\nReconstruindo o JSON consolidado do Front-End...")
output_site = {}

for id_selecao, jogos in banco_dados.items():
    nome_selecao = mapeamento_selecoes.get(id_selecao, "Desconhecido")
    total_jogos = len(jogos)
    
    if total_jogos == 0:
        continue
        
    vitorias = sum(1 for j in jogos.values() if j["resultado"] == "V")
    soma_gols_pro = sum(j["gols_pro"] for j in jogos.values())
    soma_gols_contra = sum(j["gols_contra"] for j in jogos.values())
    soma_posse = sum(j["posse"] for j in jogos.values())
    soma_chutes_feitos = sum(j["chutes_feitos"] for j in jogos.values())
    soma_chutes_sofridos = sum(j["chutes_sofridos"] for j in jogos.values())
    soma_escanteios = sum(j.get("escanteios", 0) for j in jogos.values())
    soma_recuperadas = sum(j.get("bolas_recuperadas", 0) for j in jogos.values())
    
    win_rate = (vitorias / total_jogos) * 100
    
    output_site[nome_selecao] = {
        "jogos_analisados": total_jogos,
        "aproveitamento": f"{win_rate:.1f}%",
        "media_gols_marcados": round(soma_gols_pro / total_jogos, 2),
        "media_gols_sofridos": round(soma_gols_contra / total_jogos, 2),
        "posse_media": f"{(soma_posse / total_jogos):.1f}%",
        "chutes_realizados_por_jogo": round(soma_chutes_feitos / total_jogos, 1),
        "chutes_concedidos_por_jogo": round(soma_chutes_sofridos / total_jogos, 1),
        "escanteios_por_jogo": round(soma_escanteios / total_jogos, 1),
        "bolas_recuperadas_por_jogo": round(soma_recuperadas / total_jogos, 1)
    }

with open('dados_selecoes.json', 'w', encoding='utf-8') as f:
    json.dump(output_site, f, ensure_ascii=False, indent=4)

print("\n--- Patch Aplicado com Sucesso! ---")
print("As métricas de bolas recuperadas foram injetadas no seu dados_selecoes.json.")