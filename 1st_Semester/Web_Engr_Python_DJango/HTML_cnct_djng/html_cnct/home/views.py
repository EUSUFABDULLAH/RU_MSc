from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def home(request):
    # return HttpResponse("Eusuf")
    return render(request , "index.html")
