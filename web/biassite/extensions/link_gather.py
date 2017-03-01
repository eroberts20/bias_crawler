import requests, re
from extensions.db import get_bias
from extensions.web_func import *
from bs4 import BeautifulSoup


def url_func_choice(url, soup):
    if url == "washingtonpost":
        return  washingtonpost(soup)
    elif url == "cnn":
        return  cnn(soup)
    elif url == "nytimes":
        return  nytimes(soup)
    elif url == "apnews":
        return  apnews(soup)
    elif url == "huffingtonpost":
        return  huffingtonpost(soup)
    elif url == "nbcnews":
        return  nbcnews(soup)
    elif url == "foxnews":
        return  fox(soup)
    elif "chicagotribune" in url:
        return chicagotribune(soup)
    elif "usatoday" in url:
        return usatoday(soup)
    elif "theguardian" in url:
        return theguardian(soup)
    elif "abcnews" in url:
        return abcnews(soup)
    elif "latimes" in url:
        return latimes(soup)
    elif "buzzfeed" in url:
        return buzzfeed(soup)
    else:
        return  None


def url_gather(layer, url):
    if(layer == 3):
        return
    else:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        print(page)



        #all_links = soup.find("article")

        if('www.' in url):
            url = url.split('www.', 1)[-1]
        elif("https://" in url):
            url = url.split('https://',1)[-1]
        url = url.split('.com', 1)[0]



        all_links = url_func_choice(url, soup)


        #print(all_links.prettify())
        if(all_links != None):
            all_hrefs = []
            #all_hrefs = [tag['href'] for tag in all_links.select('a[href]')]

            for link in all_links.findAll('a', attrs={'href': re.compile("^http://")}):
                all_hrefs.append(link.get('href'))

            for link in all_links.findAll('a', attrs={'href': re.compile("^https://")}):
                all_hrefs.append(link.get('href'))




            hrefs = []

            for url in all_hrefs:
                if "https://" in url:
                    temp = "https"  + url.split('https', 1)[-1]
                    hrefs.append(temp)
                    #url_gather(layer + 1, temp)
                if "http://" in url:
                    temp = "http" + url.split('http', 1)[-1]
                    hrefs.append(temp)
                    #url_gather(layer + 1, temp)



            #print(hrefs)
            print(len(hrefs))
            return hrefs
        else:

            return None
