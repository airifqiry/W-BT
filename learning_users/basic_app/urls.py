from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('register_patient/', views.register_patient, name='register_patient'),  
    path('register_volunteer/', views.register_volunteer, name='register_volunteer'),  
    path('login/',views.login_view,name='user_login'),
    path('calendar/',views.calendar_view,name='calendar')
]
