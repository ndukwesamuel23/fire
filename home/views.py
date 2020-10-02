from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.contrib.auth.models import  User

from home.models import Forum
from home.form import post_form
from home.form import cry_form

from django.contrib import messages


from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required





# Create your views here.

def home(request):
    blog = Forum.objects.all() 
    print(request.user)

    context= {
        'blog':blog
    }
    return render(request, 'index.html', context)

def navbar(request):
    return render(request, 'nav.html')

@login_required(login_url='login')
def newPost(request):
    form = post_form(request.POST or None)
    if form.is_valid():
        form.save()
        form = post_form
    
    else:
        bad = form.errors
        context = {
        'bad':bad}
    context = {
        'form': form,
        
    }
    return render(request, 'newpost.html', context)


@login_required(login_url='login')
def blog(request,id_test):
    total = Forum.objects.get(id=id_test)
 

    context ={
        'total':total,

    }
    
    return render(request, 'land.html', context)


def logout_user(request):
    logout(request)

    return redirect('login')




