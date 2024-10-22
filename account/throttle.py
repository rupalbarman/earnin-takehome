from django.core.cache import cache
from rest_framework.throttling import BaseThrottle

# 10 requests / min
MAX_REQUESTS = 10
TIMEOUT_SEC = 60


class AccountMetricThrottle(BaseThrottle):
    def allow_request(self, request, view):
        account_id = view.kwargs.get("pk")

        if account_id is None:
            return True

        key = f"throttle-account-{account_id}"

        current_cache_value = cache.get(key=key)

        if current_cache_value is None:
            cache.set(key=key, value=MAX_REQUESTS, timeout=TIMEOUT_SEC)
            current_cache_value = MAX_REQUESTS

        if current_cache_value > 0:
            cache.decr(key=key, delta=1)
            return True

        return False
