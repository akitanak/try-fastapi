from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def index():
    return [
        {"method": "POST", "path": "/tasks", "description": "create new task"},
        {"method": "GET", "path": "/tasks", "description": "list tasks"},
        {"method": "GET", "path": "/tasks/{id}", "description": "get task by id"},
        {"method": "PUT", "path": "/tasks/{id}/finish", "description": "finish task"},
        {"method": "DELETE", "path": "/tasks/{id}", "description": "remove task"}
    ]


@app.get("/healthz")
def healthz():
    return {"status": "I'm Healthy!"}


@app.get("/tasks/{task_id}")
def get(task_id):
    return 