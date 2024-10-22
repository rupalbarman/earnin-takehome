import time

from earnin.celery import app


@app.task
def fetch_metrics_task():
    # Fetch job for all accounts
    # Triggered using scheduler at a specific time
    time.sleep(2)
    return 1
