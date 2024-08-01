#  Renovação de Certificados Let's Encrypt

Este script Bash automatiza a renovação de certificados Let's Encrypt que estão prestes a expirar. Ele verifica todos os diretórios dentro do diretório "/etc/letsencrypt/live" em busca de certificados com extensão ".org". Se um certificado estiver prestes a expirar (com menos de 15 dias de validade restantes), o script irá renová-lo utilizando o Certbot..

## Instalação no Ubuntu Server:penguin:

- Certifique-se de que o Certbot está instalado e configurado corretamente em seu sistema:
  `` certbot --version``
1. Clonar o repositório:
   
   ```
   $ git clone https://github.com/NelioChume/renovacao-certificado-ssl.git
   ```

2. Aceda ao directório e dê permissão de execução ao arquivo:
   
   ```
   $ cd /renovacao-certificado-ssl
   ```
   
   ```
   $ sudo chmod +x script.sh
   ```

3. Execute o script:
   
   ```
   $ ./script.sh
   ```
   
# Adicionar o script ao crontab para execução automática
# Execute o seguinte comando para abrir o crontab no editor:

 ```
 $ sudo crontab -u root -e
 ```

# Adicione a seguinte linha ao final do arquivo para executar o script diariamente às 3 da manhã:
# Substitua /caminho/renovacao-certificado-ssl/script.sh pelo caminho completo para o scrip
1 0 */15 * * /root/renovacao-certificado-ssl/script.sh >/dev/null 2>> /root/renovacao-certificado-ssl/cronjobs.log

1 0 */15 * * cat /var/log/syslog | grep CRON >> /root/renovacao-certificado-ssl/cron.log 2>> /root/renovacao-certificado-ssl/cronjobs.log; /root/renovacao-certificado-ssl/script.sh >/dev/null 2>> /root/renovacao-certificado-ssl/cronjobs.log


# Salve e feche o editor (geralmente pressionando "Ctrl + X", depois "Y" e "Enter")

# Este cron agendará a execução do script script.sh localizado em /root/renovacao-certificado-ssl/ para ocorrer às 00:01 a cada 15 dias

### Outros comandos para verificar os logs do script
```
   $ cat /var/log/syslog | grep CRON
```

## Requisitos:dart:

- Certbot deve estar instalado e configurado corretamente.
- Este script assume que os certificados Let's Encrypt estão armazenados em "/etc/letsencrypt/live" e que os diretórios dentro desse diretório correspondem aos domínios dos certificados.

## Contribuição :writing_hand:

- Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Autor:massage:

Este script foi desenvolvido por Nélio Chume :mozambique:








