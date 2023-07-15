from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from lakshya.settings import config
# Create your views here.

# Create your views here.
def login_api(request):    
    if request.method=="GET":
        return HttpResponse("Testing")
    req_body = request.body.decode('utf-8')
    req = json.loads(req_body)
    username = req["id"]
    password = req["passwd"]
    user = authenticate(request, username=username, password=password)

    if user is not None:
        # Authentication successful
        login(request, user)        
        response =  JsonResponse({'message': 'SUCCESS'}, status=200)
        return response   
    else:
        # Authentication failed
        return JsonResponse({'message': 'FAILURE'}, status=401)
