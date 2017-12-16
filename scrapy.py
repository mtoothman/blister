

import urllib2
from bs4 import BeautifulSoup

# target = "http://cd1025.com/about/playlists/now-playing"
# page = urllib2.urlopen(target)

# soup = BeautifulSoup(page, 'html.parser')

negative = [ "DEPECHE MODE","MASTER AND SERVANT", "DAVID BOWIE", "FIVE YEARS" ]
positive = [ "VIOLENT FEMMES", "BLISTER IN THE SUN", "FRANK TURNER", "RECOVERY" ]

def artist_title():
    result = []
    for i in soup.find_all('tr'):
        result.append(i.text)
        if "VIOLENT FEMMES" in i.text:
            print i.text
            print "found!"
    else:
        print "not found!"

def check(input):
    result = []
    for i in input:
        result.append(i)
    if "VIOLENT FEMMES" in result:
        print "found!"
    else:
        print "not found!"

def all_times():
    result = []
    for i in soup.find_all('td', attrs={'class':'time'}):
        result.append(i.text)
    return result

print("positive...")
check(positive)

print("negative...")
check(negative)
#artist_title()
#all_times()
print("OK")
