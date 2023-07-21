from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Event
from .serializer import EventSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def getEventListView(req):
    events = Event.objects.all()
    serializer = EventSerializer(events,many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def eventDetailView(req):
    eventId = req.data.get('event_id')
    event = get_object_or_404(Event,event_id= eventId)
    serializer = EventSerializer(event)
    return JsonResponse(serializer.data)

@api_view(['POST'])
def addEventView(req):
    serializer = EventSerializer(data = req.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    else:
        return JsonResponse(serializer.errors, status=400)
