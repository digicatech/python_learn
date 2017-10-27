#!/usr/bin/env python
# -*- coding: utf-8 -*-

#pip install requests
import requests
#print (requests.__file__)
r = requests.get('https://www.bitstamp.net/api/ticker/')

json = r.json()
print(json.get("high"))
print(json)
