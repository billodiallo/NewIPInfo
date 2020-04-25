SetUp / Installation Requirements
Prerequisites
python3.6
pip
virtualenv
Cloning
In your terminal:
Running the Application
Creating the virtual environment

  $ python3.6 -m venv --without-pip virtual
  $ source virtual/bin/env
  $ curl https://bootstrap.pypa.io/get-pip.py | python
Installing Flask and other Modules

  $ python3.6 -m pip install Flask
  $ python3.6 -m pip install Flask-Bootstrap
  $ python3.6 -m pip install Flask-Script