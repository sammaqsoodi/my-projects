from django.shortcuts import render

def index(request):

  return render(request,'homePage/index.html')

def about(request):

  return render(request,'homePage/about.html')  
