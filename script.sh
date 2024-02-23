
#!/bin/bash

# Função para verificar a validade do certificado
verificar_validade_certificado() {
    caminho_certificado="$1"
    data_fim=$(openssl x509 -enddate -noout -in "$caminho_certificado" | sed 's/notAfter=//')
    data_fim=$(date -d"$data_fim" '+%b %d %H:%M:%S %Y %Z')
    echo "$data_fim"
}

# Diretório onde os certificados Let's Encrypt estão localizados
diretorio_letsencrypt="/etc/letsencrypt/live"

# Obter todos os diretórios dentro de /etc/letsencrypt/live
diretorios=$(ls "$diretorio_letsencrypt" | grep -E '.*\.org$')

# Loop através de cada diretório
for diretorio in $diretorios; do
    caminho_certificado="$diretorio_letsencrypt/$diretorio/fullchain.pem"
    if [ -f "$caminho_certificado" ]; then
        data_atual=$(date '+%Y-%m-%d %H:%M:%S')
        data_fim_validade=$(verificar_validade_certificado "$caminho_certificado")
        dias_restantes=$(($(($(date -d"$data_fim_validade" '+%s') - $(date -d"$data_atual" '+%s'))) / 86400))
        if [ "$dias_restantes" -le 15 ]; then
            echo "Renovando certificado em $diretorio_letsencrypt/$diretorio"
            certbot renew
        fi
    fi
done
