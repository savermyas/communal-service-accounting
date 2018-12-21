# Communal Service Accounting App
Water and electricity counters data tracking and management application

# Description
The application is intended to keep your communal services counters indicators up-to date.
It uses [Django][1] as a web-framework and [SlickGrid][2] to display the data.

# Requirements
The application is tested to run with the following environment:
  * Python 3.7.1

# Environment preparation
## Python virtual environment
```
virtualenv --python=python3 venv
source venv/bin/activate
pip install -r requirements.txt
```
## JavaScript dependencies
```
curl -sL https://github.com/6pac/SlickGrid/archive/2.3.16.tar.gz > slickgrid.tar.gz
tar -xf slickgrid.tar.gz
cp SlickGrid-2.3.16/lib/*.js commapp/commapp/static/js/
```

# Run tests
```
python -m flake8 tests commapp
python -m pylint tests commapp/commapp
python commapp/manage.py test
```

# Start server
```
python commapp/manage.py runserver
```

[1]: https://www.djangoproject.com
[2]: http://slickgrid.net
