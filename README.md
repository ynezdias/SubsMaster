# SubsMaster
Subcription Manager
Mnaging Subscriptions of Users 

Pre-Requisites
Python 3.8
Pip
Git
Steps to run:
In PipFile, the dependencies are mentioned. It is recommended to run the app inside a virtual environment to avoid conflict of existing dependencies.

Run the command pip install pipenv

Run pipenv shell. Creates virtual env

Run pipenv install. Installs dependencies from the PipFile and creates PipFile.lock

Run python dashboard_project/manage.py runserver to start the server

Open http://127.0.0.1:8000/dashboard to start

USE THE FOLLOWING STEPS

1.Create and activate a virtualenv (Python 3)
pipenv --python 3 shell

2.Install requirements
pipenv install

3.Create a MySQLlite database

4. Init database
./manage.py makemigrations

5.Init database
./manage.py migrate

6.Run tests
./manage.py test

7.Create admin user
./manage.py createsuperuser

8.Run development server
./manage.py runserver


ScreenShot
![Screenshot 2023-08-06 103953](https://github.com/ynezdias/SubsMaster/assets/88530255/3c34f8c1-95f4-433a-9eed-9fcb9232a41e)
