from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import HttpResponse

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Construct the hello message
            hello_message = f"Hello, {user.first_name}! Welcome back."
            # Store the hello message in the session
            request.session['hello_message'] = hello_message
            # Display the hello message using an alert box
            if user.username == "kalyan@gmail.com":
                script = f"<script>alert('{hello_message}'); window.location.replace('/dashboard/');</script>"
                return HttpResponse(script)
            elif user.username == "akashpingali18@gmail.com":
                script = f"<script>alert('{hello_message}'); window.location.replace('/dashboard2/');</script>"
                return HttpResponse(script)
            elif user.username == "srihan@gmail.com":
                script = f"<script>alert('{hello_message}'); window.location.replace('/dashboard3/');</script>"
                return HttpResponse(script)
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})


        