from . import views
from django.urls import path

urlpatterns = [
    path('',views.loginpage,name='loginpage'),
    path('register/',views.register,name='register'),
    path('logout/',views.logoutUser,name='logoutUser'),
]