import os

caminho_base = "/etc/letsencrypt/live/"

for diretorio in os.listdir(caminho_base):
    caminho_completo = os.path.join(caminho_base, diretorio, "fullchain.pem")
    
    if os.path.exists(caminho_completo):
        path_base = f"{caminho_base}{diretorio}/"
        print(f"O arquivo fullchain.pem foi encontrado em {path_base}")
