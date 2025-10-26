from rest_framework import serializers
from .models import Subject, Question, ExamSession

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'code', 'description']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id', 'subject', 'question_text',
            'option1', 'option2', 'option3', 'option4',
            'marks', 'difficulty'
        ]

class ExamSessionSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='subject.name', read_only=True)
    
    class Meta:
        model = ExamSession
        fields = [
            'id', 'student_name', 'subject', 'subject_name',
            'score', 'total_questions', 'start_time', 'end_time'
        ]