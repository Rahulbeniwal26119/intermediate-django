from rest_framework.throttling import BaseThrottle
import time

from django.core.cache import cache

class TokenBucket:

    def __init__(self, user_id, capacity, refill_rate):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.user_id = user_id
        self.token_key = f"token_bucket_for_user_{user_id}"
        self.timestamp_key = f"token_bucket_timestamp_for_user_{user_id}"
    
    def _refill_tokens(self):
        # Will refill and return the current number of tokens in the bucket
        last_refill = cache.get(self.timestamp_key)
        if last_refill is None:
            last_refill = time.time()
            cache.set(self.timestamp_key, last_refill)
        else:
            remaining_tokens = cache.get(self.token_key) or 0
            elapsed_time = time.time() - last_refill
            new_tokens = min(self.capacity, remaining_tokens + int(elapsed_time * self.refill_rate))
            cache.set(self.token_key, new_tokens)
            cache.set(self.timestamp_key, time.time())
    
    def allow_request(self):
        self._refill_tokens()
        tokens = cache.get(self.token_key, 0)
        if tokens >= 1:
            cache.decr(self.token_key)
            return True
        return False
    
    def consume(self):
        return self.allow_request()
    
    @property
    def availiable_tokens(self):
        return cache.get(self.token_key, 0)
    
    @property
    def last_refill(self):
        return cache.get(self.timestamp_key, 0)
    
    @property
    def last_refill_before(self):
        return time.time() - self.last_refill
    
    def __str__(self):
        return f"TokenBucket for user {self.user_id} with {self.availiable_tokens} tokens, last refill was {self.last_refill_before} seconds ago"
    
    def token_details(self):
        return {
            "user_id": self.user_id,
            "availiable_tokens": self.availiable_tokens,
            "last_refill": self.last_refill,
            "last_refill_before": self.last_refill_before,
            "capacity": self.capacity
        }
    


class TokenBucketThrottle(BaseThrottle):

    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.refill_rate = refill_rate
    
    def allow_request(self, request, view):
        if request.user.is_authenticated:
            user_id = request.user.id
        else:
            user_id = self.get_ident(request)
        
        token_bucket = TokenBucket(user_id, self.capacity, self.refill_rate)
        request.throttle_stats = token_bucket.token_details()

        return token_bucket.consume()
    
    def __call__(self, *args, **kwargs):
        return self
