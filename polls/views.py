from django.http import HttpResponse, Http404
from polls.models import Question
# Create your views here.
def index(request):
    return HttpResponse("Assalam-O-Alaikum World, From Polls App.")

def detail(request, question_id):
    question_list = Question.objects.order_by("pub_data")[:5]
    output = ", ".join(q.question_text for q in question_list)
    return HttpResponse(output)
    # return HttpResponse("You are looking at Question: %s." % question_id)

def result(request, question_id):
    response = "You are looking at the result of Question: %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting at Question: %s." % question_id)
