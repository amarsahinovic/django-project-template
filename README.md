Django project template
=======================

Simple django project template, with some basic default setup


Quick info
----------

Apps are stored in `apps/` directory with each app having her own subdirectory.
Templates go to `apps/templates/`, base templates go to root, app specific templates in subdirectory named after the app.
Static files go to `apps/static/`

Configuration files are stored inside `config/` directory.
Common configuration options are in `common.py`
For local development, copy and rename `local_settings.pypy` to `local_settings.py`
For production settings, copy and rename `production_settings.pypy` to `production_settings.py`
Both local_settings.py and production_settings.py are in `.gitignore` file, so they will not be commited to repo.

When you run the project `settings.py` will first try to import settings from `production_settings.py`, and if that fails, it will try to import `local_settings.py`, so make sure you create appropriate files.
All your urls are defined in `urls.py` which are located in apps directories and need to be included from `urls.py` in project root

You should put your python libraries in `libs/` directory

Directory `static/` under project root is user for collectstatic.
Directory `media/` for media files.

Directories `static/` and `media/` contain their own .gitignore files, so that files in these folders are not sent to repo.

Directory `docs/` is for documentation.

Also included in this template is HTML5 Boilerplate, and two dummy apps just to test if everything works.