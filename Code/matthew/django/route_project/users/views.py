from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return HttpResponse('Login page')

def register(request):
    return HttpResponse('Registration page')
    
def logout(request):
    return HttpResponse('Logout page')