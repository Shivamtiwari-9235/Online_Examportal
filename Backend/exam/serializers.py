from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'option_1', 'option_2', 'option_3', 'option_4']  # Excluding correct_answer for security