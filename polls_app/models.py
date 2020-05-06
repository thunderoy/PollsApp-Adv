from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Question(models.Model):
	question_text = models.CharField('Question', max_length=300)
	pub_date = models.DateTimeField('Published On', default=timezone.now)
	votes_count = models.IntegerField('Votes Count', default=0)

	def __str__(self):
		return self.question_text

	def published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField("Choice", max_length=300)
	votes = models.IntegerField("Votes", default=0)

	def __str__(self):
		return self.choice_text

	# Update "votes_count" field in Question model whenever a Choice is created
	def save(self, *args, **kwargs):
		# print(self.pk)
		if not self.pk:
			Question.objects.filter(pk=self.question_id).update(votes_count=models.F('votes_count') + 1)
		super().save(*args, **kwargs)