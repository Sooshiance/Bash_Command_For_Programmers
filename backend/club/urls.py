from django.urls import path

from .views import (
    StatisticAPIView,
    GalleryItemAPIView,
    ServiceAPIView,
    EventAPIView,
    FAQAPIView,
    SubscriberAPIView,
)


app_name = "club"

urlpatterns = [
    path("statistics/<str:psku>/", StatisticAPIView.as_view()),
    path("statistics/<str:sku>/", StatisticAPIView.as_view()),
    path("gallery/", GalleryItemAPIView.as_view()),
    path("gallery/<str:sku>/", GalleryItemAPIView.as_view()),
    path("service/", ServiceAPIView.as_view()),
    path("service/<str:sku>/", ServiceAPIView.as_view()),
    path("event/", EventAPIView.as_view()),
    path("event/<str:sku>/", EventAPIView.as_view()),
    path("faq/", FAQAPIView.as_view()),
    path("faq/<str:sku>/", FAQAPIView.as_view()),
    path("subscribe/", SubscriberAPIView.as_view()),
]
