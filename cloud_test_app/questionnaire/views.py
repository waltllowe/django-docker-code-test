from django.shortcuts import redirect, render
from .forms import QuestionnaireForm
from .models import FilledQuestionnaire
from django.db.models import Count
from django.http import HttpResponse
from collections import Counter


def index(request):
    # TODO: make this a real number:
    num_answers = FilledQuestionnaire.objects.count()
    context = {
        "title": "Basic Questions!",
        "num_answers": num_answers,
    }
    return render(request, "questionnaire/index.html", context)

def questionnaire(request):
    
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = QuestionnaireForm()

    context = {
        "title": "Basic Questions!",
        "form": form,
    }
    return render(request, "questionnaire/questionnaire.html", context)

def results(request):
    num_answers = FilledQuestionnaire.objects.count()
    months = FilledQuestionnaire.objects.order_by('month').values('month').annotate(num_picked = Count('month'), percent = Count('month')*100/num_answers).order_by('-num_picked')
    days = FilledQuestionnaire.objects.order_by('day').values('day').annotate(num_picked = Count('day'), percent = Count('day')*100/num_answers).order_by('-num_picked')
    daysandmonths = FilledQuestionnaire.objects.values('month', 'day')
    daysformonths = list()
    for month in months:
        daysinmonth = daysandmonths.filter(month = month['month'])
        day_counts = Counter(d['day'] for d in daysinmonth)
        most_common = {'day': day_counts.most_common(1)[0][0]}
        most_common['month'] = month['month']
        daysformonths.append(most_common)


    context = {
        "title": "Basic Questions!",
        "months": months,
        "days": days,
        "daysformonths": daysformonths,
    }
    return render(request, "questionnaire/results.html", context)