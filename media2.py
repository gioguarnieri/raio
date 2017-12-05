#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys

n=200
aux=np.zeros(n*n, float)
mask=np.zeros(n*n, float)


for i in xrange(n):
 mask[i]=1.
 aux[i]=100.
for i in xrange(n-1,n/2,-1):
 mask[n*i+n/2]=1

for i in xrange(n):
 for j in xrange(n):
  print mask[i*n+j],
 print ''

exit()

maior=0.1
guarda=[]
ii=0
while(ii<4000):
 for i in xrange(n-1):
  for j in xrange(1,n+1):
   if(mask.item(i,j)!=1):
    aux2=aux.item(i,j)
    aux.itemset((i,j), (aux.item(i+1,j)+aux.item(i-1,j)+aux.item(i,j+1)+aux.item(i,j-1))/4)
#    guarda.append(abs(aux2-aux.item(i,j)))
 for j in xrange(n): 
  aux.itemset((j,0),aux.item(j,n))
  aux.itemset((j,n+1),aux.item(j,1))
 ii=ii+1

for i in xrange(n-1,-1,-1):
 for j in xrange(n-1,-1,-1):
  print str(round(aux.item(i,j),2)) + ' ' ,
 print ''
