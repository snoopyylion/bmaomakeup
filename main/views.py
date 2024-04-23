from django.shortcuts import render,redirect
from django.http import HttpResponse
from main.models import AppInfo,Sevices,AboutMe,MyWorks
from django.contrib import messages
from .forms import ContactForm, AppointmentForm

# Create your views here.


def home(request):
    info = AppInfo.objects.get(pk=2)
    serv = Sevices.objects.get(pk=1)
    aboutm = AboutMe.objects.get(pk=1)
    mworks = MyWorks.objects.all()
    contact= ContactForm()
    if request.method == 'POST':
        contact = ContactForm(request.POST)
        if contact.is_valid: 
            contact.save()
            messages.success(request, 'Your message has been sent!')
        return redirect('home')
    
    context = {
        'info':info,
        'serv':serv,
        'aboutm':aboutm,
        'mworks':mworks,
        'contact':contact
    }
    return render(request, 'index.html', context)

def gallery(request):
    mworks = MyWorks.objects.all()
    
    
    context= {
        'mworks':mworks
    }
    return render(request, 'gallery.html', context)