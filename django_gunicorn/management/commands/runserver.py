from django.core.management.base import BaseCommand
from django.core.servers.basehttp import get_internal_wsgi_application

import gunicorn.app.base
import gunicorn.config


class DjangoApplication(gunicorn.app.base.Application):

    def __init__(self, usage=None, prog=None, callable=None):
        self.usage = usage
        self.cfg = None
        self.callable = callable
        self.prog = prog
        self.logger = None
        self.do_load_config()

    def do_load_config(self):
        self.cfg = gunicorn.config.Config(self.usage, prog=self.prog)
        self.cfg.set("errorlog", "-")
        self.cfg.set("reload", True)


class Command(BaseCommand):

    help = "Starts a lightweight Web server for development."
    requires_system_checks = False

    def get_handler(self, *args, **options):
        """
        Returns the default WSGI handler for the runner.
        """
        handler = get_internal_wsgi_application()
        from django.contrib.staticfiles.handlers import StaticFilesHandler
        return StaticFilesHandler(handler)

    def handle(self, *args, **options):
        DjangoApplication(callable=self.get_handler()).run()
