from django.shortcuts import redirect, render
from .forms import QuestionnaireForm
from .models import FilledQuestionnaire
from django.db.models import Count
from django.http import HttpResponse


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
    months = FilledQuestionnaire.objects.values('month').annotate(num_picked = Count('month'), percent = Count('month')*100/num_answers).order_by('-num_picked')
    context = {
        "title": "Basic Questions!",
        "months": months,
    }
    return render(request, "questionnaire/results.html", context)