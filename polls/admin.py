from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "pub_date", "was_published_recently"]
    # fieldsets = [
    #     (None, {"fields": ["question_text"]}),
    #     ("Date Information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    # ]
    # inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)
