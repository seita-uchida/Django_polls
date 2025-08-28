from django.shortcuts import render

from .models import Question


def index(request):
    all_question = Question.objects.all()
    context = {
        "all_question": all_question,
    }
    return render(request, "main/index.html", context)


def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    context = {
        "question": question,
    }
    return render(request, "main/detail.html", context)