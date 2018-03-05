from django.contrib import admin
from django.utils.html import format_html

from . import models


def short_description(desc):
    def inner(f):
        f.short_description = desc
        return f

    return inner


@admin.register(models.ToastrType)
class ToastrTypeAdmin(admin.ModelAdmin):
    fields = ('title', 'color')
    list_display = (
        'title',
        'color_display',
    )
    search_fields = (
        'title',
    )

    @short_description("BACKGROUND COLOR")
    def color_display(self, obj):
        style = ''.join([
            f'display: inline-block;'
            f'border: 1px solid #000;'
            f'width: 15px;'
            f'height: 15px;'
            f'background-color: #{obj.color};'
        ])
        return format_html(f'<span style="{style}"></span> #{obj.color}')

    def has_delete_permission(self, request, obj=None):
        # Zablokuj możliwość usuwania w panelu administracyjnym dla naszych danych
        if obj and obj.title in models.PREDEFINED_TOASTR_TYPES.keys():
            return False

        return True

    def has_change_permission(self, request, obj=None):
        # Zablokuj możliwość edycji tytułu w panelu administracyjnym dla naszych danych
        if obj and obj.title in models.PREDEFINED_TOASTR_TYPES.keys():
            self.readonly_fields = ['title']
        else:
            self.readonly_fields = []

        return True


@admin.register(models.Toastr)
class ToastrAdmin(admin.ModelAdmin):
    list_display = [
        'message',
        'toastr_type',
    ]
    list_filter = ['toastr_type__title']
    search_fields = ['message']
