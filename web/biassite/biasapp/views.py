from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse, redirect
from .forms import *
from datetime import  *
from extensions.bias_algo import bias_algo
from .models import Articles, Url

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from extensions.web_func import get_title

# Create your views here.
def index(request):
    if request.method=='POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            url = data['url']
            total_bias = bias_algo(url)
            urlForm = UrlForm()
            article = form.save(request)

            for link in total_bias[6]:
                title = get_title(link)
                tmp_url = Url(link_url = link, article=article, title=title)
                tmp_url.save()
            if(total_bias == None):
                context = {
                    'post':True,
                    'total_bias':"No web scraping function for this site yet",
                    'size':1,
                    'page_name':"home",
                    'form':urlForm
                }
            else:
                context = {
                    'post':True,
                    'size':total_bias[4],
                    'total_bias':total_bias[0],
                    'self_reference':total_bias[2]/total_bias[5],
                    'social_meida_ref':total_bias[1],
                    'unknowns':total_bias[3],
                    'social_perc':total_bias[1]/total_bias[5],
                    'page_name':"home",
                    'form':urlForm
                }
            return render(request, 'index.html', context)
    else:
        urlForm = UrlForm()
        context = {
            'post':False,
            'page_name':"home",
            'form':urlForm
        }
        return render(request, 'index.html', context)


def history(request):

    context = {
        'articles':Articles.objects.all().filter(user=request.user).order_by('-id')[:10],
        'page_name':'history'
    }
    return render(request, 'history.html', context)

def article(request, id):
    article_id =  Articles.objects.get(id=id)
    links = []

    links = Url.objects.all().filter(article=article_id)
    size = links.count()
    print(size)
    context = {
        'article':article_id,
        'links':links
    }

    return render(request, 'article.html', context)



def delete(request, id):
    article = Articles.objects.get(id=id).delete()
    return HttpResponseRedirect('history')



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
