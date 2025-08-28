from django.shortcuts import render


def index(request):
    question_list = [
        "プログラミングは好きですか？",
        "数学は好きですか？",
        "国語は好きですか？",
    ]
    context = {
        "question_list": question_list,  # list 型を渡す
        "is_polled": True,
        "polled_msg": "投票ありがとうございました。",
        "not_polled_msg": "投票をお願いします。",
    }
    return render(request, "main/index.html", context)


def results(request):
    question_dict = {
        "プログラミングは好きですか？": True,
        "数学は好きですか？": True,
        "国語は好きですか？": True,
    }
    context = {
        "question_dict": question_dict,  # dict 型を渡す
    }
    return render(request, "main/results.html", context)