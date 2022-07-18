import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_kanalservice.settings')

app = Celery('test_kanalservice')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.save_gdoc_data',
        'schedule': 30.0
    },
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
