from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=500)
    option_1 = models.CharField(max_length=200)
    option_2 = models.CharField(max_length=200)
    option_3 = models.CharField(max_length=200)
    option_4 = models.CharField(max_length=200)
    correct_answer = models.IntegerField()  # 1, 2, 3, or 4
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text
