from django.urls import path 
from api.views import *

urlpatterns = [
path('moods/', GetAllMoods.as_view()),
path('actions/',GetALlAction.as_view()),
path('logs/',GetALlMoodLogs.as_view()),
]


	

