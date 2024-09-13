from django.contrib import admin
from .models import *


class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'todo_status', 'created']
    list_display_links = ['id', 'user', 'title', 'todo_status', 'created']
    search_fields = ['id', 'user', 'title', 'todo_status', 'created']


admin.site.register(Todo, TodoAdmin)