#!/usr/bin/env/ python
# -*- coding: utf-8 -*-

import hashlib

m = hashlib.sha256()
m.update(b"hello world and hello mars..")
print(m.digest())
print(m.digest_size)
print(m.block_size)
print(m.hexdigest())