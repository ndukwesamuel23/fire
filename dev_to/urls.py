"""dev_to URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home.views import *

from signin.views import registerPage
from signin.views import loginPage
from signin.views import testt





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('registration/', registerPage,name='registration'),
    path('login/', loginPage, name='login'),
    path('testt/', testt, name='testt'),

]
# from home.views import *

# from signin.views import registerPage
# from signin.views import loginPage



# urlpatterns = [
#     path('',home, name='home'),
#     path('registration/', registerPage,name='registration'),
#     path('login/', loginPage, name='login'),
#     path('check/<str:id_test>', check, name='check'),
 
    
#     path('newpost/', newpost, name='newpost'),
    

    
#     # path('test/', test, name='test'),



#     path('navbar/',navbar, name='navbar'),
#     path('admin/', admin.site.urls),
# ]
