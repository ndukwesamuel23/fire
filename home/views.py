from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.contrib.auth.models import  User

from home.models import Forum
from home.form import post_form
from home.form import cry_form





# Create your views here.

def home(request):
    blog = Forum.objects.all() 

    context= {
        'blog':blog
    }
    return render(request, 'index.html', context)

def navbar(request):
    return render(request, 'nav.html')


def cry(request):
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


    def cry(request):
        form = cry_form(request.POST or None)
        if form.is_valid():
            form.save()
            form = cry_form

    
        else:
            bad = form.errors
            context = {
            'bad':bad}

        context = {
            'form': form,
        
    }

    return render(request, 'test.html', context)





def blog(request,id_test):
    total = Forum.objects.get(id=id_test)
 

    context ={
        'total':total,

    }
    
    return render(request, 'land.html', context)







