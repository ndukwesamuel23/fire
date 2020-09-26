from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, login
from django.contrib.auth.decorators import login_required
from django.contrib import  messages



# teste
from django.contrib.auth.models import  User
# this is use to queary the user model



from  signin.form import  CreateUserForm
# Create your views here.



def testt(request):
    form = CreateUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CreateUserForm()

    else:
        bad = form.errors
        context = {
        'bad':bad}

    context = {
        'form': form,
        
    }


    return render(request, 'test.html', {})


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for user: ' +user)
                return redirect('login')

            else:
                bad = form.errors
                context = {'bad': bad}

        context = {'form': form,}

    return render(request, 'registration.html', context)







def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password1')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')

            else:
                print(
                messages.info(request, 'username or password is incorret '))
                print('the is not working ')
        return render(request, 'login.html',) 



# def mmm(request):

#     fire = User.objects.all()
#     print(fire)
#     for i in fire:
#         print(i)


#     return render(request, 'test.html',)

    



