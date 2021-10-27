- Spec
  - Fields of task:
    - name
      - Type: String
    - status
      - Type: Bool
      - Value
        - 0=Incomplete
        - 1=Complete
  - Reponse headers
    - Content-Type=application/json

### 1. GET /tasks (list tasks)

```JSON
{
    "result": [
        {"id": 1, "name": "name", "status": 0}
    ]
}
```

### 2. POST /task (create task)

```JSON
request
{
  "name": "買晚餐"
}

response status code 201
{
    "result": {"name": "買晚餐", "status": 0, "id": 1}
}
```

### 3. PUT /task/<id> (update task)

```JSON
request
{
  "name": "買早餐",
  "status": 1
  "id": 1
}

response status code 200
{
  "name": "買早餐",
  "status": 1,
  "id": 1
}
```

### 4. DELETE /task/<id> (delete task)

response status code 200
