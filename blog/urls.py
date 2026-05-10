from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),

    path('users/', views.users),
    path('blogs/', views.blogs),
    path('comments/', views.comments),
    path('categories/', views.categories),

    path('blogs/<int:id>/', views.blogdetails),
]