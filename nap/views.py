from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import *



def logPage(request):
	return render(request, 'nap/vhod.html')

def registrationPage(request):
	return render(request, 'nap/registration.html')

def registrationQuery(request):
    username = request.POST['username']
    password = request.POST['pass']
    email=request.POST['email']
    u = User.objects.create_user(username, email, password)
    u.save()
    return HttpResponseRedirect(reverse('nap:logPage'))

def loginin(request):
    username = request.POST['username']
    password = request.POST['pass']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('nap:index'))
    else:
        return HttpResponseRedirect(reverse('nap:logPage'))

def index(request):
	if request.user.is_authenticated:
		return gaaa(request)
	else:
		return logPage(request)

def deletee(request, task_id):
	Task.objects.get(pk=task_id).delete()
	return HttpResponseRedirect(reverse('nap:gaaa'))

def create_task(request):

	categorie = Categorie.objects.get(pk=request.POST['categorie'])
	t = Task(title=request.POST['title'], text=request.POST['text'], publish_date=timezone.now())
	t.categorie = categorie
	t.user = request.user
	t.save()

	return HttpResponseRedirect(reverse('nap:gaaa'))


def logoutQuery(request):
	logout(request)
	return HttpResponseRedirect(reverse('nap:logPage'))

def gaaa(request):
	return render(request, 'nap/gaaa.html', {'categorie_list': Categorie.objects.all(), 'task_list': Task.objects.filter(user=request.user)})

