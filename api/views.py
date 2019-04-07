from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Mood, Action, MoodLog

class GetMoods(APIView):

	def get(self, request):

		moods = Mood.objects.all().values('id', 'title', 'emoji')
		print(moods)
		moods = list(moods)
		print(moods)

		data = json.dumps(moods)

		return Response(data)