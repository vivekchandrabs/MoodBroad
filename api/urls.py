from django.urls import path, include
from api.views import *

from rest_framework.routers import DefaultRouter
from api.viewsets import *

router = DefaultRouter()
router.register(r'moods',MoodViewSet)
router.register(r'actions',ActionViewSet)
router.register(r'logs',MoodLogViewSet)

# urlpatterns = [
# path('moods/', GetAllMoods.as_view()),
# path('actions/',GetALlAction.as_view()),
# path('logs/',GetALlMoodLogs.as_view()),
# ]

urlpatterns = [
	path('',include(router.urls))
]


	

