#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

myDict = {"name":"Mike" , "surname":"Hammer"}
print(myDict["name"])

json1 = json.dumps(myDict , ensure_ascii=False)
print(json1)