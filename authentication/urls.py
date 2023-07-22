from django.urls import path 
from . import views
from django.urls import re_path

urlpatterns = [
    path('login/',views.login_api),
    path('signup/',views.signup_api),
    path('logout/',views.logout_api),
    path('google/',views.google_auth),
]