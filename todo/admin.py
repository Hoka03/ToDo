from django.contrib import admin

from todo.models import ToDO


@admin.register(ToDO)
class ToDOAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')
    list_display_links = list_display
