from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Question, Choice
from django.utils import timezone
from django.db import models
from django.http import HttpResponse

# Create your views here.

def index(request):
	question_list = get_list_or_404(Question.objects.filter(pub_date__lte=timezone.now()).filter(votes_count__gte=2))
	paginator = Paginator(question_list, 3)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	return render(request, 'polls_app/index.html', {'page_obj': page_obj })

def detail(request, pk):
	question = get_object_or_404(Question.objects.filter(pub_date__lte=timezone.now()).filter(votes_count__gte=2), pk=pk)

	return render(request, 'polls_app/detail.html', {'question': question})

def result(request, pk):
	question = get_object_or_404(Question.objects.filter(pub_date__lte=timezone.now()).filter(votes_count__gte=2), pk=pk)

	return render(request, 'polls_app/result.html', {'question': question})

def vote(request, pk):
	question = get_object_or_404(Question.objects.filter(pub_date__lte=timezone.now()).filter(votes_count__gte=2), pk=pk)
	try:
		choice = question.choice_set.get(pk=request.POST['choice'])
	except(KeyError, Choice.DoesNotExist):
		context = {
			'question': question,
			'error_msg': "Please select a choice.",
		}

		return render(request, 'polls_app/detail.html', context=context)

	else:
		Choice.objects.filter(pk=choice.id).update(votes=models.F('votes') + 1)
		return redirect('polls_app:result', pk=question.id)
		# return HttpResponse('<h2>Thanks for taking the poll.</h2>')