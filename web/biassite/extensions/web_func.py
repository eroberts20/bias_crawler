from bs4 import BeautifulSoup
import requests, re

def get_title(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        if(len(soup('title')) != 0):
            return  soup('title')[0].string
        else:
            return "couldn't fetch title"
    except requests.exceptions.RequestException as e:  # This is the correct synta
        return "couldn't fetch title"





def washingtonpost(html_text):
    html_text = html_text.find("article")
    return html_text

def thefiscaltimes(html_text):
    html_text = html_text.find("div", {"class":"field-content"})
    return html_text

def time(html_text):

    html_text = html_text.find("div", {"data-reactid":"180"})
    print(html_text)
    return html_text

def democracynow(html_text):
    html_text = html_text.find("div", {"class":'headline_summary'})
    return html_text

def fivethirtyeight(html_text):
    html_text = html_text.find("div", {"class":"entry-content single-post-content"})
    return html_text

def cnn(html_text):
    html_text = html_text.find("div", {"itemprop": "articleBody"})
    return html_text

def bbc(html_text):
    html_text = html_text.find("div", {"class":"story-body__inner"})
    return html_text

def thehill(html_text):
    html_text = html_text.find("div", {"id":"content"})
    return html_text

def suntimes(html_text):
    html_text = html_text.find("div", {"id":"main"})
    return html_text
'''
def spectator(html_text):
    html_text = html_text.find("div", {"class": "print-only"})
    return html_text
'''

def breitbart(html_text):
    html_text = html_text.find("div", {"class":"entry-content"})
    return html_text

def cbn(html_text):
    html_text = html_text.find("div", {"class":"field-items"})
    return html_text

def thedailybeast(html_text):
    html_text = html_text.find("div", {"class":"ArticleBody"})
    return html_text

def nytimes(html_text):
    html_text = html_text.find("div", {"class":"story-body-supplemental"})
    return html_text

def csmonitor(html_text):
    html_text = html_text.find("div", {"class":"eza-body"})
    return html_text


def bloomberg(html_text):
    html_text = html_text.find("div", {"class":"body-copy"})
    return html_text

def apnews(html_text):
    html_text = html_text.find("div", {"class": "articleBody"})
    return html_text

'''
def huffingtonpost(html_text):
    html_text = html_text.find("div", {"class": "entry__text js-entry-text"})
    return html_text
'''

def fox(html_text):
    html_text = html_text.find("div", {"class":"article-text"})
    return html_text

def theblaze(html_text):
    html_text = html_text.find("div", {"class": "entry-content article-styles"})
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

def wsj(html_text):
    html_text = html_text.find("div", {"itemprop": "articleBody"})
    return html_text
