import requests
from bs4 import BeautifulSoup


def similar_articles(title, website):
    uppers = []
    lowers = []

    # Note that loop below could be modified to skip ,.-\/; and etc if neccessary
    for word in title.split():
        if word[0].isupper():
            uppers.append(word)
            uppers.append(" ")
        else:
            lowers.append(word)


    title = ''.join(uppers)

    if "The Washington Post" in title:
        title = title.replace("The Washington Post", "")

    print (title)

    title = title.replace (" ", "+")
    #replaces whitespace with a plus sign for Google compatibility purposes

    r = requests.get('https://www.google.com/search?q=+{}&gbv=1&sei=YwHNVpHLOYiWmQHk3K24Cw'.format(title))
    soup = BeautifulSoup(r.text, "html.parser")
    #creates soup and opens URL for Google. Begins search with site:wikipedia.com so only wikipedia
    #links show up. Uses html parser.

    links = []
    for item in soup.find_all('h3', attrs={'class' : 'r'}):
        temp = item.a['href'][7:] # [7:] strips the /url?q= prefix
        links.append(temp.split("&sa=")[0])

    ret = []
    for item in links:
        try:
            print(item)
            page = requests.get(item)
            soup = BeautifulSoup(page.content, 'html.parser')
            if(len(soup('title')) != 0):
                ret.append([soup('title')[0].string, item])
            else:
                ret.append(["couldnt fetch title", item])
        except requests.exceptions.RequestException as e:  # This is the correct synta
                ret.append(["couldnt fetch title", item])

    return ret
