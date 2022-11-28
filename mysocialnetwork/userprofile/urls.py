from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserAPI.as_view(), name='userProfile'),
    path('<int:pk>/', views.UserAPI.as_view(), name='userProfile'),
]

