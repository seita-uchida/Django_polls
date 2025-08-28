from django.urls import path  # path() 関数をインポート

from . import views  # ビュー関数を登録するため、views.py をインポート

urlpatterns = [
    path("", views.index, name="index"),
]