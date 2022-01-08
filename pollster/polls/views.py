
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Question, Choice
from django.http import JsonResponse

# Get questions and display them
def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'lastest_question_list': lastest_question_list}
    return render(request, 'polls/index.html', context)

# Show specific question and choices
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)

    except Question.DoesNotExist:
        raise Http404("Question doesnot exit")

    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/results.html', { 'question': question })

def vote(request, question_id):
    print(request.POST)
    print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the question votting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

def resultsData(request, obj):
    votedata = []

    question = Question.objects.get(id=obj)
    votes = question.choice_set.all()

    for i in votes:
        votedata.append({i.choice_text: i.votes})
    
    print(votedata)
    return JsonResponse(votedata, safe=False)
