from django.urls import path
from . import views

urlpatterns = [
    #empty route "''"
    path('', views.home, name='blog-home'),
    path('about', views.about, name='blog-about'),
]
