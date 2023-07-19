from django.contrib import admin
from django.urls import path
from internships.views import internship_list_view, internship_detail_view, add_internship_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('internships/', internship_list_view, name='internship_list'),
    path('internships/detail/', internship_detail_view, name='internship_detail'),
    path('internships/add/', add_internship_view, name='add_internship'),
]
