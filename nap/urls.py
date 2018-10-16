from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'nap'
urlpatterns = [
	path('', views.logPage, name='logPage'),
    path('registration/', views.registrationPage, name='registrationPage'),
    path('registrationQuery/', views.registrationQuery, name='registrationQuery'),
    path('logPage/', views.logPage, name='logPage'),
    path('loginin/', views.loginin, name='loginin'),
    path('index/', views.index, name='index'),
    path('create_task/', views.create_task, name='create_task'),
    path('logout/', views.logoutQuery, name='logout'),
    path('gaaa/', views.gaaa, name='gaaa'),
    path('deletee/<int:task_id>', views.deletee, name='deletee'),
    path('sendEmail', views.sendEmail, name='sendEmail'),

]

#    path('chto/', views.chto, name='chto'),
