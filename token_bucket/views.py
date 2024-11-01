from rest_framework.decorators import api_view
from rest_framework.views import APIView
from token_bucket.utils import TokenBucketThrottle
from rest_framework.response import Response

class TokenBucketView(APIView):
    throttle_classes = (TokenBucketThrottle(60, 1),)

    def get(self, request):
        return Response(
            request.throttle_stats
        )