from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf.urls import url
from .views import StudentView
from django.urls import path
urlpatterns = [
    
    # path('home/', views.Home.as_view(), name="home"),
    # path('home/<int:id>/', StudentDetailView.as_view(), name='home'),
    path('student/', views.StudentView.as_view(), name="student"),
    
    
    
    
    # path('',home),
    # url('home', views.home.as_view(), name="home"),
    # path('student/',post_student,name = "student"),
    # path('update_student/<id>/', update_student)

]