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

    def save(self, request,  commit=True):
        article = Articles()
        article.article_url = self.cleaned_data["url"]
        article.user = request.user

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
