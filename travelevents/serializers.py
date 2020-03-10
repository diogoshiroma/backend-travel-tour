from rest_framework import serializers
from .models import TravelEvent

class TravelEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelEvent
        fields = ('pk', 'agency_id', 'agency_name', 'tour_id', 'tour_name', 'date')
        