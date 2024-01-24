from cryptography import x509
from cryptography.hazmat.backends import default_backend
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()
cert_path = os.getenv("FILE_PATH")

def days_until_expiry(cert_path):
    with open(cert_path, 'rb') as cert_file:
        cert_data = cert_file.read()

    cert = x509.load_pem_x509_certificate(cert_data, default_backend())
    expiration_date = cert.not_valid_after

    current_date = datetime.utcnow()
    days_remaining = (expiration_date - current_date).days

    return days_remaining

if __name__ == "__main__":

    try:
        remaining_days = days_until_expiry(cert_path)
        print(f"O certificado expira em {remaining_days} dias.")
    except Exception as e:
        print(f"Erro ao processar o certificado: {e}")
