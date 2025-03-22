from django.urls import path,include 
from basic_app import views
from .views import user_logout,get_patients


    
    



#TEMPLAT EURLS
app_name='basic_app'

urlpatterns = [
    
    path('user_login/',views.user_login,name='user_login'),
     path('login_success/', views.login_success, name='login_success'),
    path('volunteer_dashboard', views.volunteer_dashboard, name='volunteer_dashboard'),
     path('index_patient/', views.index_patient, name='index_patient'),
    path('register_patient/', views.register_patient, name='register_patient'),  
    path('register_volunteer/', views.register_volunteer, name='register_volunteer'),  
    path('calendar/',views.calendar_view,name='calendar'),
    path('logout/', views.user_logout, name='logout'),
    path('list_of_patients/',views.listofp,name='list_of_patients'),
    path('v_index',views.v_index,name="vol_index"),

    

]

