from bs4 import BeautifulSoup
import requests, re


page = requests.get("https://fivethirtyeight.com/features/for-a-trump-nominee-neil-gorsuchs-record-is-surprisingly-moderate-on-immigration/")
