
from django.contrib import admin
from .models import Event,RSVP

# Register the models in the admin interface
admin.site.register(Event)
admin.site.register(RSVP)
