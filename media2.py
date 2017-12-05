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

maior=0.1
guarda=[]
ii=0
while(ii<4000):
 for i in xrange(0,n-1):
  for j in xrange(0,n-1):
   if(mask[i*n+j]!=1):
#    aux2=aux[i*n+j]
    aux[i*n+j]=(aux[(i+1)*n+j]+aux[(i-1)*n+j]+aux[i*n+j+1]+aux[i*n+j-1])/4.
 ii=ii+1

for i in xrange(n-1,-1,-1):
 for j in xrange(n-1,-1,-1):
  print  aux[i*n+j],
 print ''
