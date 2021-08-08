#from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
#from django.http import HttpResponse
#from django.template import loader
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date') #[:5]
    #template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # We have commented this line because we moved the list comprehension to html page
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #return HttpResponse("You are looking at question %s." % question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
