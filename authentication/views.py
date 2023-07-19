from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
import json
# Create your views here.

# Create your views here.
def login_api(request):    
    req_body = request.body.decode('utf-8')
    req = json.loads(req_body)
    username = req["email"]
    password = req["password"]
    user = authenticate(request, username=username, password=password)

    if user is not None:
        # Authentication successful
        login(request, user)        
        response =  JsonResponse({'message': 'SUCCESS'}, status=200)
        return response   
    else:
        # Authentication failed
        return JsonResponse({'message': 'FAILURE'}, status=401)


def signup_api(request):
    req_body = request.body.decode('utf-8')
    req = json.loads(req_body)
    email = req["email"]
    password = req["password"]
    group_name = req["group"]
    try:
        # Create a new user
        user = User.objects.create_user(username=email, password=password)
        # Retrieve the group object
        group = Group.objects.get(name=group_name)
        # Add the user to the group
        group.user_set.add(user)
        response =  JsonResponse({'message': 'SUCCESS'}, status=200)
        return response   
    except Exception as e:
        # Handle any exceptions that occur during user creation or group addition
        print(f"An error occurred: {str(e)}")
        response = JsonResponse({'message': 'FAILURE'}, status=400)
        return response 

@login_required
def logout_api(request):
    logout(request)
    response =  JsonResponse({'message': 'SUCCESS'}, status=302)
    return response