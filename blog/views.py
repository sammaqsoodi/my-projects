from django.shortcuts import render
from . import views
from .models import Post

def index(request):
  context ={
    'posts': Post.objects.all()
  }
  return render(request,'blog/index.html',context)
