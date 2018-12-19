# Communal Service Accounting App
Water and electricity counters data tracking and management application

# Description
The application is intended to keep your communal services counters indicators up-to date.

# Requirements
The application is tested to run with the following environment:
  * Python 3.7.1

# Environment preparation
```
virtualenv --python=python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

# Run tests
```
python -m flake8 tests commapp
python -m pylint tests commapp
python commapp/manage.py test
```

# Start server
```
python commapp/manage.py runserver
```
