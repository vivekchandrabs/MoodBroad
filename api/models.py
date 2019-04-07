from django.db import models

# Create your models here.
class Mood(models.Model):

	title = models.CharField(max_length=30)
	emoji = models.CharField(max_length=10)

	def __str__ (self):

		return f"{self.title} {self.emoji}"

class Action(models.Model):

	title = models.CharField(max_length=30)
	emoji = models.CharField(max_length=10)

	def __str__ (self):

		return f"{self.title} {self.emoji}"

class MoodLog(models.Model):

	mood = models.ForeignKey(Mood, null = True, on_delete = models.SET_NULL)
	action = models.ForeignKey(Action, null=True, on_delete=models.SET_NULL)
	note = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.mood} - {self.action}"