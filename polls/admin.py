from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice

# admin.site.register(Choice)
# admin.site.register(Question)

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date Information", {"fields": ["pub_date"]}),
    ]
admin.site.register(Question, QuestionAdmin)
