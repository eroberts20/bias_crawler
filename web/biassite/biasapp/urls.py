from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from biasapp.views import ArticleListView

urlpatterns = [

    url(r'^$', views.index, name='index'),

    url(r'^history/$', ArticleListView.as_view(), name='history'),
    url(r'^(?P<id>[0-9]+)/article/$', views.article, name='article'),
    url(r'^(?P<id>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^stats$', views.stats, name='stats'),
    url(r'^about$', views.about, name='about'),
    url(r'^register$', views.register, name='register'),
    url(r'^test$', views.test, name='test'),
    url(r'^self$', views.self, name='self'),
    url(r'^naive$', views.naive, name='naive')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
