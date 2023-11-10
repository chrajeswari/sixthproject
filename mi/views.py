from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sky(request):
    return render(request,'sky.html')

def rohit(request):
    return HttpResponse('<h1>Best vicket keeper</h1>')