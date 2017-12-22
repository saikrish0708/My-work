# -*- coding: utf-8 -*-
"""
Created on Fri Dec 01 20:11:28 2017

@author: Saikrishna Nellutla
""" 
import numpy
import scipy
import csv
import pandas as pd


import itertools
from nltk.tokenize import word_tokenize
import re, csv, yaml
from nltk.corpus import wordnet as wn
from nltk.metrics import edit_distance

import nltk
 

imfile = pd.read_csv("C:/Users/Saikrishna Nellutla/Downloads/AIT624-imgdataset.csv")

imfile.dropna(axis=0,how="all",inplace = True)

def convert_dict(s):
    return re.sub(r'\W',' ',s)

imfile['list'] = imfile['Concept'].apply(convert_dict)

def remove_num(s):
    s = re.sub("\d+"," ", s) 
    return " ".join(s.split())

imfile['list'] = imfile['list'].apply(remove_num)

imfile['list'].head(5)

#
#words= ['business','ceremony','festival','group','indoors','people']
#new_words=[w.replace(words[0], words[1]) for w in words]
 

#abc=['business','ceremony','festival','group','indoors','people']
#for a, b in itertools.combinations(abc, 2):
   # ai = wn.synsets(a)[0]
   # bi = wn.synsets(b)[0]
   # print(ai)
   # print(bi)
    #print(ai.wup_similarity(bi))
   # x = int(ai.wup_similarity(bi))
    
  #  if x > 0.2: 
 #       [w.replace(b,a) for w in abc]
#        print(abc)


#Printing the new list with replaced words using wup similarity

n=392
count=0
p=0
newlist = []
while(count<n):
    tokens = word_tokenize(imfile['list'][count])
    for a in range(0, len(tokens)-2):
        for b in range(a+1, len(tokens)-1):
            print(a)
            print(b)
            x = wn.synsets(tokens[a])
            y = wn.synsets(tokens[b])
            if (len(x) != 0) and (len(y) != 0):               
                ai = x[0]
                bi = y[0]
                xyz = ai.wup_similarity(bi)
                if xyz is None:
                    xyz = 0
                if xyz > 0.5:
                    tokens[b] = tokens[a]
                print(ai)
                print(bi)
                print(xyz)
    print(tokens)
    newlist.append(tokens)
    count+=1
print(newlist)
newlist[391]
newlist
type(newlist)
len(newlist)
len(new_list)    
import csv

# Using lch similarity

n=392
count=0
p=0
newlist2 = []
while(count<n):
    tokens = word_tokenize(imfile['list'][count])
    for a in range(0, len(tokens)-2):
        for b in range(a+1, len(tokens)-1):
            print(a) 
            print(b)
            x = wn.synsets(tokens[a])
            y = wn.synsets(tokens[b])
            if (len(x) != 0) and (len(y) != 0):            
                ai = x[0]
                bi = y[0]
                try:
                    xyz = ai.lch_similarity(bi)
                except:
                    continue
                if xyz is None:
                    xyz = 0
                if xyz > 2:
                    tokens[b] = tokens[a]
                    #tokens = list(set(tokens))
                    #newlist[p] = tokens
                print(ai)
                print(bi)
                print(xyz)
    print(tokens)
    newlist2.append(tokens)
    count+=1
print(newlist2)

#Writing the output to CSV
 
df=pd.DataFrame({'Concept_wup': newlist})
df

df=df.assign(Concept_path=newlist2)
df.to_csv('new_AIT624_3.csv', encoding='utf-8', index=False)

