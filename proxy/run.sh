#!/bin/bash

set -e

echo "Checking for dhparams.pem"
# Creating dhparams if they not exist
if [ ! -f "/vol/proxy/ssl-dhparams.pem" ]; then
    echo "dhparams.pem does not exist - creating..."
    openssl dhparam -out /vol/proxy/ssl-dhparams.pem 2048
fi

# Don't replace these with envsubst

export host=\$host
export request_url=\$request_uri

#Replacing nginx configuration depending on existance of ssl certificate
echo "Checking for fullchain.pem"
if [ ! -f "/etc/letsencrypt/live/${DOMAIN}/fullchain.pem" ]; then
    echo "No SSL certificate, enabling http only"
    envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf
else
    echo "SSL certificate found, enabling https"
    envsubst < /etc/nginx/default-ssl.conf.tpl > /etc/nginx/conf.d/default.conf
fi

nginx -g 'deamon off;'