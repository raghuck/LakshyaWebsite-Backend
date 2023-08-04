from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from common.models import company, skills
from internships.models import internship
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError


# def internship_list_view(request):
#     internships = Internship.objects.all()
#     serializer = InternshipSerializer(internships, many=True)
#     return JsonResponse(serializer.data, safe=False)

# def internship_detail_view(request):
#     internship_id = request.data.get('internship_id')
#     internship = get_object_or_404(Internship, internship_id=internship_id)
#     serializer = InternshipSerializer(internship)
#     return JsonResponse(serializer.data)

# @login_required
# def add_internship_view(request):
#     serializer = InternshipSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return JsonResponse(serializer.data, status=201)
#     return JsonResponse(serializer.errors, status=400)


def internship_list_view(request):
    interships = internship.objects.all()
    intern_data = []
    for intern_obj in interships:
        intern_data.append({
            'internship_id': intern_obj.internship_id,
            'description': intern_obj.description,
            'apply_before': intern_obj.apply_before,
            'company': intern_obj.company.name
        })
    return JsonResponse(intern_data, safe=False)

def internship_detail_view(request, internship_id):
    intern_obj = get_object_or_404(internship, internship_id=internship_id)
    intern_data = {
        'internship_id': intern_obj.internship_id,
        'description': intern_obj.description,
        'apply_before': intern_obj.apply_before,
        'company': intern_obj.company.name,
        'startDate': intern_obj.startDate,
        'duration': intern_obj.duration,
        'stipend': intern_obj.stipend,
        'aboutCompany': intern_obj.aboutCompany,
        'aboutInternship': intern_obj.aboutInternship,
        'whoCanApply': intern_obj.whoCanApply,
        'postedTime': intern_obj.postedTime,
        'numberofhiring': intern_obj.numberofhiring,
        'hiringsince': intern_obj.hiringsince,
        'numberofopportunities': intern_obj.numberofopportunities,
        'perks': intern_obj.perks,
        'numberofopenings': intern_obj.numberofopenings,
    }
    return JsonResponse(intern_data)


def add_internship_view(request):
    if request.method == 'POST':
        data = request.POST
        skill_name = data.get('skill_name')
        try:
            skill_obj = skills.get(name = skill_name)

        except:
            skill_obj = skills(name = skill_name)
            skill_obj.save()

        internship_obj = internship(skill_id = skill_obj.id)
        internship_obj.save()
        return JsonResponse({'message': 'Internship added successfully'}, status=201)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)

# def internship_add_new(req):
#     data = req.POST
#     skill_name = data.get('skill_name')
#     skill_obj = skills.objects.create(name = skill_name)