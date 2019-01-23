from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from .models import Question


# writing a simple view
def index(request):
    """ Need this here """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    """ Need this here """
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', { 'question': question })

def results(request, question_id):
    """ Need this here """
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    """ Need this here """
    return HttpResponse("You're voting on question %s." % question_id)
