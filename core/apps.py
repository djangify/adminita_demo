from django.apps import AppConfig
from django.db import connection


class CoreConfig(AppConfig):
    name = "core"

    def ready(self):
        with connection.cursor() as cursor:
            cursor.execute("PRAGMA journal_mode=WAL;")
            cursor.execute("PRAGMA synchronous=NORMAL;")
