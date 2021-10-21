from django.db import models

class FilledQuestionnaire(models.Model):
	MONTHS = [
		('January', 'January'),
		('February', 'February'),
		('March', 'March'),
		('April', 'April'),
		('May', 'May'),
		('June', 'June'),
		('July', 'July'),
		('August', 'August'),
		('September', 'September'),
		('October', 'October'),
		('November', 'November'),
		('December', 'December')
	]
	DAYS = [
		('Monday', 'Monday'),
		('Tuesday', 'Tuesday'),
		('Wednesday', 'Wednesday'),
		('Thursday', 'Thursday'),
		('Friday', 'Friday'),
		('Saturday', 'Saturday'),
		('Sunday', 'Sunday')
	]
	month = models.CharField("My favourite month.", max_length=9, default='January', choices=MONTHS)
	day = models.CharField("My favourite day of the week.", max_length=9, default='MON', choices=DAYS)