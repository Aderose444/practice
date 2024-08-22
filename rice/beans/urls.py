from django.urls import path
from . import views

app_name ='beans'
urlpatterns = [
    path('team/', views.team, name='team'),
    path('', views.member,name='member'),
]