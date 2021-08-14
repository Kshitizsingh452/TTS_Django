from django.shortcuts import render
from .models import *
# Create your views here.

def index (request):
    if request.method=="POST":
        text = request.POST.get("message")
        alltexts = Messages(text = text)
        alltexts.save()

    return render(request, 'index.html')