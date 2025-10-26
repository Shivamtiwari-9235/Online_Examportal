from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL
    path('questions/', views.get_questions, name='get_questions'),
    path('check-answer/<int:question_id>/', views.check_answer, name='check_answer'),
]
