from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)  # 質問の内容
    pub_date = models.DateTimeField("date published")  # 作成日時

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # related_name を追加
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text