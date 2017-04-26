from django.contrib import admin
from biasapp.models import Articles, Url, SimilarArticle

# Register your models here.
admin.site.register(Articles)
admin.site.register(Url)
admin.site.register(SimilarArticle)
