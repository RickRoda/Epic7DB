# Epic7DB
Database web app for the gacha game, Epic Seven.

Currently in development in Python + Django REST Framework + HTML/CSS/JS

__If you would like to contribute, please send me a message, this project will not run without the settings.py file which is currently untracked for security reasons__

# Installation

I have created a pythonenvironment for anyone who is interested in working on this project

In order to execute the app and begin contibuting, complete the following:

__Step 0 - Contact me to obtain the settings.py file. App will not run without this and the SECRET_KEY__

__Step 0.5 - Once you have obtained the settings.py file, place it inside the epic7db/epic7db folder__

__Step 1__ - [Install Python 3.6](https://www.python.org/downloads/) or later.

__Step 2__  - Install pipenv.
In your command line, type,
```
pip install pipenv
```

__Step 3__ - Install dependencies and activate environment.
Navigate to the root folder of the project and type,
``` 
pipenv shell
```
On its initial run, pipenv will read the PIPFILE and install all the necessary dependencies inside a virtual environment to run the application. You will use this command to re-activate your environment once its been exited.

__Step 4__ - Create your local database.
Once the environment is activated, from the root project directory, type,
```
python manage.py migrate
```
This will create a local SQLite Database file called sqlite.db in the root directory of the app.

__Step 5__ - Create a superuser account.
From the command line, type 
```
python manage.py createsuperuser
```
Follow the prompts and create your user account. This account will be used to login to the admin panel, which is located at URL
__127.0.0.1:8000/admin__


__Step 5__ - Run the Application.
To run the application in development mode, type,
```
python manage.py runserver
```
By Default, the app will run on 127.0.0.1:8000 and can be accessed via web browser.


# Some of the Features I'm aiming to provide...

Character Stats

Character Skills

Character Awakening Constellations

Damage Multiplier Approximator

Artifact Information

Labrynth Maps

Catalysts and Crafting Material Locations

