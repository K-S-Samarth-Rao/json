# Add the functions in this file

import json
d=dict()

def load_journal(fname):
  f=open(fname)
  data=json.load(f)
  return data
      

def compute_phi(fname,k):
   f=load_journal(fname)
   n00=0
   n01=0
   n10=0
   n11=0
   for i in f:
     if i['squirrel']==False and k in i['events']:
       n01=n01+1
     elif i['squirrel']==False and k not in i['events']:
       n00=n00+1
     elif i['squirrel']==True and k in i['events']:
       n11=n11+1
     elif i['squirrel']==True and k not in i['events']:
       n10=n10+1
  
   
   n0=n00+n01
   n1=n11+n10
   k0=n00+n10
   k1=n11+n01
   
   p= ((n11 *n00) -(n10* n01)) / ((n1*n0*k1*k0)**(0.5))
   return p


def compute_correlations(fname):
  f=load_journal(fname)
  for i in f:
   for j in i['events']:
     d[j]=compute_phi(fname,j)
  return d
        


def diagnose(fname):
  m=compute_correlations(fname)
  maximum=-1
  minimum=1
  for i in m:
    if m[i]>maximum:
       maximum=m[i]
       mm=i
    if m[i]<minimum:
       minimum=m[i]
       mn=i
  return(mm,mn)
