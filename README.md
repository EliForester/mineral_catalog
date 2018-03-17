# Mineral Catalog
Project to catalog minerals

## Getting Started

Clone the repository

Run the following:

```
  python manage.py makemigrations
  python manage.py migrate
  python manage.py populate_mineral_db 
  python manage.py runserver 0.0.0.0:8000
```

**_populate_mineral_db_** *is a command added to do the initial data load - without running this the project won't have any data*

### Prerequisites

Created on Python 3 w Django 2

requirements.txt
```
Django==2.0.3
pytz==2018.3
```

## Running the tests

```
python manage.py tests
```
