# Django-UrlShortner-with-Google-Oauth-Implementation

Project Setup steps:

1) open project at vscode or pycharm
2) create virtual env and install all the dependencies using requirements.txt file
3) setup mysql databae by making some changes to database setiings inside settings.py file
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'urldb',    create database with same name in mysql or else u need to specify your databse name here at settings.py file
        'USER': 'root',
        'PASSWORD': '-------', use your mysql password here
        'HOST':'localhost',
        'PORT':'3306',
    }
}

4)install mysqlclient usin pip
5) run python manage.py makemigrations and python manage.py migrate command one sequentially
6) run python manage.py runserver to run development server 
7)click on link given on console after executing above command  which will redirect u to home page.
Starting development server at   http://127.0.0.1:8000/

Note:
1) I have created short links using uuid field,
2) you need to click on refresh button to see click count increases after you get back from redirected Url or site.
3) last clicked coloumn will get updated after clicking on short link at least for once.
4) when short link created first time it will display none at last clicked coloumn.
   
