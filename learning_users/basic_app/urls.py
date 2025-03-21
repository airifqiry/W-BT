from django.urls import path,include 
from basic_app import views
from django.urls import path
from .views import get_patients

#TEMPLAT EURLS
app_name='basic_app'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
     path('login_success/', views.login_success, name='login_success'),
    path('dashboard/volunteer/', views.volunteer_dashboard, name='volunteer_dashboard'),
    path('dashboard/patient/', views.patient_dashboard, name='patient_dashboard'),
]

urlpatterns = [
    path('api/patients/', get_patients, name='get_patients'),
]

