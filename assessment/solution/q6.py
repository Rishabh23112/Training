""" The given function is too slow. What’s actually happening under the hood, and how would you fix it?

def task_report():
    lines = []
    for task in Task.objects.all():
        lines.append(f"{task.title} — owner: {task.owner.email}")
    return lines """


def task_report():
    """ 
    The previous function was too slow because it was taking N+1 queries to process .
    1 query for loading the data and +N queries for performing the actions on the each row.

    So, to prevent the N+1 we need to optimize it by using select_related() or prefetch_related().
    """
    lines = []
    for task in Task.objects.select_related("owner"):
        lines.append(f"{task.title} — owner: {task.owner.email}")
    return lines