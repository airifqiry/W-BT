from django.shortcuts import render,redirect
from basic_app.forms import UserForm,UserProfileInfoForm
from django.http import JsonResponse  # Добави това
from .models import UserProfileInfo  
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import JsonResponse
from .models import UserProfileInfo  
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.contrib import messages





 


# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')






def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # 1. Създаване на потребител
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # 2. Създаване на потребителски профил (но още не го записваме в базата)
            profile = profile_form.save(commit=False)
            profile.user = user

            # 3. Автоматично попълване на община и област на база избраното село
            selected_village = profile_form.cleaned_data['location']  # Това е Settlement обект
            profile.location = selected_village.name
            profile.municipality = selected_village.municipality
            profile.region = selected_village.region

            # 4. Профилна снимка (по избор)
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            # 5. Записване на профила в базата данни
            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html', {
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
def patient_home(request):
    return render(request, 'homePacienti.html')




@login_required
def volunteer_dashboard(request):
    volunteer = request.user.userprofileinfo
    location = volunteer.location
    municipality = volunteer.municipality
    region = volunteer.region

    # Опитваме се първо да намерим пациенти от същото село
    patients = UserProfileInfo.objects.filter(
        user_type='patient',
        location__iexact=location
    )

    if not patients.exists():
        # Ако няма пациенти от същото село – търси от същата община
        patients = UserProfileInfo.objects.filter(
            user_type='patient',
            municipality__iexact=municipality
        )

    if not patients.exists():
        # Ако няма и от общината – търси от същата област
        patients = UserProfileInfo.objects.filter(
            user_type='patient',
            region__iexact=region
        )

    return render(request, 'basic_app/volunteer_dashboard.html', {
        'patients': patients,
        'location': location,
        'municipality': municipality,
        'region': region,
    })


def register_patient(request):
    request.GET = request.GET.copy()
    request.GET['user_type'] = 'patient'
    return register(request)

def register_volunteer(request):
    request.GET = request.GET.copy()
    request.GET['user_type'] = 'volunteer'
    return register(request)

@login_required
def user_logout(request):
    logout(request)
    return redirect('index') 

@require_POST
@login_required
def assign_patient(request):
    volunteer = request.user.userprofileinfo
    patient_id = request.POST.get('patient_id')
    patient = get_object_or_404(UserProfileInfo, id=patient_id, user_type='patient')

    # Добавяме пациента към избраните
    volunteer.assigned_patients.add(patient)
    messages.success(request, f"Пациент {patient.user.get_full_name()} беше добавен!")

    return redirect('volunteer_dashboard')

class CustomLoginView(LoginView):
    def get_success_url(self):
        user_type = self.request.user.profile.user_type
        if user_type == 'volunteer':
            return reverse('volunteer_dashboard')  # ще сочи към volunteer_dashboard.html
        elif user_type == 'patient':
            return reverse('home_patient')  # ще сочи към homePacienti.html
        return super().get_success_url()


def get_patients(request):
    # Взимаме всички пациенти от базата данни
    patients = UserProfileInfo.objects.filter(user_type='patient').values(
        'user__first_name', 'user__last_name', 'needs', 'location'
    )
    return JsonResponse(list(patients), safe=False)