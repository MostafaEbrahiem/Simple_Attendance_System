from . import views
from django.urls import path

urlpatterns = [
    path('home/',views.home,name='home'),
    path('Leave/',views.func_Leave,name='Leave'),
    path('Show/',views.Show,name='Show'),
]