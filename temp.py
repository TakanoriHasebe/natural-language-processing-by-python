#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:11:57 2017

@author: Takanori
"""

"""
temp
"""

import codecs

fin = codecs.open('corpora/gingatetsudono_yoru.txt', 'r', 'utf-8')
data = fin.read()
fin.close()

print(data)







