import datetime
import time

from celery import Celery


app = Celery("tasks", broker="pyamqp://localhost//")


@app.task
def add(x, y):
    time.sleep(3)
    with open("log.txt", "a") as w:
        w.write(datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S\n"))
    return x + y
