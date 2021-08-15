from django.http import response
from django.shortcuts import render
from django.http import  FileResponse
from django.views.static import serve
from .models import *
from . import tts
from django.utils.encoding import smart_str
import os
# Create your views here.

def index (request):
    if request.method=="POST":
        text = request.POST.get("message")
        alltexts = Messages(text = text)
        alltexts.save()
        tts.convert(text) 
    return render(request, 'index.html')

def get(request):
    response = FileResponse(open("tts.mp3", 'rb'))
    response["Content-Type"] = 'application/force-download'
    return response

def reset(request):
    os.system("rm tts.mp3")
    res = response.HttpResponse()
    return res