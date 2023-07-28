from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('events/',getEventListView,name='eventList'),
    path('event/detail',eventDetailView, name='eventDetail'),
    path('event/add',addEventView,name='addEvent')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)