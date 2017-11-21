#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

myAltDict = {"phone":"05559666333" , "address":"ISTANBUL"}
myDict = {"name":"Mike" , "surname":"Hammer" , "contact": myAltDict}
print(myDict["name"])

json1 = json.dumps(myDict , ensure_ascii=False)
print(json1)