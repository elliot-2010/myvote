from django.urls import path
from . import views


app_name = "vote"

urlpatterns = [
    path('', views.index, name="index"),
    path('submit/', views.submit_vote, name="submit"),
    path('stats/', views.stats, name="stats"),
    path("api/stats-data/", views.stats_data, name="stats-data")
]