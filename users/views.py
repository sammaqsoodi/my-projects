from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import Register


def login(request):
  
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username= username, password= password)

    if user is not None:
      auth.login(request,user)
      messages.success(request, f'با موفقیت وارد شدید')
      return redirect('homePage-home')
    else:
      messages.info(request,'نام کاربری یا گذرواژه اشتباه است')  
      return redirect('login')
  else:
    return render(request, 'users/login.html')  


def register(request):

  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if password1 == password2:
      if User.objects.filter(username=username).exists():
        messages.info(request,'نام کاربری قبلا گرفته شده است')
        return redirect('register')
      elif User.objects.filter(email=email).exists():
        messages.info(request,'ایمیل قبلا گرفته شده است')
        return redirect('register')
      else:    
        user = User.objects.create_user(username = username, password =password1, email= email,first_name= first_name, last_name = last_name)
        user.save();
        messages.success(request, f'اکانت شما ساخته شده')
        return redirect('login')
    else:
      messages.info(request,'گذرواژه مطابقت ندارد')
      return redirect('register')

  else:
    return render(request, 'users/register.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html')


def updateprofile(request):
  
  if request.method == 'POST':
    fist_name = request.POST['fist_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']

    user = auth.authenticate(username= username, password= password,last_name=last_name,fist_name=fist_name)

    if user is not None:
      auth.login(request,user)
      messages.success(request, f'با موفقیت وارد شدید')
      return redirect('homePage-home')
    else:
      messages.info(request,'نام کاربری یا گذرواژه اشتباه است')  
      return redirect('login')
  else:
    return render(request, 'users/login.html')