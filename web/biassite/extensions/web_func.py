from bs4 import BeautifulSoup
import requests, re

def get_title(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    if(len(soup('title')) != 0):
        return  soup('title')[0].string
    else:
        return "couldn't fetch title"


def washingtonpost(html_text):
    html_text = html_text.find("article")
    return html_text

def cnn(html_text):
    html_text = html_text.find("div", {"itemprop": "articleBody"})
    return html_text

def nytimes(html_text):
    html_text = html_text.find("div", {"class":"story-body-supplemental"})
    return html_text

def apnews(html_text):
    html_text = html_text.find("div", {"class": "articleBody"})
    print(html_text)
    return html_text

def huffingtonpost(html_text):
    html_text = html_text.find("div", {"class": "entry__text js-entry-text"})
    return html_text

def fox(html_text):
    html_text = html_text.find("div", {"class":"article-text"})
    return html_text

def nbcnews(html_text):
    html_text = html_text.find("div", {"class": "article-body"})
    return html_text

def chicagotribune(html_text):
    html_text = html_text.find("div", {"class": "trb_ar_main"})
    return html_text

def usatoday(html_text):
    html_text = html_text.find("div", {"itemprop": "articleBody"})
    return html_text

def theguardian(html_text):
    html_text = html_text.find("div", {"itemprop": "articleBody"})
    return html_text

def abcnews(html_text):
    html_text = html_text.find("div", {"class":"article-copy"})
    return html_text

def latimes(html_text):
    html_text = html_text.find("div", {"itemprop": "articleBody"})
    return html_text

def buzzfeed(html_text):
    html_text = html_text.find("div", {"class":"buzz_superlist_item_text"})
    return html_text
