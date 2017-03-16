#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 17:02:51 2017

@author: tyoung12
"""

firstSentence = ['I', 'am', 'playing', 'xbox', 'and','trying','hard']
secondSentence = ['I', 'am', 'trying', 'hard', 'for', 'a', 'win']
print("First list: " + str(firstSentence))
print("Second list: " + str(secondSentence))

##1
#print([x for x in firstSentence+secondSentence if len(x) > 2])
 
 
##2
#print([x for x in firstSentence if len(x) >= 2 and x[:1] is 'a'])


##3
#print([x[-2:] for x in firstSentence])

##4
#print([x for x in firstSentence+secondSentence if len(x)%2 is 0])

##5 NOT DONE


##6
#print([x for x in firstSentence + secondSentence if len(x)>5])

##7
#print([x for x in firstSentence for y in secondSentence if len(x) < 3 and x is y])

##8
#print([x for x in firstSentence for y in secondSentence if x is y])

##9
#print([x[:1].upper() + x[1:] for x in firstSentence])

##10
#print([x.replace('a', 'ee') for x in firstSentence])

#11 NOT DONE
#print([(x,y) for x in firstSentence for y in secondSentence for z in range(len(firstSentence)) if firstSentence[z] != secondSentence[z]])

##12
#print([(x,y)for x in firstSentence for y in secondSentence if x is y])

##13
##print([x+y for x in firstSentence for y in secondSentence if len(y) > len(x)])

##14
##print([firstSentence.index(x) for x in firstSentence for y in secondSentence if x is y])

##15
#print([(x[0],y[0]) for x in firstSentence for y in secondSentence])