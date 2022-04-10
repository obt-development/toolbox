from django.http import HttpResponse
from django.shortcuts import render
from .models import Event
import calendar
from calendar import HTMLCalendar
from datetime import datetime


def event(request):
    
    data = {
        'events': Event.objects.all()
    }
    
    return render(request, 'events/event.html', data)


def detail_event(request, pk):
    
    data = {
        'my_event': Event.objects.get(pk=pk)
    }
    
    return render(request, 'events/detail_event.html', data)

def create_event(request):
    if request.method == "POST":
        try: 
            new_event = Event()
            new_event.name = request.POST['name']
            new_event.description = request.POST['descrition']
            
            new_event.save()
            return HttpResponse("New Event Created !!")
        except:
            return HttpResponse("Error Creating New Event !!!")
    
    return render(request, 'events/create_event.html')


def calendar_view(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    cal = HTMLCalendar().formatmonth(year, month_number)
    current_date = datetime.now()
    current_year = current_date.year
    current_day = current_date.day
    current_month = current_date.month
    
    data={
        'year': current_year,
        'month' : month,
        'month_number' : month_number,
        'cal':cal,
        'current_date': current_date,
        'current_year':current_year,
        'current_day': current_day,
        'current_month' : current_month,
    }
    return render(request, 'events/calendar.html', data)