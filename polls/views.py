from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from polls.models import Question,Choice
from django.core.urlresolvers import reverse

# Create your views here.

#poll index Question.objects.order_by('-pub_date')[:5]
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list' : latest_question_list
    }
    #response = '<br>'.join([q.question_text for q in latest_question_list])

    #template = loader.get_template('polls/index.html')
    #return HttpResponse(template.render(context,request))
    return render(request, 'polls/index.html', context)

#question details
def detail(request,question_id):
    # try:
    #     question = Question.objects.get(pk = question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    #return HttpResponse("You're looking at question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

#the results of question
def results(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question' : question})
    #return HttpResponse("You're looking at the results of question %s." % question_id)

#voting on question
def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_message' : "You didn't select a choice",
        })
    else:
        select_choice.votes += 1
        select_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
    #return HttpResponse("You're voting on question %s." % question_id)

#test
def showName(request):
    param1 = request.GET.get('p1')
    param2 = request.GET.get('p2')
    return HttpResponse("the param1 is %s and the param2 is %s" % (param1,param2))

