from django.shortcuts import render

def home(request):
    
    return render(request,'home.html', context={'info':'This is test message.'})