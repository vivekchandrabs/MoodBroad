from django.contrib import admin
from api.models import Mood, Action, MoodLog
# Register your models here.

admin.site.register([Mood, Action, MoodLog])