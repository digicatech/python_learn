#!/usr/bin/env/ python
# -*- coding: utf-8 -*-

import json
import requests
url = "http://localhost:9200/dict/entrtest"
jsonData = {'description':'This is json data'}
requests.post(url , json=jsonData)
