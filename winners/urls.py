from django.urls import path

from winners import views

urlpatterns = [
    path("select-winners", views.GetTopFiveWinners.as_view(), name='select-winners')
]