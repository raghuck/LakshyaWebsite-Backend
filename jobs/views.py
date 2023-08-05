import json
from django.http import JsonResponse
from common.models import company,candidate
from jobs.models import Job,jobApplied
from lakshya.settings import config


def jobs_list_view(request):
    jobs = Job.objects.all()
    job_data = []
    for job_obj in jobs:
        job_data.append({
            'id': job_obj.id,
            'title':job_obj.title,
            'location':job_obj.location,
            'MinExperience':job_obj.MinExperience,
            "salary" : job_obj.salary,
            'company': job_obj.company.name,
            'type' : job_obj.type,
            "image":config['NGROK']+job_obj.company.logo.url
        })
    return JsonResponse({"jobs":job_data},status=201)

def jobs_detail_view(req):
    jobId = json.loads(req.body.decode('utf-8'))['jobId']
    job_obj = Job.objects.get(id=jobId)
    skillsList = list(job_obj.skills.split(","))
    skillsList = list(map(lambda x:x.strip(),skillsList))
    
    applicantList = list(job_obj.whoCanApply.split(","))
    applicantList = list(map(lambda x:x.strip(),applicantList))
    
    perksList = list(job_obj.perks.split(","))
    perksList = list(map(lambda x:x.strip(),perksList))
    
    job_data = {
        'id': job_obj.id,
        'company': job_obj.company.name,
        'description': job_obj.description,
        'aboutCompany': job_obj.company.description,
        'salary': job_obj.salary,
        'startDate': job_obj.startDate.strftime('%Y-%m-%d'),
        'whoCanApply': applicantList,
        'applyBefore': job_obj.apply_before.strftime('%Y-%m-%d'),
        'perks': perksList,
        'openings': job_obj.openings,
        'skills':skillsList
    }
    return JsonResponse(job_data,status=201)

def apply_job_view(req):
    if not req.user.is_authenticated:
        response =  JsonResponse({'message': 'REDIRECT'}, status=302)
        return response
    jobId = json.loads(req.body.decode('utf-8'))['jobId']
    newApplication = jobApplied(
        job = Job.objects.get(id=jobId),
        candidate = candidate.objects.get(email=req.user)
    )
    newApplication.save()
    return JsonResponse({"message":"SUCCESS"},status=201)

def add_jobs_view(req):
    if not req.user.is_authenticated:
        response =  JsonResponse({'message': 'REDIRECT'}, status=302)
        return response
    if req.method == 'POST':
        data = json.loads(req.body.decode('utf-8'))
        print(data)
        newJob = Job(
            title = data['jobTitle'],
            location = data['location'],
            description = data['description'],
            salary =data['salary'],
            apply_before = data['applyBefore'],
            MinExperience = data['MinExperience'],
            type = data['type'],
            company = company.objects.get(email=req.user),
            startDate = data['startdate'],
            whoCanApply = ", ".join(list(map(lambda x:x['content'],data['whocanApply']))),
            skills = ", ".join(list(map(lambda x:x['content'],data['skills']))),
            openings = data['numberOfOpenings'],
            perks = data['perks'],
        )
    newJob.save()
    return JsonResponse({"message":"SUCCESS"},status=201)