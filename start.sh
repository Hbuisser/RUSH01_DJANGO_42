#!/bin/sh

# python -m pip install django-ex00/dist/django-ex00-0.1.tar.gz
python manage.py collectstatic

brew services stop nginx
brew install nginx
brew services start nginx
cp ./config/rush01_nginx.conf ~/.brew/etc/nginx/servers/
brew services restart nginx

# python3 manage.py collectstatic
python3 manage.py makemigrations
python3 manage.py migrate


python3 -m pip install gunicorn
gunicorn -c ./config/gunicorn_config.py rush01.wsgi 

nginx 