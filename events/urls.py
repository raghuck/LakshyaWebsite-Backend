from django.urls import path
from .views import *

urlpatterns=[
    path('events/',getEventListView,name='eventList'),
    path('event/detail',eventDetailView, name='eventDetail'),
    path('event/add',addEventView,name='addEvent')
]