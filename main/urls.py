from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),  # name = "index" を追加
    path("results/", views.results, name="results"),  # この行を追加
]