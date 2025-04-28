from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Question
from django.template import loader

# Create your views here.
def index(request):
    question_list = Question.objects.order_by("pub_date")[:5]
    output = ", ".join(q.question_text for q in question_list)
    context = {"latest_question_list": question_list}
    return render(request, "polls/index.html", context)
    # return HttpResponse(template.render(context, request))
    # return HttpResponse(output)
    # return HttpResponse("Assalam-O-Alaikum World, From Polls App.")

def detail(request, question_id):
    return HttpResponse("You are looking at Question: %s." % question_id)

def result(request, question_id):
    response = "You are looking at the result of Question: %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting at Question: %s." % question_id)
