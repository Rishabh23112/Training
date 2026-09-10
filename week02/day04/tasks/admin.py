from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    columns = ("title", "status", "due_date", "created_at")
    filter = ("status", "due_date")
    search = ("title", "description")
    date_hierarchy = "created_at"


# Register your models here.
