from django.urls import path
from . import views

urlpatterns = [
    #empty route "''"
    path('', views.startPage, name='startPage-home'),
]
