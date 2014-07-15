django-gunicorn
===============

django-gunicorn is a very simple Django app to provide Gunicorn integration
with `runserver`.

Status
------

The current state of this project is considered extremely experimental. It was
tested with Gunicorn 19.0.0 only. It depends on it actually. This app makes use
of the new `--reload` option which allows for code reloading while Gunicorn is
running.

Issues and pull requests welcomed!
