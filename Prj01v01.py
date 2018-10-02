# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 20:53:49 2018

@author: 460
"""

r = list()
for a in range(1001, 1000000, 2):
    for j in range(3, int(a**0.5)+1, 2):
        if a % j == 0:
            break
    else:
        r.append(a)
#print(r)
n=len(r)
#print(n)
count = 0
for i in range(0, n-2):
    if r[i+1]-r[i] == 2:
        print(r[i], r[i+1])
        count +=1
print(count)
        