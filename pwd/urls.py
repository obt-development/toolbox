from django.urls import path
from django.contrib.auth import views as auth_views
from .views import GeneratorView

app_name = 'pwd'

urlpatterns = [
    path('generator/', GeneratorView.as_view(), name = 'generator'),
    
]