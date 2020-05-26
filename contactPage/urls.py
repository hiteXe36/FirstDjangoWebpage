from django.urls import path
from . import views

urlpatterns = [
    #empty route "''"
    path('', views.contactPage, name='contact-home'),
]
