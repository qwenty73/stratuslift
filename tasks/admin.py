from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'mechanic')

admin.site.register(Task, TaskAdmin)
