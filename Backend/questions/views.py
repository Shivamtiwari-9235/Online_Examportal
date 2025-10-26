from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Subject, Question, ExamSession
from .serializers import SubjectSerializer, QuestionSerializer, ExamSessionSerializer

class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def questions(self, request, pk=None):
        subject = self.get_object()
        questions = Question.objects.filter(subject=subject, is_active=True)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.filter(is_active=True)
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        subject_id = self.request.query_params.get('subject', None)
        difficulty = self.request.query_params.get('difficulty', None)
        
        if subject_id:
            queryset = queryset.filter(subject_id=subject_id)
        if difficulty:
            queryset = queryset.filter(difficulty=difficulty)
            
        return queryset

class ExamSessionViewSet(viewsets.ModelViewSet):
    queryset = ExamSession.objects.all()
    serializer_class = ExamSessionSerializer
    
    @action(detail=False, methods=['post'])
    def start_exam(self, request):
        subject_id = request.data.get('subject')
        student_name = request.data.get('student_name')
        
        subject = get_object_or_404(Subject, id=subject_id)
        total_questions = Question.objects.filter(subject=subject, is_active=True).count()
        
        session = ExamSession.objects.create(
            student_name=student_name,
            subject=subject,
            total_questions=total_questions
        )
        
        return Response(ExamSessionSerializer(session).data)