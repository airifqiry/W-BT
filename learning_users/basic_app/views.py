from django.shortcuts import render,redirect
from basic_app.forms import UserForm,UserProfileInfoForm
from django.http import JsonResponse  # Добави това
from .models import UserProfileInfo  
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import JsonResponse
from .models import UserProfileInfo  



 


# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')






def register(request):

    registered = False
    if request.method == 'POST':
        user_type = request.POST.get('user_type', 'patient')  # по подразбиране

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST, files=request.FILES)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            
            profile.user = user
            profile.user_type = user_type
            if 'profile_pic' in request.FILES:
                
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        user_type = request.GET.get('user_type', 'patient')  # fallback ако липсва

    template_name = 'basic_app/registaciqPacienti.html' if user_type == 'patient' else 'basic_app/registraciqDobrovolci.html'
    return render(request, template_name, {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    })
def login_view(request):
     return render (request,'basic_app/log_in.html')


def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return redirect('login_success')
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'basic_app/login.html', {})

@login_required
def login_success(request):
    profile = request.user.userprofileinfo
    if profile.user_type == 'volunteer':
        return redirect('volunteer_dashboard')
    elif profile.user_type == 'patient':
        return redirect('patient_dashboard')
    return redirect('home')

def calendar_view(request):
    return render(request, 'basic_app/kalendar.html')


@login_required
def volunteer_dashboard(request):
   return render(request, 'basic_app/homeDobrovolci.html')  # или шаблон по избор

@login_required
def patient_dashboard(request):
    return render(request, 'basic_app/homePacienti.html')  # или шаблон по избор

def register_patient(request):
    request.GET = request.GET.copy()
    request.GET['user_type'] = 'patient'
    return register(request)

def register_volunteer(request):
    request.GET = request.GET.copy()
    request.GET['user_type'] = 'volunteer'
    return register(request)

@login_required
def logout_view(request):
    logout(request)
    return redirect('index') 


def get_patients(request):
    # Взимаме всички пациенти от базата данни
    patients = UserProfileInfo.objects.filter(user_type='patient').values(
        'user__first_name', 'user__last_name', 'needs', 'location'
    )
    return JsonResponse(list(patients), safe=False)