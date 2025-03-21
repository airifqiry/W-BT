from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('register_patient/', views.register_patient, name='register_patient'),  # нова
    path('register_volunteer/', views.register_volunteer, name='register_volunteer'),  # нова
    path('user_login/', views.user_login, name='user_login'),
]
