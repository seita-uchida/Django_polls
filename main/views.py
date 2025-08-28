from django.shortcuts import render


def index(request):  # ビュー関数を定義
    return render(request, "main/index.html")