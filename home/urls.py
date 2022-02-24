
from django.urls import path,include
from home import views
urlpatterns = [
    
    path('', views.index),
    path('about', views.about),
    path('contact', views.contact),
    path('services', views.services),
    
    
    
]