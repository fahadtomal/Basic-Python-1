# -*- coding: utf-8 -*-
"""
Created on Fri May 20 12:27:15 2016

@author: Tomal- PC
"""
#important mechanism
def processor(A) :
    for target_identifier in A :
        if isinstance(target_identifier, list):
                  processor(target_identifier);  #recursion
        else:
                print(target_identifier);
        
list_name=["a",["b",["c",["e"],]],"k"];
processor(list_name); 