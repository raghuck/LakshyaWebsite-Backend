from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('events/',getEventListView,name='eventList'),
    path('details',eventDetailView, name='eventDetail'),
    path('add',addEventView,name='addEvent'),
    path('rsvp',registerEvent,name='regEvent')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)