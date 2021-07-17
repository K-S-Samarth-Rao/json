# Add the functions in this file

import json

def load_journal(file:str)->dict:
    f=open(file,"r")
    return json.load(f)
    
def compute_phi(file:str, event:str)->float:
    journal=load_journal(file)
    correlation = 0.0
    n00 = n01 = n10 = n11 = 0
    n_0 = n0_ = n_1 = n1_ = 0
    
    for i in range(len(journal)):
        squirrel = dict(journal[i])['squirrel']
        events = dict(journal[i])['events']
        
        if squirrel == True:
            n_1 += 1
        else:
            n_0 += 1
              
        if event in events:
            n1_ += 1
            if squirrel:
               n11 += 1
            else:
               n10 += 1
        else:
             n0_ += 1
             if squirrel:
                 n01 += 1
             else:
                 n00 += 1
                  
     correlation = (n11 * n00 - n01 * n10)/((n_1 * n_0 * n0_ * n1_)**0.5)
     return correlation
     
def compute_correlations(file:str)->dict:
    journal = load_journal(file)
    events_dict = {}
    
    for i in range(len(journal)):
        events = journal[i]["events"]
        for j in events:
            if j not in events_dict:
               events_dict[j] = compute_phi(file,j)
    return events_dict
    
def diagnose(file: str)->dict:
    events_dict = computer_correlations(file)
    event = []
    
    max,min = -999,999
    high,low = "",""
    
    for i in events_dict:
        if(events_dict[i]<min):
            min = events_dict[i]
            low = i
        elif(events_dict[i]>max):
            max = events_dict[i]
            high = i
             
    event.append(high)
    event.append(low)
    
    return event  
