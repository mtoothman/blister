

import urllib2
from bs4 import BeautifulSoup

target = "http://cd1025.com/about/playlists/now-playing"
page = urllib2.urlopen(target)

soup = BeautifulSoup(page, 'html.parser')

negative = [
    DEPECHE MODE
    MASTER AND SERVANT

    FRANK TURNER
    RECOVERY

    DAVID BOWIE
    FIVE YEARS
    ]

positive = [
    VIOLENT FEMMES
    BLISTER IN THE SUN

    FRANK TURNER
    RECOVERY

    DAVID BOWIE
    FIVE YEARS
    ]

def artist_title():
    result = []
#    for i in soup.find_all('tr'):
    for i in negative:
        result.append(i.text)
        if "VIOLENT FEMMES" in i.text:
            print i.text
            print "found!"
    else:
        print "not found!"

def all_times():
    result = []
    for i in soup.find_all('td', attrs={'class':'time'}):
        result.append(i.text)
    return result

artist_title()
all_times()
print("OK")
