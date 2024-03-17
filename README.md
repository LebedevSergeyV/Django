# Website Product Placement 
# Production and software for Windows

The project is written on the [Django](https://www.djangoproject.com) framework.
The backend is written in [python](https://www.python.org).
Frontend is written using [bootstrap](https://getbootstrap.com).
This is a website where anyone who wants to register can place an ad.

___

# Links and versions to the website    

* [Lebedev Sergey Vyacheslav](https://github.com/LebedevSergeyVach) – Product Lead & Fullstack Developer.

* [Website](https://serphantom.space) - a link to a website located on its server with a white (external) ip address connected. [LebedevSergeyVach](https://github.com/LebedevSergeyVach). A fresh and constantly updated version of the site.

___

# Project deployment on the server [Debian](https://www.debian.org).

#### Uploading a project.
```commandline
git clone git@github.com:LebedevSergeyVach/WebsiteProductPlacement.git
```
#### The command for configuring and migrating the project database on the Django framework on the server.
```commandline
python manage.py makemigrations
```
```commandline
python manage.py migrate
```
#### Creating and configuring a website administrator.
```commandline
python manage.py createsuperuser
```
#### The command to start the rebuild of the docker site on the server [Debian](https://www.debian.org).
```commandline
sudo docker compose -f "./docker-compose.yml" build --force-rm --no-cache
```
#### The command to run the site docker build on the server [Debian](https://www.debian.org).
```commandline
sudo docker compose -f "./docker-compose.yml" up
```
#### Clearing dockers data and file cache.
```commandline
sudo docker builder prune
```
___

## Documentation for each directory

* `The main application of the framework` - [advertisements](advertisements%2Fadvertisements%2FREADME.md)
* `The main application of the project` - [app advertisements](advertisements%2Fapp_advertisements%2FREADME.md)
* `Authorization application` - [app auth](advertisements%2Fapp_auth%2FREADME.md)
* `Project Template Directory` - [templates](advertisements%2Ftemplates%2FREADME.md)
* `Directory of static project files` - [static](advertisements%2Fstatic%2FREADME.md)
* `The directory of the project's media files` - [media](advertisements%2Fmedia%2FREADME.md)


## List of the main commands used in the project

* `Project Console commands` - [commands](advertisements%2FREADME.md)

---

# Размещение продукции на веб-сайте
# Продукция и программное обеспечение для Windows

Проект написан на фреймворке [Django](https://www.djangoproject.com).
Бэкенд написан на [Python](https://www.python.org).  
Фронтенд разработан с использованием [Bootstrap](https://getbootstrap.com).  
Это веб-сайт, на котором любой желающий может разместить рекламу.

---

## Ссылки и версии веб-сайта    
* [Лебедев Сергей Вячеславович](https://github.com/LebedevSergeyVach) – Ведущий разработчик и Fullstack-разработчик.
* [Веб-сайт](https://serphantom.space) - ссылка на веб-сайт, размещенный на собственном сервере с белым (внешним) IP-адресом. [LebedevSergeyVach](https://github.com/LebedevSergeyVach). Свежая и постоянно обновляемая версия сайта.

---

## Развертывание проекта на сервере [Debian](https://www.debian.org).

#### Загрузка проекта.
```commandline
git clone git@github.com:LebedevSergeyVach/WebsiteProductPlacement.git
```
#### Команда для настройки и миграции базы данных проекта на фреймворке Django на сервере.
```commandline
python manage.py makemigrations
```
```commandline
python manage.py migrate
```
#### Создание и настройка администратора веб-сайта.
```commandline
python manage.py createsuperuser
```
#### Команда для запуска сборки сайта в docker на сервере.
```commandline
sudo docker compose -f "./docker-compose.yml" build --force-rm --no-cache
```
#### Команда для запуска docker-сборки сайта на сервере.
```commandline
sudo docker compose -f "./docker-compose.yml" up
```
#### Очистка данных docker и файлового кэша.
```commandline
sudo docker builder prune
```

---

## Документация для каждого каталога
* `Главное приложение фреймворка` - [advertisements](advertisements%2Fadvertisements%2FREADME.md)
* `Основное приложение проекта` - [app advertisements](advertisements%2Fapp_advertisements%2FREADME.md)
* `Приложение авторизации проекта` - [app auth](advertisements%2Fapp_auth%2FREADME.md)
* `Директория шаблонов проекта` - [templates](advertisements%2Ftemplates%2FREADME.md)
* `Директория статических файлов проекта` - [static](advertisements%2Fstatic%2FREADME.md)
* `Директория медиа файлов проекта` - [media](advertisements%2Fmedia%2FREADME.md)

## Список основных команд, используемых в проекте
* `Консольные команды проекта` - [commands](advertisements%2FREADME.md)

___

`README` - [README.md](README.md)
