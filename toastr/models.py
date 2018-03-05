import re

from django.core.exceptions import ValidationError
from django.db import models


def validate_hex_color(color):
    pattern = re.compile(r'^([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')

    if not pattern.match(color):
        raise ValidationError("Please provide valid hexadecimal color value")

    return color


PREDEFINED_TOASTR_TYPES = {
    'Success': '28a745',
    'Warning': 'ffc107',
    'Info': '17a2b8',
    'Danger': 'dc3545',
}


class ToastrType(models.Model):

    title = models.CharField(max_length=1000)
    color = models.CharField(
        max_length=6, default='ffffff',
        validators=[validate_hex_color]
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Toastr Type"
        verbose_name_plural = "Toastr Types"


class Toastr(models.Model):

    toastr_type = models.ForeignKey(ToastrType)
    message = models.TextField(max_length=1000)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = "Toastr"
        verbose_name_plural = "Toastrs"
