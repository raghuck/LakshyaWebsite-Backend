from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Internship
from .serializers import InternshipSerializer
from rest_framework.decorators import api_view


def internship_list_view(request):
    internships = Internship.objects.all()
    serializer = InternshipSerializer(internships, many=True)
    return JsonResponse(serializer.data, safe=False)

def internship_detail_view(request):
    internship_id = request.data.get('internship_id')
    internship = get_object_or_404(Internship, internship_id=internship_id)
    serializer = InternshipSerializer(internship)
    return JsonResponse(serializer.data)

@login_required
def add_internship_view(request):
    serializer = InternshipSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
