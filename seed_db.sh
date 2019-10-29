#!/bin/bash

rm -rf budgetappapi/migrations
rm db.sqlite3
python manage.py makemigrations budgetappapi
python manage.py migrate
python manage.py loaddata user
python manage.py loaddata token
python manage.py loaddata budgeter
python manage.py loaddata department
python manage.py loaddata departmenthour
python manage.py loaddata projectdepartment
python manage.py loaddata projectbudget

# 1. Save that in a seed_db.sh file
# 2. Run chmod +x seed_db.sh (in bash only not Windows Terminal)
# 3. Run ./seed_db.sh
