# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 16:57:46 2018

@author: hasee
"""
 

file1=None
file2=None
with open("C:/Users/hasee/Desktop/hw2/output.txt", "r") as fp:    
       file1 = fp.read().splitlines()
        
with open("C:/Users/hasee/Desktop/hw2/output2.txt", "r") as fp:    
       file2 = fp.read().splitlines()
 
print(len(file1))
print(len(file2))
for index in range(len(file1)):
    line=file1[index].split(',')
    line2=file2[index].split(',')
    
    for item,item2 in zip(line,line2):
        if item!=item2:
            print(index,False)
            print(item)
            print(item2)
 