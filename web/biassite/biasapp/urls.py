from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),

    url(r'history$', views.history, name='history'),
    url(r'^(?P<id>[0-9]+)/article/$', views.article, name='article'),
    url(r'^(?P<id>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^stats$', views.stats, name='stats'),
    url(r'about$', views.about, name='about'),
    url(r'register$', views.register, name='register'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
