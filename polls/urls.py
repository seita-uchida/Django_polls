from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # /polls/ という URL がリクエストされたら polls/urls.py を参照するよう指定
    path("polls/", include("main.urls")),
]