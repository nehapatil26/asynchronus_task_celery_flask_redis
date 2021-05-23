from flask import Flask,jsonify
from celery import Celery
from celery.schedules import crontab
import random # for time shedule

app = Flask(__name__)
#app.secret_key = random.getrandbits(128) # generate file name

app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery_beat_schedule = {
    "time_scheduler":{
        "task":"app.scrap",
        "schedule": 1.0
    }
}

celery = Celery(app.name,broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(
    result_backend = app.config['CELERY_BROKER_URL'],
    beat_schedule = celery_beat_schedule
    )

@app.route('/')
def hello_world():

    scrap.delay()

    message = {
        'message': 'hello,world'
    }

    resp = jsonify(message)
    return resp



@celery.task()
def scrap():
    print(random.randint(10000,99999))