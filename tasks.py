from celery import Celery

app = Celery('tasks', backend='db+sqlite:///db.sqlite3', broker='redis://localhost')

@app.task
def add(x, y):
    return x + y