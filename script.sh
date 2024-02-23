#!/bin/bash

# Diretório onde os certificados Let's Encrypt estão localizados
diretorio_letsencrypt="/etc/letsencrypt/live"

# Arquivo de log
log_file="/renovacao-certificado-ssl/log.log"

# Função para registrar mensagens no arquivo de log
log() {
    local message="$1"
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $message" >> "$log_file"
}

# Função para verificar a validade do certificado
verificar_validade_certificado() {
    local caminho_certificado="$1"
    local data_fim=$(openssl x509 -enddate -noout -in "$caminho_certificado" | sed 's/notAfter=//')
    data_fim=$(date -d"$data_fim" '+%s')
    local data_atual=$(date '+%s')
    local dias_restantes=$((($data_fim - $data_atual) / 86400))
    echo "$dias_restantes"
}

# Redirecionar saída para o arquivo de log
exec > >(tee -a "$log_file")
exec 2>&1

# Loop através de cada diretório
for diretorio in "$diretorio_letsencrypt"/*; do
    if [ -d "$diretorio" ]; then
        caminho_certificado="$diretorio/fullchain.pem"
        if [ -f "$caminho_certificado" ]; then
            dias_restantes=$(verificar_validade_certificado "$caminho_certificado")
            if [ "$dias_restantes" -le 15 ]; then
                certbot renew
                log "Certificado renovado em $diretorio"
            else
                log "Certificado em dia em $diretorio"
            fi
        else
            log "Certificado não encontrado em $diretorio"
        fi
    fi
done
