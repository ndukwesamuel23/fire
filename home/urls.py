from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name="home"),
    # path('newpost', views.newpost, name='newpost'),
    path('blog/<str:id_test>/', views.blog, name="blog"),
    path('cry/', views.cry, name='cry')



]