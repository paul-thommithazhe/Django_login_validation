from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from app1.forms import CreateUserForm
from .forms import updateform
from django.views.decorators.cache import never_cache

# Create your views here.
@never_cache
def admin(request):
    if not request.session.has_key('admin'):
        return redirect('/')
    data = User.objects.all()
    return render(request,'app2/admin.html', {'data': data})

def delete(request, id):
    User.objects.get(id=id).delete()
    return redirect('/admin_panel')


def create(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin_panel')
    else:
        form = CreateUserForm()
    return render(request,'app1/register.html',{'form':form, 'url': '/admin_panel/create'})

def update(request, id):
    if request.method == 'POST':
        data = User.objects.get(id=id)
        form = updateform(request.POST,instance=data)
        if form.is_valid():
            val = form.cleaned_data
            
            data.username = val['username']
            data.email = val['email']
            data.save()

            return redirect('/admin_panel')
    else:
        data = User.objects.get(id=id)
        form = updateform(instance=data)
    return render(request,'app2/update.html',{'form':form, 'url': '/admin_panel/update', 'id': id})

def search(request):
    val = request.GET['search']
    data = User.objects.filter(username__contains=val)
    return render(request,'app2/admin.html', {'data': data})

def adminlogout(request):
    if request.session.has_key('admin'):
        del request.session['admin']
    return redirect('/')



