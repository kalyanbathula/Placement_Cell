from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')
def stats(request):
    return render(request, 'stats.html')

def Companies(request):
    return render(request, 'Companies.html')
def aboutus(request):
    return render(request,'aboutus.html')

def artificialintelligence(request):
    return render(request, 'artificialintelligence.html')

def cloudarchitect(request):
    return render(request, 'cloudarchitect.html')
def contactus(request):
    return render(request,'contactus.html')

def cybersecurityeng(request):
    return render(request, 'cybersecurityeng.html')

def dashboard(request):
    return render(request, 'dashboard.html')
def dashboard2(request):
    return render(request,'dashboard2.html')

def dashboard3(request):
    return render(request, 'dashboard3.html')

def dataanalyst(request):
    return render(request, 'dataanalyst.html')
def dataarchitect(request):
    return render(request,'dataarchitect.html')
def databaseadmin(request):
    return render(request, 'databaseadmin.html')

def datascientist(request):
    return render(request, 'datascientist.html')
def login_view(request):
    return render(request,'login.html',{})
def notifs(request):
    return render(request, 'notifs.html')

def softwaredev(request):
    return render(request, 'softwaredev.html')
def informationsecurityanalyst(request):
    return render(request,'informsecurityanalyst.html')
def networksecurityadmin(request):
    return render(request, 'networksecurityadmin.html')
def logout_user(request):
    logout(request)
    return redirect('index')
from django.http import JsonResponse

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
import json


def submit_form_view(request):
    if request.method == 'POST':
        # Retrieve form data from the request
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comments = request.POST.get('comments')

        # Perform form validation
        if not name or not email or not phone or not comments:
            messages.error(request, 'All fields are required.')
            return redirect('contactus')  # Assuming 'contactus' is the URL name for the contact form page

        # Process the form data
        # ...
        messages.success(request, 'Form submitted successfully.')


    # If the request method is not POST, render the form page
    return render(request, 'contactus.html')  # Replace 'contactus.html' with the actual template name

from django.shortcuts import render
import json
import os
from django.conf import settings

def get_job_listings(request):
    if request.method == 'GET':
        json_file_path = os.path.join(settings.BASE_DIR,'PlacementApp', 'static', 'js', 'job.json')
        with open(json_file_path) as json_file:
            data = json.load(json_file)
            job_listings = data['jobs']
        return render(request, 'job_listings.html', {'job_listings': job_listings})