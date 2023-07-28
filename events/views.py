from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializer import EventSerializer
from rest_framework.decorators import api_view
import json


@api_view(['GET'])
@csrf_exempt
def getEventListView(req):
    eventList = []
    events = Event.objects.all()
    for event in events:
        event_data={
            'event_id': event.event_id,
            'title': event.title,
            'image': event.image.url,
            'location': event.location,
            'category': event.category,
            'description': event.description,
            'date': event.date.strftime('%Y-%m-%d'),
            'time': event.time.strftime('%H:%M:%S'),
            'link': event.join_link,
            'mentor': event.mentor.name,
            'company': event.company.name,
        }
        eventList.append(event_data)

    return JsonResponse(eventList, safe= False)



@api_view(['POST'])
@csrf_exempt
def eventDetailView(req):
    eventId = req.data.get('event_id')
    event = get_object_or_404(Event,event_id= eventId)


    try: 
        req_object = req.body.decode('utf-8')
        req = json.loads(req_object)
        image_url = req_object.image.url

        event_detail = {
        'event_id': event.event_id,
        'title': event.title,
        'description': event.description,
        'date': event.date.strftime('%Y-%m-%d'),
        'time': event.time.strftime('%H:%M:%S'),
        'link': event.join_link,
        'image': image_url,
        'category': event.category,
        'location': event.location
        }
        return JsonResponse(event_detail)


    except:
        print('error')
   
  

@api_view(['POST'])
@csrf_exempt
def addEventView(req):
    event_data = req.data

    event_id= event_data.get('event_id')
    title = event_data.get("title")
    description = event_data.get('description')
    location = event_data.get('location')
    category = event_data.get('category')
    date = event_data.get('date')
    time = event_data.get('time')
    join_link = event_data.get('join_link')
    mentor_name = event_data.get('mentor')
    company_name = event_data.get('company')

    image =event_data.get('image_path')

    #validate data
    if not all([event_id,title,description,category,location,date,time,join_link,image,mentor_name,company_name]):
        return JsonResponse({'error ':'Incomplete data provided.' },status = 400 )
    
    #get or create the mentor and company objects
    mentor, _ = mentor.objects.get_or_create(name = mentor_name)
    company, _ = company.objects.get_or_create(name = company_name)

    #creating event object
    event = Event.objects.create(
        event_id=event_id,
        title = title,
        description=description,
        location = location,
        category = category,
        image= image,
        date=date,
        time=time,
        join_link=join_link,
        mentor=mentor,
        company=company,
    )

    # Returning created event
    event_data = {
    'event_id': event.event_id,
    'title': event.title,
    'description': event.description,
    'location': event.location,
    'category': event.category,
    'image': event.image.url,
    'date': event.date.strftime('%Y-%m-%d'),
    'time': event.time.strftime('%H:%M:%S'),
    'join_link': event.join_link,
    'mentor': event.mentor.name,
    'company': event.company.name,
    }

    return JsonResponse(event_data, status = 201)