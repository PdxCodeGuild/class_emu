from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register_login(request):
    # print(request.GET)
    # b = request.GET['a']
    # print(request.GET['lang'])
    return render(request, 'users/register_login.html')


def register_user(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    login(request, user)
    return HttpResponseRedirect(reverse('users:protected'))

@login_required
def protected(request):
    books = request.user.books.all()
    context = {
        'books': books
    }
    print(request.user.username) # able to access the user immediately
    return render(request, 'users/protected.html', context)


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('users:protected'))
    return HttpResponseRedirect(reverse('users:register_login'))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:register_login'))
