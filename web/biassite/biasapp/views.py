
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse, redirect
from .forms import *
from datetime import  *
from extensions.bias_algo import bias_algo
from extensions.db import get_bias
from extensions.google_search import similar_articles
from .models import Articles, Url, SimilarArticle
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.core import serializers

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
                    'self_reference':(article.self_reference/article.total_links) * 100,
                    'social_meida_ref':article.social_meida_ref,
                    'unknowns':article.unknown_links,
                    'social_perc':(article.social_meida_ref/article.total_links) * 100,
                    'page_name':"home",
                    'link':article.article_url,
                    'total_links':article.total_links,
                    'gov':article.gov_links,
                    'edu':article.edu_links,
                    'title':article.title,
                    'form':urlForm
                }
            else:
                total_bias = bias_algo(url)
                urlForm = UrlForm()
                if(total_bias != None):
                    article = form.save(total_bias, request)
                    title = "blank"
                    for link in total_bias[6]:
                        title = get_title(link[0])
                        tmp_url = Url(link_url = link[0], article=article, title=title, text=link[1][0], positive = (link[1][1]['pos']) *100, negative = (link[1][1]['neg']) * 100, neutral = link[1][1]['neu'] * 100)
                        tmp_url.save()
                    if(total_bias == None):
                        context = {
                            'post':True,
                            'total_bias':"No web scraping function for this site yet",
                            'size':1,

                            'page_name':"home",
                            'form':urlForm
                        }
                    elif(total_bias[5] == 0):
                        context = {
                            'post':True,
                            'total_bias':"No links in the article",
                            'size':1,

                            'page_name':"home",
                            'form':urlForm
                        }
                    else:
                        context = {
                            'post':True,
                            'size':1,
                            'total_bias':article.calc_bias,
                            'self_reference':(article.self_reference/article.total_links) * 100,
                            'social_meida_ref':article.social_meida_ref,
                            'unknowns':article.unknown_links,
                            'social_perc':(article.social_meida_ref/article.total_links) * 100,
                            'page_name':"home",
                            'link':article.article_url,
                            'total_links':article.total_links,
                            'gov':article.gov_links,
                            'edu':article.edu_links,
                            'title':article.title,
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
    similar_links = SimilarArticle.objects.all().filter(article=article)
    if similar_links:
        similar = similar_links
    else:
        alike = similar_articles(article.title, article.website)

        alike.pop(0)
        for sim in alike:
            new = SimilarArticle(link_url = sim[1], title = sim[0], article=article)
            similar.append(new)
            new.save()



    context = {
        'article':article,
        'social_perc': (article.social_meida_ref/article.total_links) * 100,
        'self_reference':(article.self_reference/article.total_links) * 100,
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
    articles1 = Articles.objects.all()
    articles1 = serializers.serialize('json', Articles.objects.all())


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
            'articles1':articles1,
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

@login_required
def self(request):
    user_articles = Articles.objects.filter(user=request.user).order_by('-posted_on')
    right_articles = user_articles.filter(calc_bias__gt=0)
    left_articles = user_articles.filter(calc_bias__lt=0)
    neutral_articles = user_articles.filter(calc_bias=0)
    size = user_articles.count()

    context = {
        'total_searched':user_articles.count(),
        'right_percent':(right_articles.count()/size) * 100,
        'left_percent':(left_articles.count()/size) *100,
        'user':request.user,
    }
    return render(request, 'self.html', context)

def test(request):
    context = {}
    return render(request, 'test.html', context)

def naive(request):
    context = {}
    return render(request, 'naive.html', context)
