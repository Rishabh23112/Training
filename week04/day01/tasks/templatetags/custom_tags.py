from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name="status_badge")
def status_badge(status):
    badges = {
        "TODO": "<span class='badge badge-yellow'>Todo</span>",
        "IN_PROGRESS": "<span class='badge badge-blue'>In Progress</span>",
        "DONE": "<span class='badge badge-green'>Done</span>",
    }

    html = badges.get(status.upper(), '<span class="badge badge-gray">Unknown</span>')
    return mark_safe(html)
