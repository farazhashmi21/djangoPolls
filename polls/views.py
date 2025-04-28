from django.http import HttpResponse
# from django.template import loader
from polls.models import Question
from django.shortcuts import render

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    # template = loader.get_template("polls/index.html")
    return render(request, "polls/index.html", context)
    # return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You are looking at Question: %s." % question_id)

def result(request, question_id):
    response = "You are looking at the result of Question: %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting at Question: %s." % question_id)
