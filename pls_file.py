#!/usr/bin/env python
# -*- coding: utf-8 -*-

#pip install urllib2
import requests
import configparser
import sys
import io

#played song list
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
r = requests.get("http://46.20.3.204/played.html" , headers=headers)
#print(r.text)

#meta data
r2 = requests.get("http://mp3channels.webradio.antenne.de/chillout/index.html" , headers=headers)
print(r2.text)


#***** pls file ***************
#target_url = "http://46.20.3.204/listen.pls"
target_url = "http://mp3channels.webradio.antenne.de/chillout/listen.pls"
response = requests.get(target_url) # it's a file like object and works just like a file

'''for line in response: # files are iterable
    print(line)'''


#print(response.content)

config = configparser.ConfigParser(allow_no_value=True)
config.read_string(str(response.text))
#print(config.get("playlist", "NumberOfEntries"))

numberOfEntries = config.get("playlist", "NumberOfEntries")
print(numberOfEntries)

for n in range(0 , int(numberOfEntries)):
    print(config.get("playlist" , "File"+str(n+1)))
