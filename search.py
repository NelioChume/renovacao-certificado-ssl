import os

caminho_base = "/etc/letsencrypt/live/"

for diretorio in os.listdir(caminho_base):
    caminho_completo = os.path.join(caminho_base, diretorio, "fullchain.pem")
    
    if os.path.exists(caminho_completo):
        print(f"O arquivo fullchain.pem foi encontrado em {caminho_completo}")
    else:
        print(f"O arquivo fullchain.pem não foi encontrado em {caminho_completo}")
