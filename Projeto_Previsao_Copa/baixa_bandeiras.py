import urllib.request
import os

# Nossa lista de códigos de bandeiras
FLAGS = {
  'CAN': 'ca', 'MEX': 'mx', 'USA': 'us', 'ENG': 'gb-eng', 'FRA': 'fr', 'ESP': 'es', 
  'POR': 'pt', 'GER': 'de', 'NED': 'nl', 'BEL': 'be', 'CRO': 'hr', 'SUI': 'ch', 
  'NOR': 'no', 'SCO': 'gb-sct', 'AUT': 'at', 'BIH': 'ba', 'SWE': 'se', 'TUR': 'tr', 
  'CZE': 'cz', 'JPN': 'jp', 'IRN': 'ir', 'JOR': 'jo', 'KOR': 'kr', 'UZB': 'uz', 
  'AUS': 'au', 'QAT': 'qa', 'KSA': 'sa', 'ALG': 'dz', 'CPV': 'cv', 'EGY': 'eg', 
  'GHA': 'gh', 'CIV': 'ci', 'MAR': 'ma', 'SEN': 'sn', 'RSA': 'za', 'TUN': 'tn',
  'ARG': 'ar', 'BRA': 'br', 'COL': 'co', 'ECU': 'ec', 'PAR': 'py', 'URU': 'uy',
  'PAN': 'pa', 'CUW': 'cw', 'HTI': 'ht', 'NZL': 'nz', 'COD': 'cd', 'IRQ': 'iq'
}

# Cria uma pasta chamada 'flags' se ela não existir
if not os.path.exists('flags'):
    os.makedirs('flags')

print("Iniciando o download das bandeiras...")

for pais, codigo in FLAGS.items():
    # Vamos baixar todas no tamanho 80 (maior resolução que usamos)
    url = f"https://flagcdn.com/w80/{codigo}.png"
    destino = f"flags/{codigo}.png"
    
    try:
        urllib.request.urlretrieve(url, destino)
        print(f"Sucesso: {codigo}.png salva!")
    except Exception as e:
        print(f"Erro ao baixar a bandeira de {pais}: {e}")

print("\n--- Todas as bandeiras foram baixadas e salvas na pasta 'flags'! ---")