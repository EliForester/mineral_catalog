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
django-debug-toolbar==1.9.1
peewee==3.1.5
pytz==2018.3
sqlparse==0.2.4
```

## Running the tests

```
python manage.py tests
```

## Debug Toolbar

Can be toggled by setting USE_DEBUG_TOOLBAR to True in settings.py

```
USE_DEBUG_TOOLBAR = True
```

## Test coverage

```
Name                                                  Stmts   Miss  Cover
-------------------------------------------------------------------------
TOTAL                                                   189     32    83%
```