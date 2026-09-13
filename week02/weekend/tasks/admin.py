from django.contrib import admin

from .models import Task


@admin.action(description="Mark selected as Done")
def mark_as_done(modeladmin, request, queryset):
    queryset.update(status=Task.Status.DONE)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "colored_status",
        "due_date",
        "created_at",
    )

    list_filter = (
        "status",
        "due_date",
    )

    search_fields = ("title",)

    actions = (mark_as_done,)

    @admin.display(description="Status")
    def colored_status(self, obj):
        return obj.get_status_display()
