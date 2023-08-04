from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from common.models import company, skills
from jobs.models import jobs
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError

# @api_view(['GET'])
# def job_list_view(request):
#     jobs = Job.objects.all()
#     serializer = JobSerializer(jobs, many=True)
#     return JsonResponse(serializer.data, safe=False)

# @api_view(['POST'])
# def job_detail_view(request):
#     job_id = request.data.get('job_id')
#     job = get_object_or_404(Job, id=job_id)
#     serializer = JobSerializer(job)
#     return JsonResponse(serializer.data)

# @api_view(['POST'])
# @csrf_exempt
# def add_job_view(request):
#     serializer = JobSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return JsonResponse(serializer.data, status=201)
#     return JsonResponse(serializer.errors, status=400)

def jobs_list_view(request):
    jobs = jobs.objects.all()
    job_data = []
    for job_obj in jobs:
        job_data.append({
            'job_id': job_obj.job_id,
            'description': job_obj.description,
            'apply_before': job_obj.apply_before,
            'company': job_obj.company.name
        })
    return JsonResponse(job_data, safe=False)

def jobs_detail_view(request, job_id):
    job_obj = get_object_or_404(jobs, job_id=job_id)
    job_data = {
        'job_id': job_obj.job_id,
        'description': job_obj.description,
        'apply_before': job_obj.apply_before,
        'company': job_obj.company.name,
        'startDate': job_obj.startDate,
        'duration': job_obj.duration,
        'stipend': job_obj.stipend,
        'aboutCompany': job_obj.aboutCompany,
        'aboutJob': job_obj.aboutJob,
        'whoCanApply': job_obj.whoCanApply,
        'postedTime': job_obj.postedTime,
        'numberofhiring': job_obj.numberofhiring,
        'hiringsince': job_obj.hiringsince,
        'numberofopportunities': job_obj.numberofopportunities,
        'perks': job_obj.perks,
        'numberofopenings': job_obj.numberofopenings,
    }
    return JsonResponse(job_data)


def add_jobs_view(request):
    if request.method == 'POST':
        data = request.POST
        skill_name = data.get('skill_name')
        try:
            skill_obj = skills.get(name = skill_name)

        except:
            skill_obj = skills(name = skill_name)
            skill_obj.save()

        job_obj = jobs(skill_id = skill_obj.id)
        job_obj.save()
        return JsonResponse({'message': 'Job added successfully'}, status=201)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)

