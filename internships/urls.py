from django.urls import path
from internships.views import internship_list_view, internship_detail_view, add_internship_view

urlpatterns = [
    path('list/', internship_list_view),
    path('details/', internship_detail_view),
    path('add/', add_internship_view)
]
