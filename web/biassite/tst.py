from bs4 import BeautifulSoup
import requests, re

url = "http://www.theverge.com/2017/3/3/14795396/jeff-sessions-obscenity-pornography-free-speech-politics-conservatives-reddit"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

print( soup('title')[0].string)
