from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.core.mail import send_mail
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


from django.template.loader import get_template 

def sendEmail(request):
	
	task = Task.objects.get(pk=request.POST['taskId'])
	
	#data = "Привет! <img src='" + request.get_host() + "/static/img/im.jpg'> Как ты? \n Спорим, что плохо, потому что ты забыл про задачу? \n Вот она: \n\n" + task.title + "\n\n" + task.text + "\n\n Хороего дня! :Р"

	template = get_template('nap/email.html').render({'task': task, 'full_path': request.get_host()})

	send_mail('Notification!', 'ыы', "Darina", [request.user.email], fail_silently=False, html_message=template)
	return HttpResponseRedirect(reverse('nap:index'))