from django.http import JsonResponse
from common import models
from .models import *
import json

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


def eventDetailView(req):
    eventId = req.data.get('event_id')
    event = Event.objects.get(event_id= eventId)
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
    mentor = models.mentor.objects.get(name = mentor_name)
    company = models.company.objects.get(name = company_name)

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
            candidate = Candidate.objects.get(email=candidate_email)
        except Candidate.DoesNotExist:
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

    
