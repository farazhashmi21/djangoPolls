from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice

# admin.site.register(Choice)
# admin.site.register(Question)

class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date Information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = ChoiceInLine

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
