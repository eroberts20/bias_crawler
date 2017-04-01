import requests, re
from bs4 import BeautifulSoup
from extensions.link_gather import url_gather
from extensions.db import *
from extensions.sentence import sentiment_api


def bias_algo(url):
    if('www.' in url):
        url_short = url.split('www.', 1)[-1]
    elif("https://" in url):
        url_short = url.split('https://',1)[-1]
    else:
        url_short = url
    url_short = url_short.split('.com', 1)[0]
    print("URLSHOET" + url_short)
    hrefs = url_gather(1, url)
    #variables

    tmp_bias = 0
    social_meida_ref = 0
    self_reference = 0
    total_bias = 0
    unknowns = 0
    if(hrefs != None):
        total_links = len(hrefs)
    tlinks  = []

    if(hrefs != None):
        for h in hrefs:
            turl = h[0]
            push = str.join(u'\n',map(str,h[1]))
            push = sentiment_api(push)
            tlinks.append((turl, push))

            if('www.' in turl):
                turl = turl.split('www.', 1)[-1]
            elif("https://" in turl):
                turl = turl.split('https://',1)[-1]
            turl = turl.split('.com', 1)[0]
            print("*********************")
            print("this is the url " + turl)

            tmp_bias = get_bias(turl)
            if(url_short == turl):
                self_reference += 1
            if(tmp_bias != None):
                print("bias ", end='')
                print(tmp_bias)
                total_bias = (total_bias + tmp_bias) / 2



            else:

                if(turl in "facebooktwitterinstagram"):
                    social_meida_ref += 1
                else:
                    unknowns += 1
                print("NO DATA ON SITE")
                tmp_bias = 0


        '''
        print("total_bias: ", end='')
        print(total_bias)
        print("social media references ", end='')
        print(social_meida_ref)
        print("self reference ", end='')
        print(self_reference)
        '''
        if(len(hrefs) == 0):
            size = 0
        else:
            size = 1
        return_array = []
        return_array.extend((total_bias, social_meida_ref, self_reference, unknowns, size, total_links, tlinks))
        '''
        0 total_bias is calculated bias
        1 social_meida_ref is number of links in article to social media
        2 self_reference is number of links in article to own domain
        3 unknowns are links in article not in my database
        4 size whether or not there are any links at all
        5 total_links is number of total links
        6 tlinks is the array of urls and dict of pos, neg, neu inside of tuple

        '''

        return return_array
    else:
        print("website not in web_func yet")
