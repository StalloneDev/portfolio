from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from django.core.mail import send_mail, BadHeaderError

# Create your views here.
from .models import Contact



def index(request):
    
    
    
    return render(request, 'base.html',)