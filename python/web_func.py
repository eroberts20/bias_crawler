 from bs4 import BeautifulSoup

def washingtonpost(html_text):
    html_text = html_text.find("article")
    return html_text

def cnn(html_text):
    html_text = html_text.find("div", {"itemprop": "articleBody"})
    return html_text

def nytimes(html_text):
    html_text = html_text.find("article")
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
