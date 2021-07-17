# Add the functions in this file

import json
D=dict()

def load_journal(fname):
  f=open(fname)
  data=json.load(f)
  return data
      

def compute_phi(fname,k):
   f=load_journal(fname)
   n00,n01,n10,n11=0
   for i in f:
     if i['squirrel']==False and k in i['events']:
       n01=n01+1
     elif i['squirrel']==False and k not in i['events']:
       n00=n00+1
     elif i['squirrel']==True and k in i['events']:
       n11=n11+1
     elif i['squirrel']==True and k not in i['events']:
       n10=n10+1
  
   
   n_0=n00+n01
   n_1=n11+n10
   n0_=n00+n10
   n1_=n11+n01
   
   correlation = ((n11 *n00) -(n10* n01)) / ((n_1*n_0*n1_*n0_)**(0.5))
   return correlation


def compute_correlations(fname):
  f=load_journal(fname)
  for i in f:
   for j in i['events']:
     D[j]=compute_phi(fname,j)
  return D
        


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
