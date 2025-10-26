from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Question
from .serializers import QuestionSerializer

def home(request):
    return JsonResponse({'message': 'Welcome to Mahakal Backend API'})

@api_view(['GET'])
def get_questions(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def check_answer(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
        user_answer = request.data.get('answer')
        
        if user_answer is None:
            return Response({'error': 'Answer not provided'}, status=400)
            
        is_correct = user_answer == question.correct_answer
        return Response({'correct': is_correct})
    except Question.DoesNotExist:
        return Response({'error': 'Question not found'}, status=404)
