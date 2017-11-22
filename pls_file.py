#!/usr/bin/env python
# -*- coding: utf-8 -*-

#pip install urllib2
import requests
import configparser
import sys
import io

target_url = "http://46.20.3.204/listen.pls"
response = requests.get(target_url) # it's a file like object and works just like a file

'''for line in response: # files are iterable
    print(line)'''

print(response.content)

config = configparser.ConfigParser(allow_no_value=True)
config.read_string(str(response.content))
print(config.get("playlist", "NumberOfEntries"))
