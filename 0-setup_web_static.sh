#!/usr/bin/env bash
# Bash script that sets up a web server for the deployment of web_static.
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
sudo ln -fs /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
file="/etc/nginx/sites-available/default"
sudo sed -i "/listen 80 default_server;/a \\\n\\tlocation /hbnb_static {\\n\\t\\talias /data/web_static/current/;\\n\\t}" $file
sudo service nginx restart