from django.urls import path
from . import views     #to use the home() function from views

urlpatterns = [
    path('', views.home, name='blog-home'),      #'' empty path so it's the homepage, home view from the views, name naming of the path 
    path('about/', views.about, name='blog-about'),
]


