import json
import time
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

# === DICIONÁRIO COMPLETO ===
mapeamento_selecoes = {
    "4748": "Brasil", "4819": "Argentina", "4481": "França",
    "4713": "Inglaterra", "4698": "Espanha", "4711": "Alemanha",
    "4704": "Portugal", "4705": "Holanda", "4725": "Uruguai",
    "4820": "Colômbia", "4724": "EUA", "4781": "México",
    "4752": "Canadá", "4770": "Japão", "4735": "Coreia do Sul",
    "4741": "Austrália", "4739": "Senegal", "4778": "Marrocos",
    "4715": "Croácia", "4717": "Bélgica", "4699": "Suíça",
    "4757": "Equador", "4834": "Arábia Saudita", "4792": "Catar",
    "4766": "Irã", "4729": "Tunísia", "4758": "Egito",
    "4691": "Argélia", "4764": "Gana", "4768": "Costa do Marfim",
    "4736": "África do Sul", "4753": "Cabo Verde", "4723": "Uzbequistão",
    "4771": "Jordânia", "4784": "Nova Zelândia", "4789": "Paraguai",
    "5164": "Panamá", "7229": "Haiti", "55827": "Curaçao",
    "4695": "Escócia", "4700": "Turquia", "4714": "República Tcheca",
    "4688": "Suécia", "4767": "Iraque",
    "4475": "Noruega", "4718": "Áustria",
    "4823": "RD Congo", "4479": "Bósnia e Herzegovina"
}

arquivo_banco = 'banco_selecoes.json'
driver = webdriver.Chrome()

if os.path.exists(arquivo_banco):
    with open(arquivo_banco, 'r', encoding='utf-8') as f:
        banco_dados = json.load(f)
else:
    banco_dados = {}

print("Iniciando o mapeamento do ciclo de 2 anos das seleções (Com extração de xG)...")

for id_selecao, nome_selecao in mapeamento_selecoes.items():
    print(f"\n=== Analisando Histórico de: {nome_selecao} ===")
    
    if id_selecao not in banco_dados:
        banco_dados[id_selecao] = {}

    # PASSO 1: Coletar os IDs de jogos recentes
    ids_jogos_selecao = []
    pagina = 0
    continuar_calendario = True
    
    while continuar_calendario:
        url_calendario = f"https://api.sofascore.com/api/v1/team/{id_selecao}/events/last/{pagina}"
        try:
            driver.get(url_calendario)
            time.sleep(4) 
            
            conteudo = driver.find_element(By.TAG_NAME, "pre").text
            dados_cal = json.loads(conteudo)
            eventos = dados_cal.get('events', [])
            
            if not eventos:
                break
                
            for partida in eventos:
                ano_partida = datetime.fromtimestamp(partida['startTimestamp']).year
                
                if ano_partida < 2024:
                    continuar_calendario = False
                    continue
                    
                if partida['status']['type'] == 'finished':
                    ids_jogos_selecao.append(partida)
                    
            pagina += 1
        except Exception as e:
            print(f"Erro ao ler calendário na página {pagina}: {e}")
            break

    print(f"Encontradas {len(ids_jogos_selecao)} partidas válidas.")

    # PASSO 2: Extrair métricas de cada jogo
    for idx, partida in enumerate(ids_jogos_selecao, 1):
        id_jogo = str(partida['id'])
        
        # ATUALIZAÇÃO INTELIGENTE: Agora o código exige a chave "xg_favor" para pular o jogo. 
        # Isso força o script a reabrir os jogos antigos e raspar a métrica nova!
        if id_jogo in banco_dados[id_selecao] and "xg_favor" in banco_dados[id_selecao][id_jogo]:
            continue
            
        try:
            time_mandante_id = str(partida['homeTeam']['id'])
            coluna_alvo = "home" if time_mandante_id == id_selecao else "away"
            coluna_oposta = "away" if coluna_alvo == "home" else "home"
            
            gols_pro = int(partida['homeScore']['current']) if coluna_alvo == "home" else int(partida['awayScore']['current'])
            gols_contra = int(partida['awayScore']['current']) if coluna_alvo == "home" else int(partida['homeScore']['current'])
            
            codigo_vencedor = partida.get('winnerCode', 3)
            if codigo_vencedor == 3:
                resultado = "E"
            elif (codigo_vencedor == 1 and coluna_alvo == "home") or (codigo_vencedor == 2 and coluna_alvo == "away"):
                resultado = "V"
            else:
                resultado = "D"

            url_stats = f"https://api.sofascore.com/api/v1/event/{id_jogo}/statistics"
            driver.get(url_stats)
            time.sleep(1.5)
            
            conteudo_stats = driver.find_element(By.TAG_NAME, "pre").text
            json_stats = json.loads(conteudo_stats)
            
            if 'statistics' not in json_stats or len(json_stats['statistics']) == 0:
                continue
                
            estatisticas_gerais = json_stats['statistics'][0]['groups']
            
            posse_jogo = 50
            finalizacoes_feitas = 0
            finalizacoes_sofridas = 0
            escanteios_favor = 0
            recuperacoes = 0
            xg_favor = 0.0
            xg_contra = 0.0
            
            for grupo in estatisticas_gerais:
                for item in grupo.get('statisticsItems', []):
                    nome_metrica = item['name']
                    
                    if nome_metrica == "Ball possession":
                        posse_jogo = int(str(item.get(coluna_alvo, "50")).replace('%', ''))
                    elif nome_metrica == "Total shots":
                        finalizacoes_feitas = int(item.get(coluna_alvo, 0))
                        finalizacoes_sofridas = int(item.get(coluna_oposta, 0))
                    elif nome_metrica == "Corner kicks":
                        escanteios_favor = int(item.get(coluna_alvo, 0))
                    elif nome_metrica == "Recoveries":
                        valor_rec = str(item.get(coluna_alvo, "0")).split()[0].replace('%', '')
                        recuperacoes = int(valor_rec)
                    # A NOSSA NOVA MÉTRICA DE OURO AQUI:
                    elif nome_metrica == "Expected goals":
                        xg_favor = float(item.get(coluna_alvo, 0) or 0)
                        xg_contra = float(item.get(coluna_oposta, 0) or 0)

            if id_jogo not in banco_dados[id_selecao]:
                banco_dados[id_selecao][id_jogo] = {}
                
            banco_dados[id_selecao][id_jogo].update({
                "resultado": resultado,
                "gols_pro": gols_pro,
                "gols_contra": gols_contra,
                "posse": posse_jogo,
                "chutes_feitos": finalizacoes_feitas,
                "chutes_sofridos": finalizacoes_sofridas,
                "escanteios": escanteios_favor,
                "bolas_recuperadas": recuperacoes,
                "xg_favor": xg_favor,
                "xg_contra": xg_contra
            })
            print(f"-> [{idx}/{len(ids_jogos_selecao)}] Jogo {id_jogo} processado com xG!")
            
        except Exception as e:
            print(f"-> [{idx}/{len(ids_jogos_selecao)}] Aviso: Erro no jogo {id_jogo} - {e}")

    with open(arquivo_banco, 'w', encoding='utf-8') as f:
        json.dump(banco_dados, f, ensure_ascii=False, indent=4)

