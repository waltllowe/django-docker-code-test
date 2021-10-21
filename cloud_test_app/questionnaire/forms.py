from django import forms
from django.forms import ModelForm
from .models import FilledQuestionnaire

class QuestionnaireForm(ModelForm):
	class Meta:
		model = FilledQuestionnaire
		fields = ['month', 'day']
