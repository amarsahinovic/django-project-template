Django project template
=======================

Simple django project template, with some basic default setup.

Quick info - read before using this template!
---------------------------------------------

Apps are stored in `apps/` directory with each app having her own subdirectory.
Templates shared among all apps go to `apps/templates/`, app specific templates go to `apps/APPNAME/templates/APPNAME`
Shared static files go to `apps/static/`, app specific static files go to `apps/APPNAME/static/APPNAME`

Configuration files are stored inside `config/` directory.
Common configuration options are in `common.py`
For local development, copy and rename (don't delete) `repo_local_settings.py` to `local_settings.py`
For production, copy and rename (don't delete) `repo_production_settings.py` to `production_settings.py`
If you create both `local_settings.py` and `production_settings.py`, `production_settings.py` will be used.
Both `local_settings.py` and `production_settings.py` are in `.gitignore` file, so they will not be commited to repo.
If you create your own setting file, make sure you put this at the top: `from common import *`

When you run the project `settings.py` will first try to import settings from `production_settings.py`, and if that fails, it will try to import `local_settings.py`, so make sure you create appropriate files.
All your urls are defined in `urls.py` which are located in apps directories and need to be included from `urls.py` in project root

You should put your python libraries in `libs/` directory

Directory `static/` under project root is user for collectstatic.
Directory `media/` for media files.

Directories `static/` and `media/` contain their own .gitignore files, so that files in these directories are not sent to repo.

Directory `docs/` is for documentation.

### Note: In the default `repo_local_settings.py` and `repo_production_settings.py` I have used `psycopg2` as the database ENGINE, so if you don't use this, change it before starting the project, otherwise you will see some errors.

Also included in this template is HTML5 Boilerplate, and two dummy apps just to test if everything works.