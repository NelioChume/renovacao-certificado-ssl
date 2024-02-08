import os
from dotenv import load_dotenv
import subprocess
from OpenSSL import crypto
from datetime import datetime, timedelta

load_dotenv()

# Obtenha os caminhos do arquivo e do Certbot do arquivo .env
caminho_base = os.getenv("FILE_PATH")
certbot = os.getenv("CERTBOT_PATH")

def days_until_expiry(cert_path):
    with open(cert_path, 'rb') as cert_file:
        cert_data = cert_file.read()

    cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert_data)
    expiration_date = datetime.strptime(cert.get_notAfter().decode(), "%Y%m%d%H%M%SZ")

    current_date = datetime.utcnow()
    days_remaining = (expiration_date - current_date).days

    return days_remaining

def renew_certificates():
    try:
        result = subprocess.run([certbot, "renew", "--quiet"], capture_output=True, text=True)
        output = result.stdout
        error_output = result.stderr

        if "Cert not yet due for renewal" in output or "No renewals were attempted" in output:
            print("Os certificados não precisam ser renovados neste momento.")
        elif "Congratulations, all renewals succeeded" in output:
            print("Renovação bem-sucedida!")
        else:
            print("Erro ao renovar certificados. Saída do Certbot:")
            print(output)
            print("Saída de erro do Certbot:")
            print(error_output)
    except Exception as e:
        print(f"Erro ao renovar certificados: {e}")

if __name__ == "__main__":
    for diretorio in os.listdir(caminho_base):
        caminho_completo = os.path.join(caminho_base, diretorio, "fullchain.pem")

        if os.path.exists(caminho_completo):
            try:
                remaining_days = days_until_expiry(caminho_completo)
                print(f"O certificado em {caminho_completo} expira em {remaining_days} dias.")
                
                # Se restarem menos de 30 dias, renovar automaticamente
                if remaining_days < 30:
                    renew_certificates()
            except Exception as e:
                print(f"Erro ao processar o certificado em {caminho_completo}: {e}")
