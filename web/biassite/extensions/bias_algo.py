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
    gov = 0
    edu = 0
    total_links = 0

    org_bias = 0
    if(hrefs != None):
        total_links = len(hrefs)
    if(total_links == 0):
        total_links = 0
    tlinks  = []

    if(hrefs != None):
        for h in hrefs:
            turl = h[0]
            push = str.join(u'\n',map(str,h[1]))
            push = sentiment_api(push)  #sentimnet of text in json format
            tlinks.append((turl, push)) #full url + sentiment

            if('.gov' in turl):
                gov += 1 #if government link
            elif('.edu' in turl):
                edu += 1 #if educational link
            else:
                if('www.' in turl):
                    turl = turl.split('www.', 1)[-1]
                elif("https://" in turl):
                    turl = turl.split('https://',1)[-1]
                turl = turl.split('.com', 1)[0]
                print("*********************")
                print("this is the url " + turl)

                '''




                '''

                tmp_bias = get_bias(turl)
                org_bias = tmp_bias


                if(url_short == turl):
                    self_reference += 1
                if(tmp_bias != None):
                    print(push[1])
                    if((push[1]['neu'] < push[1]['pos']) and (push[1]['neu'] < push[1]['neg'])):
                        if(push[1]['pos'] > push[1]['neg']):
                            if(tmp_bias > 0):
                                tmp_bias += 0.1
                            if(tmp_bias < 0):
                                tmp_bias -= 0.1
                            if(tmp_bias == 0):
                                tmp_bias -= 0.01
                        if( push[1]['neg'] > push[1]['pos'] ):
                            if(tmp_bias > 0):
                                tmp_bias -= 0.1
                            if(tmp_bias < 0):
                                tmp_bias += 0.1
                            if(tmp_bias == 0):
                                tmp_bias += 0.01

                    if(gov > 0):
                        if(tmp_bias > 0):
                            tmp_bias = tmp_bias - tmp_bias/(gov * 2)
                        if(tmp_bias < 0):
                            tmp_bias = tmp_bias + abs(tmp_bias)/(gov * 2)
                    if(edu > 0):
                        if(tmp_bias > 0):
                            tmp_bias = tmp_bias - tmp_bias/(edu * 2)
                        if(tmp_bias < 0):
                            tmp_bias = tmp_bias + abs(tmp_bias)/(edu * 2)
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
        return_array.extend((total_bias, social_meida_ref, self_reference, unknowns, size, total_links, tlinks, gov, edu, org_bias))
        '''
        0 total_bias is calculated bias
        1 social_meida_ref is number of links in article to social media
        2 self_reference is number of links in article to own domain
        3 unknowns are links in article not in my database
        4 size whether or not there are any links at all
        5 total_links is number of total links
        6 tlinks is the array of urls and dict of pos, neg, neu inside of tuple
        7 gov links
        8 edu links
        9 bias of original site

        '''

        return return_array
    else:
        print("website not in web_func yet")
