from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'subjects', views.SubjectViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'exam-sessions', views.ExamSessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]