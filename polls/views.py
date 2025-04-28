from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Assalam-O-Alaikum World, From Polls App.")

def detail(request, question_id):
    return HttpResponse("You are looking at Question: %s." % question_id)

def result(request, question_id):
    response = "You are looking at the result of Question: %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting at Question: %s." % question_id)
