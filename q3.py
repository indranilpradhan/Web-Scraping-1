#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib.request as ur
import bs4
import time
from playsound import playsound
url = "https://www.cricbuzz.com/live-cricket-scores/22747/ind-vs-ban-2nd-t20i-bangladesh-tour-of-india-2019"
req = ur.Request(url, headers={'User-Agent': 'Chrome/77.0.3865.120'})
flag=1
try:
    html = ur.urlopen(req).read()
    print(html)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    data=soup.find_all("span",{"class":"cb-font-20 text-bold"})
    for i in data:
        l =[x for x in i.contents[0].split()]
    a1 = int((l[1].split('/'))[0])
    b1 = int((l[1].split('/'))[1])
except IOError:
    print("Unable to make connection")
    flag=0
while True and flag:
    try:
        req = ur.Request(url, headers={'User-Agent': 'Chrome/77.0.3865.120'})
        html = ur.urlopen(req).read()
        soup = bs4.BeautifulSoup(html, 'html.parser')
        data=soup.find_all("span",{"class":"cb-font-20 text-bold"})
        l = []
        for i in data:
            l =[x for x in i.contents[0].split()]
        a = int((l[1].split('/'))[0])
        b = int((l[1].split('/'))[1])

        if a - a1 == 6 or a - a1 == 4:
            playsound('b.wav')
        if b - b1 == 1:
            playsound('a.wav')
        a1 = a
        b1 = b
        print(a1,b1,sep='/')
        time.sleep(5)
    except IOError:
        print("Can't create Connection")
        flag=0

