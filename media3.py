#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys

n=5
aux=np.zeros(n*n, float)
aux2=np.zeros((n*n,n*n), float)
mask=np.zeros(n*n, float)


for i in xrange(n):
 mask[i]=1.
 aux[i]=100.
for i in xrange(n-1,n/2,-1):
 mask[n*i+n/2]=1
for i in xrange(n*n-1,n*n-n-1,-1):
 mask[i]=1


for i in xrange(n*n):
 aux2.itemset((i,i),4)
 if(mask[i]!=1):
   aux2.itemset((i,i-2), -1)
   aux2.itemset((i,i-1), -1)
   aux2.itemset((i,i+1), -1)
   aux2.itemset((i,i+2), -1)
   

#ii=0
#while(ii<4000):
# for i in xrange(0,n-1):
#  for j in xrange(0,n):
#   if(mask[i*n+j]!=1):
#    aux[i*n+j]=(aux[(i+1)*n+j]+aux[(i-1)*n+j]+aux[i*n+j+1]+aux[i*n+j-1])/4.
# ii=ii+1

for i in xrange((n)**2-1,-1,-1):
 for j in xrange((n)**2-1,-1,-1):
  print  aux2.item(i,j),
 print ''
