from django.urls import path
from . import views
app_name='login_register'
urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('success',views.success,name='success'),
    path('register',views.register,name='register'),
    path('forms',views.forms,name='forms'),
    path('save',views.save,name='save'),
    path('logout', views.logout, name='logout'),

]