import requests, re
from bs4 import BeautifulSoup


url = 'http://www.cnn.com/2017/02/03/us/bishop-eddie-long-i-knew/index.html'

def washingtonpost(html_text):
    html_text = html_text.find("article")
    return html_text

def cnn(html_text):
    html_text = html_text.find("div", {"itemprop": "articleBody"})
    return html_text

def nytimes(html_text):
    html_text = html_text.find("article")
    return html_text

def url_gather(layer, url):
    if(layer == 3):
        return
    else:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        print(page)



        #all_links = soup.find("article")

        url = url.split('www.', 1)[-1]
        url = url.split('.com', 1)[0]



        if url == "washingtonpost":
            all_links = washingtonpost(soup)
        elif url == "cnn":
            all_links = cnn(soup)
        elif url == "nytimes":
            all_links = nytimes(soup)
        else:
            all_links = None

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
                    url_gather(layer + 1, temp)
                if "http://" in url:
                    temp = "http" + url.split('http', 1)[-1]
                    hrefs.append(temp)
                    url_gather(layer + 1, temp)



            print(hrefs)
            print(len(hrefs))

url_gather(1, url)
