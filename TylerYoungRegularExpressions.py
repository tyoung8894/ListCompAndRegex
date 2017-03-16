#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 19:06:44 2017

@author: tyoung12
"""

##Tyler Young

import re
   
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



def filterList(regex, lst):
    count = 0
    for x in lst:
        result = regex.findall(x)
        for p in result:
            count += 1
            #print(p)
            
    print(count)
   
  
lst = readFile()


###Prints the word count for each question by calling filterList to create a
###word count of the words that fit the regular expression for that question
###some expressions did not work correctly in filterList so I had to use
###re.search manually to get the word count


##1  Answer = 898
p1 = re.compile(r'^[\w\-]+a$')
print("Word count for #1:")
filterList(p1, readFile())

##2 Answer = 286
p2 = re.compile(r'^[A-Za-z]{4}d$')
print("Word count for #2:")
filterList(p2, readFile())

##3 Answer = 6,988
p3 = re.compile(r'^[A-Za-z\-]+[aeiou]$')
print("Word count for #3:")
filterList(p3, readFile())

##4 Answer = 1,655
p4 = re.compile(r'^[AEIOUaeiou].*[AEIOUaeiou]$')
print("Word count for #4:")
filterList(p4, readFile())

###5 Answer = 398
print("Word count for #5:")
count5 = 0
answer5 = [x for x in lst if re.search(r'^([aeiou]).*\1$', x)]
for a in answer5:
    count5+=1

print(count5)

##6 Answer = 19
print("Word count for #6:")
p6 = re.compile('.*[aeiou]{4}.*')
filterList(p6, readFile())

##7 Answer = 8
print("Word count for #7:")
p7 = re.compile('(?:[^in]*in){3}[^in]*')
filterList(p7, readFile())

##8 Answer = 62
print("Word count for #8:")
count8 = 0
answer8 = [x for x in lst if re.search(r'.*([a-z][a-z]{2})\1.*', x)]
for a in answer8:
    count8+=1
 
print(count8)        


###9
#count9 = 0
#answer9 =[x for x in lst if re.search(r'.*([a-z])([a-z])\1\2.*', x)]
#for a in answer9:
    #print(a)

###10  answer = 39
print("Word count for #10:")
count10 = 0  
answer10 = [x for x in lst if re.search(r'.*([A-Za-z])\1.*([A-Za-z])\2.*([A-Za-z])\3.*', x)]
for a in answer10:
    count10 +=1
        
print(count10)



                            
    






    











