from django.shortcuts import render
from .models import Contact
# Create your views here.
from django.http import HttpResponse
# Create your views here.


def index (request):
    return render(request,'index.html')


def about (request):
    return render(request,'about.html')


def contact(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'contact.html', {'thank': thank})



def gallery(request):
    return render(request, 'gallery.html')


def event(request):
    return render(request, 'event.html')



def donate(request):
    return render(request, 'donate.html')



def vol(request):
    return render(request, 'vol.html')



def camp(request):
    return render(request, 'camp.html')


def phil(request):
    return render(request, 'phil.html')


def fund(request):
    return render(request, 'fund.html')



def joinnow(request):
    return render(request, 'joinform.html')