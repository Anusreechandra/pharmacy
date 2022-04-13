from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('',views.main_page,name='mainpage'),
    path('login',views.login,name='login'),
    path('owner_home',views.owner_home,name='owner_home'),
    path('add_medicine',views.add_medicine,name='add_medicine'),
    path('view_medicine',views.view_medicine,name='view'),
 ]