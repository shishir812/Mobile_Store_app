from django.urls import path
from mobile_app import views

#app_name = 'mobile_app'


urlpatterns = [

     path('mobile/', views.index, name='mobile_list'),
     path('', views.mobile_create, name= 'mobile_create'),




]

