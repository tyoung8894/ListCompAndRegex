#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 19:06:44 2017

@author: tyoung12
"""
import re
   
##1  Answer = 898
#p = re.compile('^[\w\-]+a$')

##2 Answer = 286
#p = re.compile('^[A-Za-z]{4}d$')

##3 Answer = 6,988
#p = re.compile('^[A-Za-z\-]+[aeiou]$')

##4 Answer = 1,655
#p = re.compile('^[AEIOUaeiou].*[AEIOUaeiou]$')

##5 Answer = 
#p = re.compile('^([aeiou])[a-z]*/1$')

##6 Answer = 19
#p = re.compile('.*[aeiou]{4}.*')

##7 Answer = 8
#p = re.compile('(?:[^in]*in){3}[^in]*')

##8 Answer = 
p = re.compile('^\w*(\w{2})\w*\1')



def readFile():
    lst = []
    #count = 0
    infile = open('lowerwords.txt', 'r')
    lines = infile.read()
    words = lines.split()
    infile.close()
    
    for i in range(len(words)):
        if words[i] not in lst:
            lst.append(words[i])
    
    return lst

    #for i in range(len(lst)):
        #print(lst[i])
        #count+=1
    
    #print(count)
        
#readFile()

#strings = re.findall(r'text pattern', f.read())


def filterList(regex, lst):
    #lst = readFile()
    count = 0
    for x in lst:
        result = regex.findall(x)
        #print(len(result))
        for p in result:
            count += 1
            print(p)
            
    print(count)
   

filterList(p, readFile())
