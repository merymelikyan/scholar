from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path('team/', views.team, name="team"),
    path('contact/', views.contact, name="contact"),
    path('courses/', views.courses, name="courses"),
    path('services/', views.services, name="services"),
    path('events/', views.events, name="events"),
   
    
] 