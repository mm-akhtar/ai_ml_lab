# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 16:11:06 2022

@author: kkakh
"""
import pandas as pd
import numpy as np

data = pd.DataFrame(data = pd.read_csv('3-dataset.csv'))
concepts = np.array(data.iloc[:,:-1])
target = np.array(data.iloc[:, -1])

def learn(concepts, target):
    specific_h = concepts[0].copy()
    print("Initialization of specific_h and general_h")
    print(specific_h)
    general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
    print(general_h)
    
    for i, h in enumerate(concepts):
        if target[i]=='Y':
            for x in range(len(specific_h)):
                if h[x] !=specific_h[x]:
                    specific_h[x]='?'
                    general_h[x][x]='?'
        print(specific_h)
        if target[i] == 'N':
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x]=specific_h[x]
                else:
                    general_h[x][x]='?'
        print("steps of candidate elimination algorithm", i+1)
        print(specific_h)
        print(general_h)
    indices = [i for i,val in enumerate(general_h) if val == ['?','?','?','?','?','?']]
    for i in indices:
        general_h.remove(['?','?','?','?','?','?'])
    
    return specific_h, general_h
                
s_final, g_final = learn(concepts, target)
print("Final Specific_h:", s_final, sep="\n")
print("Final General_h:", g_final, sep="\n") 