from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from biasapp.models import Articles
from extensions.web_func import get_title


class UrlForm(forms.Form):
    url = forms.CharField(
        label = "url",
        max_length = 300,
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'url'})
    )


    def save(self,total_bias,  request,  commit=True):
        turl = self.cleaned_data["url"]
        if('www.' in self.cleaned_data["url"]):
            turl =self.cleaned_data["url"].split('www.', 1)[-1]
        elif("https://" in turl):
            turl = turl.split('https://',1)[-1]
        turl = turl.split('.com', 1)[0]
        article = Articles()
        article.website = turl
        article.article_url = self.cleaned_data["url"]
        article.user = request.user
        article.calc_bias = total_bias[0]
        article.social_meida_ref = total_bias[1]
        article.unknown_links = total_bias[3]
        article.total_links = total_bias[5]
        article.self_reference = total_bias[2]
        article.title = get_title(article.article_url)
        try:
            check = Articles.objects.get(url=article.article_url)
        except:
            if commit:
                article.save()
            return article



class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'})
    )
    password = forms.CharField(
        label="Password",
        max_length=32,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'})
    )

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
    label="Email",
    required=True,
    widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'email'})
    )
    username = forms.CharField(
        label="Username",
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'})
    )

    password1 = forms.CharField(
        label="Password1",
        max_length=32,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password1'})
    )

    password2 = forms.CharField(
        label="Password2",
        max_length=32,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password2'})
    )
