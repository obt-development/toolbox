from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.event, name = 'events'),
    path('<int:pk>/', views.detail_event, name = 'detail_events'),
    path('create_event/', views.create_event, name = 'create_event'),
    path('calendar/', views.calendar_view, name = 'calendar'),
    path('calendar/<int:year>/<str:month>/', views.calendar_view, name = 'calendar'),
    
]