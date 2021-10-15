from django.db import models

class FilledQuestionnaire(models.Model):
	MONTHS = [
		('JAN', 'January'),
		('FEB', 'February'),
		('MAR', 'March'),
		('APR', 'April'),
		('MAY', 'May'),
		('JUN', 'June'),
		('JUL', 'July'),
		('AUG', 'August'),
		('SEP', 'September'),
		('OCT', 'October'),
		('NOV', 'November'),
		('DEC', 'December')
	]
	DAYS = [
		('MON', 'Monday'),
		('TUE', 'Tuesday'),
		('WED', 'Wednesday'),
		('THU', 'Thursday'),
		('FRI', 'Friday'),
		('SAT', 'Saturday'),
		('SUN', 'Sunday')
	]
	month = models.CharField(max_length=3, choices=MONTHS)
	day = models.CharField(max_length=3, choices=DAYS)