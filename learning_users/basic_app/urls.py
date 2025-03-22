from django.urls import path,include 
from basic_app import views
from .views import user_logout,get_patients


    
    



#TEMPLAT EURLS
app_name='basic_app'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
     path('login_success/', views.login_success, name='login_success'),
    path('dashboard_volunteer/', views.volunteer_dashboard, name='volunteer_dashboard'),
     path('patient_home/', views.patient_home, name='patient_home'),
    path('register_patient/', views.register_patient, name='register_patient'),  
    path('register_volunteer/', views.register_volunteer, name='register_volunteer'),  
    path('login/',views.login_view,name='user_login'),
    path('calendar/',views.calendar_view,name='calendar'),
    path('logout/', views.user_logout, name='logout'),
    path('api/patients',views.get_patients,name='get_patients'),
    path('assign_patient/', views.assign_patient, name='assign_patient'),

]

