import time
from random import random, randrange

from utils import backoff

# 10% chance of failure
CHANCE_OF_FAILURE = 0.1


@backoff(retries=3)
def call_api(metrics: list[str]) -> list[dict]:
    if random() < CHANCE_OF_FAILURE:
        raise Exception("Simulated error")

    time.sleep(1)
    metric_data = []
    for m in metrics:
        metric_data.append(
            {
                "id": m,
                "value": randrange(10),
            }
        )

    return metric_data
