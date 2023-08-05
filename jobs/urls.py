from django.urls import path
from jobs.views import jobs_list_view, jobs_detail_view, add_jobs_view,apply_job_view

urlpatterns = [
    path('list/', jobs_list_view),
    path('details/', jobs_detail_view),
    path('add/', add_jobs_view),
    path('apply/',apply_job_view)
]