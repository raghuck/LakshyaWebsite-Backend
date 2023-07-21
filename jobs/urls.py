from django.urls import path
from jobs.views import job_list_view, job_detail_view, add_job_view

urlpatterns = [
    path('list/', job_list_view),
    path('details/', job_detail_view),
    path('add/', add_job_view)
]