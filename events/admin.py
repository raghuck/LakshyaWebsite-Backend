
from django.contrib import admin
from .models import *

# Register the models in the admin interface
admin.site.register(Event)
admin.site.register(mentor)
admin.site.register(company)
