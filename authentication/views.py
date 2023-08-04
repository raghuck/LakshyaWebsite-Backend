from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
import json
from google.oauth2 import id_token
from google.auth.transport import requests
from lakshya.settings import config
# Create your views here.

# Create your views here.
def login_api(request):    
    req_body = request.body.decode('utf-8')
    req = json.loads(req_body)
    email = req["email"]
    password = req["password"]
    user = authenticate(request, username=email, password=password)

    if user is not None:
        # Authentication successful
        login(request, user)        
        response =  JsonResponse({'message': 'SUCCESS'}, status=201)
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
    user = User.objects.filter(username=email).first()
    if user:
        response = JsonResponse({'message': 'USER ALREADY EXISTS WITH THE GIVEN EMAIL'}, status=302)
    try:
        # Create a new user
        user = User.objects.create_user(username=email, password=password)
        # Retrieve the group object
        group = Group.objects.get(name=group_name)
        # Add the user to the group
        group.user_set.add(user)
        response =  JsonResponse({'message': 'SUCCESS'}, status=201)
        return response   
    except Exception as e:
        # Handle any exceptions that occur during user creation or group addition
        print(f"An error occurred: {str(e)}")
        response = JsonResponse({'message': 'FAILURE'}, status=500)
        return response 

def logout_api(request):
    if not request.user.is_authenticated:
        response =  JsonResponse({'message': 'REDIRECT'}, status=302)
        return response
    try:
        logout(request)
        response =  JsonResponse({'message': 'SUCCESS'}, status=201)
        return response
    except:
        response = JsonResponse({'message': 'FAILURE'}, status=401)
        return response

def third_party_auth(request,email):
    user = User.objects.filter(username=email).first()
    if user:
        # User already exists, log them in
        login(request, user)
        response =  JsonResponse({'message': 'SUCCESS'}, status=201)
        return response
    else:
        # User doesn't exist, create a new one and log them in
        try:
            user = User.objects.create_user(username=email, password=None)
            user.set_unusable_password()
            user.save()
            login(request, user)
            response =  JsonResponse({'message': 'SUCCESS'}, status=201)
            return response
        except Exception as e:
            print(e)
            response =  JsonResponse({'message': 'SUCCESS'}, status=500)
            return response       

def google_auth(request):
    json_data = json.loads(request.body)
    token = json_data['credential']
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), config['GOOGLE_AUTH_CLIENT'])
        email = idinfo['email']
        print("User Logged in via Google Auth :",email)
        response = third_party_auth(request,email)
        return response
    except ValueError:
        response = JsonResponse({'message': 'FAILURE'}, status=401)
        return response
    
    