driver.quit()

# =========================================================================
# PASSO 3: Consolidador Final (Com Média Inteligente de xG)
# =========================================================================
print("\nReconstruindo o JSON final consolidado...")
output_site = {}

for id_selecao, nome_selecao in mapeamento_selecoes.items():
    jogos = banco_dados.get(id_selecao, {})
    total_jogos = len(jogos)
    
    if total_jogos == 0:
        continue
        
    vitorias = sum(1 for j in jogos.values() if j.get("resultado") == "V")
    soma_gols_pro = sum(j.get("gols_pro", 0) for j in jogos.values())
    soma_gols_contra = sum(j.get("gols_contra", 0) for j in jogos.values())
    soma_posse = sum(j.get("posse", 50) for j in jogos.values())
    soma_chutes_feitos = sum(j.get("chutes_feitos", 0) for j in jogos.values())
    soma_chutes_sofridos = sum(j.get("chutes_sofridos", 0) for j in jogos.values())
    soma_escanteios = sum(j.get("escanteios", 0) for j in jogos.values())
    soma_recuperadas = sum(j.get("bolas_recuperadas", 0) for j in jogos.values())
    
    # Lógica de Média Segura para xG (conta só os jogos que registraram o dado)
    jogos_com_xg = sum(1 for j in jogos.values() if j.get("xg_favor", 0) > 0)
    soma_xg_favor = sum(j.get("xg_favor", 0) for j in jogos.values())
    soma_xg_contra = sum(j.get("xg_contra", 0) for j in jogos.values())
    
    media_xg_favor = round(soma_xg_favor / jogos_com_xg, 2) if jogos_com_xg > 0 else round(soma_gols_pro / total_jogos, 2)
    media_xg_contra = round(soma_xg_contra / jogos_com_xg, 2) if jogos_com_xg > 0 else round(soma_gols_contra / total_jogos, 2)
    
    win_rate = (vitorias / total_jogos) * 100 if total_jogos > 0 else 0
    
    output_site[nome_selecao] = {
        "jogos_analisados": total_jogos,
        "aproveitamento": f"{win_rate:.1f}%",
        "media_gols_marcados": round(soma_gols_pro / total_jogos, 2),
        "media_gols_sofridos": round(soma_gols_contra / total_jogos, 2),
        "posse_media": f"{(soma_posse / total_jogos):.1f}%",
        "chutes_realizados_por_jogo": round(soma_chutes_feitos / total_jogos, 1),
        "chutes_concedidos_por_jogo": round(soma_chutes_sofridos / total_jogos, 1),
        "escanteios_por_jogo": round(soma_escanteios / total_jogos, 1),
        "bolas_recuperadas_por_jogo": round(soma_recuperadas / total_jogos, 1),
        "gols_esperados": media_xg_favor,
        "gols_esperados_contra": media_xg_contra
    }

with open('dados_selecoes.json', 'w', encoding='utf-8') as f:
    json.dump(output_site, f, ensure_ascii=False, indent=4)

print("\n--- Pipeline 100% Finalizado! ---")
print("Arquivo 'dados_selecoes.json' gerado com a nova métrica preditiva de xG!")