#!/usr/bin/env python
# -*- coding: utf-8 -*-

#pip install requests
import requests
#print (requests.__file__)
r = requests.get('https://api.github.com/digicatech', auth=('user', 'pass'),verify=False)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())

json = r.json()
print(json.get("documentation_url"))