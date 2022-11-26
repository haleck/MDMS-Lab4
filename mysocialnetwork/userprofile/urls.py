from django.urls import path
from . import views

urlpatterns = [
    path('<int:userid>/', views.getUser, name='userProfile'),
]

