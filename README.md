# Communal Service Accounting App
Water and electricity counters data tracking and management application

# Description
The application is intended to keep your communal services counters indicators up-to date.
It uses [Django][1] as a web-framework and [SlickGrid][2] to display the data.

# Requirements
The application is tested to build and run with the following environment:
  * [Python 3.7.1][3]
  * [NPM 6.4.1][4]

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
cp SlickGrid-2.3.16/slick.grid.css commapp/commapp/static/
cp SlickGrid-2.3.16/slick-default-theme.css commapp/commapp/static/
cp SlickGrid-2.3.16/slick.grid.js commapp/commapp/static/
cp SlickGrid-2.3.16/slick.core.js commapp/commapp/static/
cp SlickGrid-2.3.16/lib/jquery-1.11.2.min.js commapp/commapp/static/
cp SlickGrid-2.3.16/lib/jquery.event.drag-2.3.0.js commapp/commapp/static/
cp SlickGrid-2.3.16/css/smoothness/jquery-ui-1.11.3.custom.min.css commapp/commapp/static/
cp -r SlickGrid-2.3.16/css/smoothness/images commapp/commapp/static/
cp -r SlickGrid-2.3.16/images commapp/commapp/static/
```

# Run tests
```
python -m flake8 tests commapp
python -m pylint tests commapp/commapp
python commapp/manage.py test
```

# Start server
```
python commapp/manage.py migrate
python commapp/manage.py loaddata test
python commapp/manage.py runserver
```

[1]: https://www.djangoproject.com
[2]: http://slickgrid.net
[3]: https://www.python.org/downloads/release/python-371/
[4]:
