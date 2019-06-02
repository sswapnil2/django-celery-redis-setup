from celery import Celery
import os 
from time import sleep

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')

app = Celery('django_celery')


app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task
def fib(n):
    sleep(2)  # simulate slow computation
    if n < 0:
        return []
    elif n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        results = fib(n - 1)
        results.append(results[-1] + results[-2])
        return results
