from django.contrib import admin

from .models import SomeCity


@admin.register(SomeCity)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'city')
    list_filter = ('id',)
