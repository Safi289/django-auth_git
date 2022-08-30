from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User


def index(request):
    # return HttpResponse('home page');
    if request.user.is_authenticated:
        if request.user.is_authenticated == True:
            username = request.user.username
            diction = {'username': username}
        return render(request, 'home.html', context=diction)
    else:
        return HttpResponseRedirect("/accounts/login/")
