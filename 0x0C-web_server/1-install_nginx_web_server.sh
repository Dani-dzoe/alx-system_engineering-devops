#!/usr/bin/env bash
# Install nginx server
apt-get update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
echo "Hello World!" > /var/www/index.html
service nginx start
