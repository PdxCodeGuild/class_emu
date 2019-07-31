from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect


from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register_login(request):
    
    message = request.GET.get('message', '')
    next = request.GET.get('next', '')
        
    
    context = {
        'message': message,
        'next': next
    }
    return render(request, 'users/register_login.html', context)


def register_user(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    next = request.POST['next']
    
    user = User.objects.create_user(username, email, password)
    login(request, user)
    
    if next != '':
        return HttpResponseRedirect(next)
    return HttpResponseRedirect(reverse('users:protected'))


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    next = request.POST['next']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if next != '':
            return HttpResponseRedirect(next)
        return HttpResponseRedirect(reverse('users:protected'))
    if next != '':
        return HttpResponseRedirect(reverse('users:register_login')+'?message=fail&next='+next)
    return HttpResponseRedirect(reverse('users:register_login')+'?message=fail')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:register_login')+'?message=logout')

@login_required
def protected(request):
    # print(request.user.username)
    return render(request, 'users/protected.html')

@login_required
def protected2(request):
    # print(request.user.username)
    return HttpResponse('protected2')