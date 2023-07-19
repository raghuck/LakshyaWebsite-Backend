from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Job
from .serializers import JobSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def job_list_view(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def job_detail_view(request):
    job_id = request.data.get('job_id')
    job = get_object_or_404(Job, id=job_id)
    serializer = JobSerializer(job)
    return JsonResponse(serializer.data)

@api_view(['POST'])
@csrf_exempt
def add_job_view(request):
    serializer = JobSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
