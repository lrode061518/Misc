#!/usr/bin/env sh

OUTPUT_KEY="/etc/ssl/private/selfsigned.key"
OUTPUT_CRT="/etc/ssl/certs/selfsigned.crt"

sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout $OUTPUT_KEY -out $OUTPUT_CRT

