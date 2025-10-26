from django.contrib import admin
from .models import Subject, Question, ExamSession

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'created_at')
    search_fields = ('name', 'code')
    list_filter = ('created_at',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'subject', 'difficulty', 'marks', 'is_active')
    list_filter = ('subject', 'difficulty', 'is_active', 'created_at')
    search_fields = ('question_text', 'subject__name')
    list_editable = ('marks', 'is_active')
    fieldsets = (
        ('Question Details', {
            'fields': ('subject', 'question_text', 'explanation', 'marks', 'difficulty')
        }),
        ('Options', {
            'fields': ('option1', 'option2', 'option3', 'option4', 'correct_answer')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )

@admin.register(ExamSession)
class ExamSessionAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'subject', 'score', 'total_questions', 'start_time', 'end_time')
    list_filter = ('subject', 'start_time')
    search_fields = ('student_name',)