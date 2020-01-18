Built using Python, Django, and the Django REST Framework for serving data to the
[client-side application](https://github.com/bparker12/budget_app_client) via HTTP

# Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Requirements

* Computer
* Bash Terminal
* [Python 3](https://www.python.org/downloads/)
* [Pip](https://pip.pypa.io/en/stable/installing/)
* Text editor (Visual Studio Code)

### Installing

1. Clone down this repository and cd into it.
2. Once inside this repository, cd into `budget_app_api` and open your VSCode here with
`code .`
1. Create your virtual environment
```
python -m venv budgetAppEnv
```
* Start virtual environment on Mac
```
source ./budgetAppEnv/bin/activate
```
* Start virtual environment on Windows
```
source ./budgetAppEnv/Scripts/activate
```
5. Run `cd ..` You should be in a directory containing `requirements.txt`
6. Install the app's dependencies:
```
pip install -r requirements.txt
```

7. How to DL the set up fixtures

## `seed_db.sh`
This is our way of managing database migrations.

* Set execute permissions
```
chmod -x seed_db.sh
```
* **CLOSE ALL CONNECTIONS TO THE DATABASE**
* Run the script
```
./seed_db.sh
```

* Fire up that server! (will need to be completed in command prompt for windows)
```
python manage.py runserver
```
