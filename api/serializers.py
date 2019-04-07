from rest_framework import serializers
from api.models import MoodLog

class MoodLogSerializer(serializers.ModelSerializer):

	class Meta:

		model = MoodLog
		fields = '__all__'
		depth = 1