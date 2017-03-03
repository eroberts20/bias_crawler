from django.shortcuts import render, redirect
from .forms import *
from datetime import  *
from extensions.bias_algo import bias_algo
from .models import Articles

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    if request.method=='POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            url = data['url']
            urlForm = UrlForm()
            form.save(request)
            total_bias = bias_algo(url)
            if(total_bias == None):
                context = {
                    'total_bias':"No web scraping function for this site yet",
                    'page_name':"home",
                    'form':urlForm
                }
            else:
                context = {
                    'size':total_bias[4],
                    'total_bias':total_bias[0],
                    'self_reference':total_bias[2],
                    'social_meida_ref':total_bias[1],
                    'unknowns':total_bias[3],
                    'page_name':"home",
                    'form':urlForm
                }
            return render(request, 'index.html', context)
    else:
        urlForm = UrlForm()
        context = {
            'page_name':"home",
            'form':urlForm
        }
        return render(request, 'index.html', context)


def history(request):

    context = {
        'articles':Articles.objects.all().filter(user=request.user),
        'page_name':'history'
    }
    return render(request, 'history.html', context)


def register(request):
    form = RegisterForm()
    context = {
        'form':form,
        'cur_date':datetime.now(),
        }
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
            login(request, user)

        return redirect('index')

    else:
        return render(request, "register.html", context)

def about(request):
    context = {}
    return render(request, 'about.html', context)


def logout(request):
    logout(request)
