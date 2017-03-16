#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 17:02:51 2017

@author: tyoung12
"""
##Tyler Young
firstSentence = ['I', 'am', 'playing', 'xbox', 'and','trying','hard']
secondSentence = ['I', 'am', 'trying', 'hard', 'for', 'a', 'win']

##Prints the question number with the list for that question

##1
print("Question 1 list:")
print([x for x in firstSentence+secondSentence if len(x) > 2])
 
 
##2
print("Question 2 list:")
print([x for x in firstSentence if len(x) >= 2 and x[:1] is 'a'])


##3
print("Question 3 list:")
print([x[-2:] for x in firstSentence])

##4
print("Question 4 list:")
print([x for x in firstSentence+secondSentence if len(x)%2 is 0])

##5 
print("Question 5 list:")
print([x for x in range(0,len(firstSentence)) if len(firstSentence[x]) % 2 ==0])

##6
print("Question 6 list:")
print([x for x in firstSentence + secondSentence if len(x)>5])

##7
print("Question 7 list:")
print([x for x in firstSentence for y in secondSentence if len(x) < 3 and x is y])

##8
print("Question 8 list:")
print([x for x in firstSentence for y in secondSentence if x is y])

##9
print("Question 9 list:")
print([x[:1].upper() + x[1:] for x in firstSentence])

##10
print("Question 10 list:")
print([x.replace('a', 'ee') for x in firstSentence])

#11 not correct
print("Question 11 list:")
#print([(x,y) for i in range(0,len(firstSentence)) for x in firstSentence for y in secondSentence if firstSentence[i] is not secondSentence[i]])


##12
print("Question 12 list:")
print([(x,y)for x in firstSentence for y in secondSentence if x is y])

##13
print("Question 13 list:")
print([x+y for x in firstSentence for y in secondSentence if len(y) > len(x)])

##14
print("Question 14 list:")
print([firstSentence.index(x) for x in firstSentence for y in secondSentence if x is y])

##15
print("Question 15 list:")
print([(x[0],y[0]) for x in firstSentence for y in secondSentence])