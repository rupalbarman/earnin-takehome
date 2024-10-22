import time
from random import randrange

def call_api(metrics: list[str]) -> list[dict]:
    time.sleep(1)
    metric_data = []
    for m in metrics:
        metric_data.append({
            "id": m,
            "value": randrange(10),
        })
    return metric_data
