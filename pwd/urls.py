from django.urls import path
from . import views

app_name = 'pwd'

urlpatterns = [
    path('generator/', views.generator, name = 'generator'),
    
]