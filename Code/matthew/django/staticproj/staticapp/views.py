from django.shortcuts import render



def page1(request):
    return render(request, 'staticapp/page1.html')


def page2(request):
    return render(request, 'staticapp/page2.html')
