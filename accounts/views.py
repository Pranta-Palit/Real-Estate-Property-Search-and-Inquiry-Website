from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST': # POST must be in capital letter
        # Register User, get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Validation: check if passwords match
        if password == password2:
            # Check if username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                # Check if username already exists
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email being used')
                    return redirect('register')
                else:
                    # create user
                    user = User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        email=email,
                        password=password
                    )
                    # Login after registration
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    
                    # redirect to login page
                    user.save()
                    messages.success(request, 'You are now registered and can login')
                    return redirect('login')


        else:
            messages.error(request, 'Password do not match')
            return redirect('register') 
    else:
        return render(request,'accounts/register.html')
    
def login(request):
    if request.method == 'POST': # POST must be in capital letter
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(
            username=username,
            password=password
        )

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request,'accounts/login.html')

def logout(request):  # it will not render any html, it will redirect to a page like index
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "You are now logged out")
    return redirect('index')

def dashboard(request):
    return render(request,'accounts/dashboard.html')