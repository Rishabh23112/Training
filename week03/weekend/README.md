# Task Tracker API

A Django Task Tracker with a server-rendered task UI and an authenticated REST API. Tasks belong to the signed-in user, so API responses and detail operations are scoped to that user.


## Setup


```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```


## API overview

Base URL: `http://127.0.0.1:8000/api/`

All API endpoints require authentication. In a browser, sign in first and use the browsable API. From the command line, pass `-u username:password` to `curl` to use Basic authentication.

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/api/tasks/` | List the current user's tasks |
| `POST` | `/api/tasks/` | Create a task for the current user |
| `GET` | `/api/tasks/<id>/` | Retrieve one of the current user's tasks |
| `PUT` / `PATCH` | `/api/tasks/<id>/` | Replace or partially update a task |
| `DELETE` | `/api/tasks/<id>/` | Delete a task |

### Task fields

| Field | Required | Rules |
| --- | --- | --- |
| `title` | Yes | 1–200 characters; whitespace-only titles are rejected |
| `description` | No | Up to 1,000 characters |
| `status` | Yes | `todo`, `in-progress`, or `done` |
| `due_date` | No | ISO 8601 date: `YYYY-MM-DD`; cannot be in the past |
| `id`, `created_at`, `updated_at` | No | Server-generated, read-only |


Example task response:

```json
{
    "id": 1,
    "title": "test",
    "description": "test desc",
    "status": "in-progress",
    "due_date": "2026-09-22",
    "created_at": "2026-09-21T09:22:42.346499+05:30",
    "updated_at": "2026-09-21T09:27:30.057487+05:30"
}
```

## Usage examples

Set credentials once for the examples below:

```bash
API_URL="http://127.0.0.1:8000/api/tasks/"
AUTH="your_username:your_password"
```

List tasks:

```bash
curl -u "$AUTH" "$API_URL"
```

Create a task:

```bash
curl -u "$AUTH" -X POST "$API_URL" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "New task",
    "description": "Task description",
    "status": "todo",
    "due_date": "2026-09-22"
  }'
```

Retrieve a task:

```bash
curl -u "$AUTH" "${API_URL}1/"
```

Partially update a task:

```bash
curl -u "$AUTH" -X PATCH "${API_URL}1/" \
  -H "Content-Type: application/json" \
  -d '{"status": "done"}'
```

Delete a task:

```bash
curl -u "$AUTH" -X DELETE "${API_URL}1/" -i
```

## Filtering

Filtering is available only on `/api/tasks/`.
| Query parameter | Example | Effect |
| --- | --- | --- |
| `status` | `?status=todo` | Return tasks with the supplied status |
| `due_before` | `?due_before=2026-09-22` | Return tasks due on or before this date |
| `due_after` | `?due_after=2026-09-19` | Return tasks due on or after this date |

```bash
# Filter by status
curl -u "$AUTH" "${API_URL}?status=todo"

# Filter by date range
curl -u "$AUTH" "${API_URL}?due_after=2026-09-19&due_before=2026-09-22"

# Combine filters
curl -u "$AUTH" "${API_URL}?status=in-progress&due_before=2026-09-22"
```


## Validation and errors

Successful creates return `201 Created`, successful updates return `200 OK`, and deletes return `204 No Content`. Invalid input returns `400 Bad Request` with field-level errors when applicable; requesting a task that is absent or belongs to another user returns `404 Not Found`.
