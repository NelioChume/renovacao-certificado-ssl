import os
import subprocess
from datetime import datetime, timedelta

# Função para verificar a validade do certificado
def verificar_validade_certificado(caminho_certificado):
    comando = f"openssl x509 -enddate -noout -in {caminho_certificado}"
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    data_fim = resultado.stdout.replace('notAfter=', '', 1)
    data_fim = datetime.strptime(data_fim.strip(), '%b %d %H:%M:%S %Y %Z')
    return data_fim

# Diretório onde os certificados Let's Encrypt estão localizados
diretorio_letsencrypt = "/etc/letsencrypt/live"

# Obter todos os diretórios dentro de /etc/letsencrypt/live
diretorios = [diretorio for diretorio in os.listdir(diretorio_letsencrypt) if os.path.isdir(os.path.join(diretorio_letsencrypt, diretorio))]

# Loop através de cada diretório
for diretorio in diretorios:
    if diretorio.endswith('.org'):
        caminho_certificado = os.path.join(diretorio_letsencrypt, diretorio, "fullchain.pem")
        if os.path.exists(caminho_certificado):
            data_atual = datetime.now()
            data_fim_validade = verificar_validade_certificado(caminho_certificado)
            dias_restantes = (data_fim_validade - data_atual).days
            if dias_restantes <= 15:
                print(f"Renovando certificado em {os.path.join(diretorio_letsencrypt, diretorio)}")
                subprocess.run(["certbot", "renew"])
