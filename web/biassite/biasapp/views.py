
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse, redirect
from .forms import *
from datetime import  *
from extensions.bias_algo import bias_algo
from extensions.db import get_bias
from extensions.google_search import similar_articles
from .models import Articles, Url
from django.views.generic import ListView
from django.shortcuts import get_object_or_404


from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from extensions.web_func import get_title


class ArticleListView(ListView):
    #model = Articles.objects.filter(user=self.request.user)
    paginate_by = 5
    template_name = 'history.html'
    def get_queryset(self):
        return Articles.objects.filter(user=self.request.user).order_by('-posted_on')


# Create your views here.
def index(request):
    if request.method=='POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            url = data['url']
            article = Articles.objects.filter(article_url=url)
            if(article):
                article = article[0]
                print("article previously searched")
                urlForm = UrlForm()
                context = {
                    'post':True,
                    'size':1,
                    'total_bias':article.calc_bias,
                    'self_reference':article.self_reference/article.total_links,
                    'social_meida_ref':article.social_meida_ref,
                    'unknowns':article.unknown_links,
                    'social_perc':article.social_meida_ref/article.total_links,
                    'page_name':"home",
                    'total_links':article.total_links,
                    'form':urlForm
                }
            else:
                total_bias = bias_algo(url)
                urlForm = UrlForm()
                if(total_bias != None):
                    article = form.save(total_bias, request)

                    for link in total_bias[6]:
                        title = get_title(link[0])
                        tmp_url = Url(link_url = link[0], article=article, title=title, text=link[1][0], positive = link[1][1]['pos'], negative = link[1][1]['neg'], neutral = link[1][1]['neu'])
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
                            'total_links':total_bias[5],
                            'form':urlForm
                        }
                else:
                    context = {
                        'post':True,
                        'size':2,
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




def article(request, id):
    article =  Articles.objects.get(id=id)
    links = []
    similar = []
    links = Url.objects.all().filter(article=article).reverse()
    size = links.count()
    similar = similar_articles(article.title, article.website)
    similar.pop(0)
    context = {
        'article':article,
        'social_perc':article.social_meida_ref/article.total_links,
        'self_reference':article.self_reference/article.total_links,
        'unknowns':article.unknown_links,
        'size':article.total_links,
        'similar':similar,
        'links':links
    }

    return render(request, 'article.html', context)



def delete(request, id):
    article = get_object_or_404(Articles, pk=id)
    article.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


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

def stats(request):
    articles = Articles.objects.all()

    unique = divide_sources(articles)

    if request.GET.get('featured'):
        featured_filter = request.GET.get('featured')
        articles = Articles.objects.filter(website=featured_filter)
        print(featured_filter)
    else:
        articles = None

    average_bias = 0
    average_links = 0
    if(articles != None):
        for article in articles:
            average_bias = average_bias + article.calc_bias
            average_links = average_links + article.total_links

        average_bias = average_bias / len(articles)
        average_links = average_links / len(articles)
        bias = get_bias(articles[0].website)
        context = {
            'average_links':average_links,
            'bias':bias,
            'website':articles[0].website,
            'average_bias':average_bias,
            'articles':articles,
            'unique':unique
        }
    else:
        context = {
            'unique':unique

        }
    return render(request, 'stats.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def logout(request):
    logout(request)


def divide_sources(articles):
    unique = []
    for article in articles:
        unique.append(article.website)
    unique = set(unique)
    return unique
