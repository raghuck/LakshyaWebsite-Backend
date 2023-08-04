from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(company)
admin.site.register(candidate)
admin.site.register(mentor)
admin.site.register(tag)