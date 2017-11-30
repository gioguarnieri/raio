#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys

n=200
aux=np.zeros((n,n), float)
mask=np.zeros((n,n), float)


for i in xrange(n):
 mask.itemset((0,i), 1)
 aux.itemset((0,i), 100)
for i in xrange(n-1,n/2,-1):
 mask.itemset((i,n/2), 1)
maior=0.1
guarda=[]
ii=0
while(ii<200):
 for i in xrange(n-1):
  for j in xrange(n-1):
   if(mask.item(i,j)!=1):
    aux2=aux.item(i,j)
    aux.itemset((i,j), (aux.item(i+1,j)+aux.item(i-1,j)+aux.item(i,j+1)+aux.item(i,j-1))/4)
    guarda.append(abs(aux2-aux.item(i,j)))
 ii=ii+1

for i in xrange(n-1,-1,-1):
 for j in xrange(n-1,-1,-1):
  print str(round(aux.item(i,j),2)) + ' ' ,
 print ''
