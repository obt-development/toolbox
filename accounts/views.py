from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import forms
from .models import CustomUser

from .forms import CustomUserCreationForm


def register(request):
    if request.user.is_authenticated:
        return redirect('pages:home')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'accounts:profil')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/register.html', context)


def modifprofil(request, id):
    user = get_object_or_404(CustomUser, id=id)
    form = CustomUserCreationForm(request.POST or None, instance=user)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('accounts:profil')
    
    return render(request, 'accounts/modifprofil.html', {"form":form})


def profile(request):
    if request.method == 'Request':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/profile.html', context)



