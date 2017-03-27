import urllib.request


response = urllib.request.urlopen("https://www.googleapis.com/customsearch/v1?key=AIzaSyA12_w5ABSfHNEjL9bpO45P_pIEuWwsEQY&cx=004513427531628452432:p4a8opwwcv4&q=news").read()
print(response)
