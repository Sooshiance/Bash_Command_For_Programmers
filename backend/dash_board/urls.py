from django.urls import path

from .views import (
    CreatedProjectTimeLapse,
    CreatedPostOneDay,
    AdvancedSearchView,
)


app_name = "dash_board"

urlpatterns = [
    path("date/range/<str:start>/<str:end>/", CreatedProjectTimeLapse.as_view()),
    path("one/day/<str:day>/", CreatedPostOneDay.as_view()),
    path("advanced-search/", AdvancedSearchView.as_view()),
]
