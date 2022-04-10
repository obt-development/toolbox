from django.shortcuts import render, redirect
from django.core.mail import send_mail

from .forms import ContactForm

    
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website ToolBox" 
            body = {
            'name': form.cleaned_data['name'],     
            'firstname': form.cleaned_data['firstname'], 
            'email': form.cleaned_data['email'], 
            'message':form.cleaned_data['message'], 
            }
            message = "\n".join(body.values())
            send_mail(subject, message, 'boutet.13010@gmail.com', ['boutet.13010@gmail.com']) 
            return redirect('pages:home')
    
    form = ContactForm()
    return render(request, "contact/contact.html", {'form':form})