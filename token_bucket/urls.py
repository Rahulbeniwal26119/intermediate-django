from django.urls import path

from .views import TokenBucketView

urlpatterns = [
    path("bucket_stats/", TokenBucketView.as_view()),
]

