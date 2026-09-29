"""A model has been registered with the Django admin site so it can be searched and filtered, but neither the search box nor the filters show up, and no error is thrown. Here’s the code — find the bug(s):

from django.contrib import admin
from .models import Task

class TaskAdmin:
    list_display = ("title", "status", "due_date")
    search_fields = "title"
    list_filter = "status"

admin.site.register(Task)

"""

from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    """
        Bug1: search_fields and list_filter should be a tuple.
        Bug2 : we should use admin decorator to register admin above the class.
        Bug3 : TaskAdmin must be inherited from admin.ModelAdmin
    """
    list_display = ("title", "status", "due_date")
    search_fields = ("title")
    list_filter = ("status")

