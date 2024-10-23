from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def register(request):
    """
    Handle user registration.

    If the request method is POST, this function will create a new user 
    with the provided username, password, and first name. After creating 
    the user, it will authenticate and log in the user, redirecting them 
    to the shop page.

    Args:
        request: The HTTP request object containing the user data.

    Returns:
        HttpResponse: A redirect to the 'services:shop' if the user is 
        successfully registered and logged in, or renders the registration 
        template if the request method is not POST.
    """
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
    """
    Handle user login.

    If the request method is POST, this function will authenticate the 
    user with the provided username and password. If the credentials are 
    valid, it logs in the user and redirects them to the shop page. If 
    the credentials are invalid, it renders the login template with an 
    error message.

    Args:
        request: The HTTP request object containing the user credentials.

    Returns:
        HttpResponse: A redirect to the 'services:shop' if the user is 
        successfully logged in, or renders the login template with an 
        error message if the credentials are invalid.
    """
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
