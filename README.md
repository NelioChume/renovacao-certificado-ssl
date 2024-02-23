#  Renovação de Certificados Let's Encrypt

Este script Bash automatiza a renovação de certificados Let's Encrypt que estão prestes a expirar. Ele verifica todos os diretórios dentro do diretório "/etc/letsencrypt/live" em busca de certificados com extensão ".org". Se um certificado estiver prestes a expirar (com menos de 15 dias de validade restantes), o script irá renová-lo utilizando o Certbot.

## Instalação no Ubuntu Server:penguin:

- Certifique-se de que o Certbot está instalado e configurado corretamente em seu sistema:
  `` certbot --version``
1. Clonar o repositório:
   
   ```
   $ git clone https://github.com/NelioChume/renovacao-certificado-ssl.git
   ```

2. Aceda ao directório e dê permissão de execução ao arquivo:
   
   ```
   $ cd /Generate_SSL
   ```
   
   ```
   $ sudo chmod +x script.sh
   ```

3. Execute o script:
   
   ```
   $ ./script.sh
   ```
   
   

## Requisitos:dart:

- Certbot deve estar instalado e configurado corretamente.
- Este script assume que os certificados Let's Encrypt estão armazenados em "/etc/letsencrypt/live" e que os diretórios dentro desse diretório correspondem aos domínios dos certificados.

## Contribuição :writing_hand:

- Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Autor:massage:

Este script foi desenvolvido por Nélio Chume :mozambique:








