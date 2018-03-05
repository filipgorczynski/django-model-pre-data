from django.apps import AppConfig
from django.db import DEFAULT_DB_ALIAS

from .utils import is_database_synchronized


class ToastrConfig(AppConfig):
    name = 'toastr'

    def ready(self):
        from .models import ToastrType, PREDEFINED_TOASTR_TYPES
        # Prevent executing before applying migrations
        if is_database_synchronized(DEFAULT_DB_ALIAS):
            for title, color in PREDEFINED_TOASTR_TYPES.items():
                try:
                    ToastrType.objects.get(title=title)
                except ToastrType.DoesNotExist:
                    new_toastr_type = ToastrType.objects.create(
                        title=title,
                        color=color
                    )
                    new_toastr_type.save()
