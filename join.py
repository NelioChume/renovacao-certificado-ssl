from cryptography import x509
from cryptography.hazmat.backends import default_backend
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()
caminho_base = "/etc/letsencrypt/live/"

def days_until_expiry(cert_path):
    with open(cert_path, 'rb') as cert_file:
        cert_data = cert_file.read()

    cert = x509.load_pem_x509_certificate(cert_data, default_backend())
    expiration_date = cert.not_valid_after

    current_date = datetime.utcnow()
    days_remaining = (expiration_date - current_date).days

    return days_remaining

if __name__ == "__main__":
    for diretorio in os.listdir(caminho_base):
        caminho_completo = os.path.join(caminho_base, diretorio, "fullchain.pem")

        if os.path.exists(caminho_completo):
            try:
                remaining_days = days_until_expiry(caminho_completo)
                print(f"O certificado em {caminho_completo} expira em {remaining_days} dias.")
            except Exception as e:
                print(f"Erro ao processar o certificado em {caminho_completo}: {e}")
