#!/bin/sh

# Waits for proxy to be availbe, then gets the first certificate

set -e

#nc - netcat checks if port 80 is accessible 
until nc -z proxy 80; do
    echo "Waiting for proxy"
    sleep 5s & wait ${!}
done

echo "Getting certf"

certbot certonly \
    --webroot \
    --webroot-path "/vol/www/" \
    -d "$DOMAIN" \
    --email $EMAIL \
    --rsa-key-size 4096 \
    --agre-tos \
    --noninteractive