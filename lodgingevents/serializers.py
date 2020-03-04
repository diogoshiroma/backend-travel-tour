from rest_framework import serializers
from .models import LodgingEvent

class LodgingEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = LodgingEvent
        fields = ('pk', 'host_id', 'host_name', 'bedroom_id', 'bedroom_name', 'start_date', 'end_date')