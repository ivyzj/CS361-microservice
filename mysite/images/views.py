from django.shortcuts import render
from django.http import HttpResponse

# from django.template import loader
from .models import Question

# Create your views here.

def index(request):
    
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # version 4 use shortcut render()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'images/index.html', context)

    # version 3
    # template = loader.get_template('images/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))
    # version 2
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # version 1
    # return HttpResponse("Hello, world. You're at the images index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)