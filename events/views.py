from django.http import JsonResponse
import common.models as commonModels
from .models import *
import json
from lakshya.settings import config

def getEventListView(req):
    eventList = []
    events = Event.objects.all()
    for event in events:
        event_data={
            'id': event.event_id,
            'title': event.title,
            'image': config["NGROK"]+event.image.url,
            'location': event.location,
            'category': event.category,
            'date': event.date.strftime('%Y-%m-%d')
        }
        eventList.append(event_data)
    return JsonResponse(eventList, safe= False)


def eventDetailView(req):
    eventId = json.loads(req.body.decode('utf-8'))['eventId']
    event = Event.objects.get(event_id= eventId)
    try: 
        EventDetails = {
            "event": {
                "title": event.title,
                "details": {
                    "date": event.date.strftime('%Y-%m-%d'),
                    "location": event.location,
                    "category":event.category,
                    "time": event.time.strftime('%I:%M %p'),
                    "image": config['NGROK']+event.image.url, 
                }
            },
            "eventInfo": {
                "title": event.title,
                "details": {
                    "date": event.date.strftime('%Y-%m-%d'),
                    "time": event.time.strftime('%I:%M %p'),
                    "eventType": event.category,
                    "officialLinks":event.join_link,
                    "venue": event.venue,                        
                },
            },
            "speakerDetails": {
                "name": event.speakerName,
                "details": {
                    "description": event.speakerDescription,
                    "image": config['NGROK']+event.speakerImage.url,
                },
            },
            "organizerDetails": {
                "name": event.company.name,
                "details": {
                    "description": event.company.description,
                    "image" : config['NGROK']+event.company.logo.url
                }
            }
        }
        return JsonResponse(EventDetails,status=201)
    except:
        return JsonResponse({"message:FAILURE"},status=500)
   
  
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
    image = event_data.get('image_path')

    #get or create the mentor and company objects
    mentor = commonModels.mentor.objects.get(name = mentor_name)
    company = commonModels.company.objects.get(name = company_name)

    #creating event object
    event = Event(
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
    event.save()
    return JsonResponse({"message":"SUCCESS"}, status = 201)


def registerEvent(req):
    try:
        candidate_data = json.loads(req.body)
        candidate_email = candidate_data.get('email')
        event_id = candidate_data.get('event_id')

        try:
            candidate = commonModels.Candidate.objects.get(email=candidate_email)
        except commonModels.Candidate.DoesNotExist:
            return JsonResponse({'message': 'Candidate with this email does not exist.'}, status=400)

        try:
            event = Event.objects.get(event_id=event_id)
        except Event.DoesNotExist:
            return JsonResponse({'message': 'Event with this ID does not exist.'}, status=400)

        rsvp = RSVP(event=event, candidate=candidate)
        rsvp.save()

        return JsonResponse({'message': 'Candidate successfully registered for the event.'}, status=201)

    except Exception as e:
        return JsonResponse({'message': str(e)}, status=500)