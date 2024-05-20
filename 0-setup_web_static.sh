#!/usr/bin/env bash
# Script to set up web servers for deploying web_static

# Update the package index
sudo apt-get update

# Install Nginx web server
sudo apt-get -y install nginx

# Allow Nginx HTTP traffic through the firewall
sudo ufw allow 'Nginx HTTP'

# Create necessary directories for web_static deployment
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

chmod 777 /data/web_static/releases/test

# Create a test HTML file in the test release directory
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link to the test release directory
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership of the /data/ directory to the ubuntu user
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content from the symbolic link
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart Nginx to apply the new configuration
sudo service nginx start
