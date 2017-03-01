import requests, re
from bs4 import BeautifulSoup
from extensions.link_gather import url_gather
from extensions.db import *



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
        for h in hrefs:
            turl = h
            if('www.' in turl):
                turl = turl.split('www.', 1)[-1]
            elif("https://" in turl):
                turl = turl.split('https://',1)[-1]
            turl = turl.split('.com', 1)[0]
            print("*********************")
            print("this is the url " + turl)
            bias = get_bias(turl)
            if(url_short == turl):
                self_reference += 1
            if(bias != 0):
                print("bias ", end='')
                print(bias)
                if(bias == 1):
                    tmp_bias = -10
                elif(bias == 2):
                    tmp_bias = -5
                elif(bias == 3):
                    tmp_bias = 0
                elif(bias == 4):
                    tmp_bias = 5
                elif(bias == 5):
                    tmp_bias = 10



            else:
                if(turl in "facebooktwitter"):
                    social_meida_ref += 1
                else:
                    unknowns += 1
                print("NO DATA ON SITE")

            total_bias = (total_bias + tmp_bias) / 2

        print("total_bias: ", end='')
        print(total_bias)
        print("social media references ", end='')
        print(social_meida_ref)
        print("self reference ", end='')
        print(self_reference)

        return_array = []
        return_array.extend((total_bias, social_meida_ref, self_reference, unknowns))

        return return_array
    else:
        print("website not in web_func yet")
