
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CreateUserForm, loginform
from django.contrib import messages



# Create your views here.



def index(request):
    return render(request,'app1/index.html')

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CreateUserForm()
    return render(request,'app1/register.html',{'form':form, 'url': 'register'})

def login(request):
    if request.method == 'POST':
        form = loginform(request.POST)
        if form.is_valid():
            name = request.POST['username']
            pwd = request.POST['password']
            user = authenticate(username = name, password = pwd)
            if user:
                b = User.objects.get(username = name)
                if b.is_superuser:
                    request.session['admin'] = request.POST['username']
                    return redirect('/admin_panel')
                else:
                    request.session['user'] = request.POST['username']
                    return redirect('profile')
            else:
                return render(request,'app1/login.html',{'form':form ,'err':'user not found'})
    
    else:
        form = loginform()
    return render(request,'app1/login.html',{'form':form,'user':False})





def profile(request):
    if request.session.has_key('user'):
        return render(request,'app1/profile.html',{'user':request.session['user']})


def logout(request):
    return render(request,'app1/logout.html')
