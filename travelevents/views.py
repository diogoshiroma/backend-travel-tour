from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import TravelEvent
from .serializers import *
from django.shortcuts import render
# Create your views here.

@api_view(['GET', 'POST'])
def event_list(request):
    if request.method == 'GET':
        events = TravelEvent.objects.all()
        serializer = TravelEventSerializer(events, context ={'request': request}, many = True)

        return Response({
            'data': serializer.data
        })
    elif request.method == 'POST':
        serializer = TravelEventSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def event_detail(request, event_pk):
  #Retrieve, update or delete a event by id/pk.
    try:
        event = TravelEvent.objects.get(pk = event_pk)
    except TravelEvent.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TravelEventSerializer(event, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TravelEventSerializer(event, data = request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        