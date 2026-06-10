from curl_cffi import requests
import json
from datetime import datetime

# 1. Mapeamento das seleções
TEAM_MAP = {
    "Canada": "CAN", "Mexico": "MEX", "USA": "USA", "England": "ENG",
    "France": "FRA", "Spain": "ESP", "Portugal": "POR", "Germany": "GER",
    "Netherlands": "NED", "Belgium": "BEL", "Croatia": "CRO", "Switzerland": "SUI",
    "Scotland": "SCO", "Sweden": "SWE", "Turkey": "TUR", "Czech Republic": "CZE",
    "Norway": "NOR", "Austria": "AUT", "Bosnia & Herzegovina": "BIH",
    "Japan": "JPN", "Iran": "IRN", "Jordan": "JOR", "South Korea": "KOR",
    "Uzbekistan": "UZB", "Australia": "AUS", "Qatar": "QAT", "Saudi Arabia": "KSA",
    "Iraq": "IRQ", "Algeria": "ALG", "Cape Verde": "CPV", "Egypt": "EGY",
    "Ghana": "GHA", "Ivory Coast": "CIV", "Morocco": "MAR", "Senegal": "SEN",
    "South Africa": "RSA", "Tunisia": "TUN", "DR Congo": "COD",
    "Argentina": "ARG", "Brazil": "BRA", "Colombia": "COL", "Ecuador": "ECU",
    "Paraguay": "PAR", "Uruguay": "URU", "Panama": "PAN", "Curaçao": "CUW",
    "Haiti": "HTI", "New Zealand": "NZL"
}

# 2. Motor de Extração com Paginação
def fetch_real_schedule():
    print("⏳ Conectando à API do Sofascore e varrendo todas as páginas...")
    
    agenda = {}
    pagina = 0
    jogos_totais = 0
    
    while True:
        url = f"https://www.sofascore.com/api/v1/unique-tournament/16/season/58210/events/next/{pagina}"
        
        try:
            # impersonate="chrome120" é o nosso disfarce bypass TLS
            response = requests.get(url, impersonate="chrome120")
            response.raise_for_status()
            data = response.json()
            
            eventos = data.get('events', [])
            
            # Se a lista de eventos vier vazia, os jogos da Copa acabaram
            if not eventos:
                break
                
            for event in eventos:
                timestamp = event['startTimestamp']
                dt = datetime.fromtimestamp(timestamp)
                
                data_str = dt.strftime("%Y-%m-%d")
                hora_str = dt.strftime("%H:%M")

                time_home = event['homeTeam']['name']
                time_away = event['awayTeam']['name']

                idA = TEAM_MAP.get(time_home, time_home[:3].upper())
                idB = TEAM_MAP.get(time_away, time_away[:3].upper())

                if data_str not in agenda:
                    agenda[data_str] = []

                novo_jogo = {"idA": idA, "idB": idB, "time": hora_str}
                
                # Previne duplicidade
                if novo_jogo not in agenda[data_str]:
                    agenda[data_str].append(novo_jogo)
                    jogos_totais += 1
            
            print(f"Página {pagina} processada com sucesso!")
            pagina += 1
            
        except Exception as e:
            print(f"❌ Erro ao processar a página {pagina}: {e}")
            break

    # 3. Salva no disco
    with open("agenda_copa.json", "w", encoding="utf-8") as f:
        json.dump(agenda, f, ensure_ascii=False, indent=2)

    print(f"✅ Sucesso! agenda_copa.json gerado com {jogos_totais} jogos no total.")

# ESSE É O GATILHO QUE FALTAVA!
if __name__ == "__main__":
    fetch_real_schedule()