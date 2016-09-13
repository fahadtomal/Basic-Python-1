# -*- coding: utf-8 -*-
"""
Created on Fri May 20 11:21:05 2016

@author: Tomal- PC
"""
def processor(A) :
    for target_identifier in A :
        if isinstance(target_identifier, list):
                  processor(target_identifier);  #recursion
        else:
                print(target_identifier);
            
            
list_name = ["1" , 2, ["A" , "B" , "C", ["S", "o" , "a" , "r", ["t","o","m","a","l"]]
 ,"g" ,4, 5,7]];
processor(list_name);