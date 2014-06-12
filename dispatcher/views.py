from django.shortcuts import render

from dispatcher.models import Machine, Owner
from django.http import HttpResponse

# Create your views here.
def index(request):
    machine_list = Machine.objects.all()
    return render(request, 'dispatcher/index.html', {'machine_list': machine_list})

def signin(request):
    return render(request, 'dispatcher/signin.html', {})

def login(request):
    usermail = request.POST['loginEmail']
    password = request.POST['loginPasswd']

    try:
        user = Owner.objects.get(email=usermail, passwd=password)
    except Owner.DoesNotExist:
        return HttpResponse("User Not Exist!")
    # return HttpResponse("Login Success!")
    machine_list = Machine.objects.all()
    return render(request, 'dispatcher/logedin.html', {'user': user, 'machine_list': machine_list,})

def signup(request):
    return render(request, 'dispatcher/signup.html', {})

def register(request):
    username = request.POST['userName']
    usermail = request.POST['userEmail']
    password = request.POST['userPasswd']

    user = Owner(name=username, email=usermail, passwd=password)
    user.save()
    return render(request, 'dispatcher/signedup.html', {})


def lend(request):
    user_list = Owner.objects.all()
    return render(request, 'dispatcher/lendto.html', {'user_list': user_list,})


def userdetail(request, username):
    user = Owner.objects.filter(name=username)
    return render(request, 'dispatcher/userdetail.html', {'user': user})

def machinedetail(request, user, machine):
    return render(request, 'dispatcher/machinedetail.html', {'user': user, 'machine': machine})
