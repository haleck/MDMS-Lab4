from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.UserAPICreate.as_view()),
    path('api/users/<int:pk>/', views.UserAPIUpdate.as_view()),

    path('api/posts/', views.PostAPICreate.as_view()),
    path('api/posts/<int:pk>/', views.PostAPIUpdate.as_view()),

    path('api/points/', views.PointsAPICreate.as_view()),
    path('api/points/<int:pk>/', views.PointsAPIUpdate.as_view()),

    path('api/comments/', views.CommentsAPICreate.as_view()),
    path('api/comments/<int:pk>/', views.CommentsAPIUpdate.as_view()),

    path('api/photos/', views.PhotosAPICreate.as_view()),
    path('api/photos/<int:pk>/', views.PhotosAPIUpdate.as_view()),
]

