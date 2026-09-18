from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "due_date", "status", "created_at")
    list_filter = ("status", "due_date", "created_at")
    search_fields = ("title", "description", "owner__username")


# Register your models here.
