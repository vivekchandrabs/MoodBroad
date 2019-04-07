from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Mood, Action, MoodLog

import json

from api.serializers import MoodLogSerializer

class GetAllMoods(APIView):

	def get(self, request):

		moods = Mood.objects.all().values('id', 'title', 'emoji')
		print(moods)
		moods = list(moods)
		print(moods)

		
		return Response(moods)

class GetALlAction(APIView):

	def get(self, request):


		actions = Action.objects.all().values('id', 'title', 'emoji')
		# print(moods)
		actions = list(actions)
		# print(moods)
	
		return Response(actions)


class GetALlMoodLogs(APIView):

		def get(self, request):


			# log = MoodLog.objects.all().values('id', 'mood','action','note','timestamp')
			# # print(moods)
			# actions = list(log)
			# # print(moods)

			querryset = MoodLog.objects.all()
			logs = MoodLogSerializer(querryset, many = True)
			return Response(logs.data)