# Vend-O-Matic

Built using Python, Django, and the Django REST Framework

## Getting Started

These instructions are to walk you through cloning down the repository, get the virtual environment running, and set up the database.

### Requirements

* Computer
* Bash Terminal
* [Python 3](https://www.python.org/downloads/)
* [Pip](https://pip.pypa.io/en/stable/installing/)
* Text editor (Visual Studio Code)

### Installing

1. In the terminal, select a directory to use, and then clone down this repository and cd into it.

2. Once inside this repository, cd into `Vending_test` and open your VSCode here with
`code .`
#### Virtual Environment
1. Create your virtual environment
```
python -m venv vendingTestEnv
```
* Start virtual environment on Mac
```
source ./vendingTestEnv/bin/activate
```
* Start virtual environment on Windows
- in the Command Prompt, cd into ```VendingTestEnv/Scripts```
- activate
- then cd back to ```Vending_test```

6. Ensure that you are at ```Vending_test``` and then it is time to install the app's dependencies:
```
pip install -r requirements.txt
```

7. How to DL the set up fixtures

#### Setting Up the Database (`Redo_db.sh`)
This is our way of managing database migrations.

* Set execute permissions by running the below in your terminal
```
chmod -x Reset_db.sh
```
 **CLOSE ALL CONNECTIONS TO THE DATABASE**
* Run the script
```
./Restet_db.sh
```
* Running the above in the terminal will also be how to reset the database if you would like to rerun any tests

* Fire up that server! (will need to be completed in command prompt for windows)
```
python manage.py runserver
```

### Testing
The original testing for this project was conducted using POSTMAN, click [here](https://www.getpostman.com/downloads/) to download
