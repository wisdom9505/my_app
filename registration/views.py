from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']

        # Create a new user object
        user = User.objects.create_user(username=username, password=password)
        user.first_name = first_name
        user.save()

        # Authenticate and login the user
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('services:shop')

    return render(request, 'registration/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('services:shop')
        else:
            # Handle invalid login credentials
            return render(request, 'registration/login.html', {'error': 'Invalid username or password.'})

    return render(request, 'registration/login.html')

