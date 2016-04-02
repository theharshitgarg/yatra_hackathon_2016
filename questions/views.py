from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template import loader
from django.http import Http404
from django.shortcuts import render
import pygal
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
	return HttpResponse("This is home page")

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

def index(request):
    #return HttpResponse("Hello")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('questions/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'questions/detail.html', {'question': question})

def about_us(request):
	return render(request, 'questions/About_us.html', {})

def line(request):
	line_chart = pygal.Line()
	line_chart.title = 'Students Evaluation Results'
	line_chart.x_labels = map(str, range(2002, 2013))
	line_chart.add('Q1', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
	line_chart.add('Q2',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
	line_chart.add('Q3',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
	line_chart.add('Q4',  [10, 20 ,10, 3, 33, 55, 23, 14, 42, 4,3,44,4,4,4,4])
	line_chart.render()
	return HttpResponse(line_chart.render())

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'questions/successful.html', {})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'questions/name.html', {'form': form})


def handle_submission(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        print request.POST
        print "-----"*3,request.POST.get('choice1')
        form = NameForm(request.POST)
        # check whether it's valid:
        return render(request, 'questions/successful.html', {})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'questions/name.html', {'form': form})