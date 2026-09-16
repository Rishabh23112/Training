from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "status", "due_date")

    list_filter = ("status", "due_date", "user")

    search_fields = ("title", "description", "user__username")


# Register your models here.
