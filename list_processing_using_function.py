# -*- coding: utf-8 -*-
"""
Created on Fri May 20 01:31:38 2016

@author: Tomal- PC
"""


#list processing using function and recursion


def list_processor(A) :                    #function definition(list processing function) , A =argument
    for target_identifier in A :
        if isinstance(target_identifier, list) :
            list_processor(target_identifier);    #recursion
        else :print(target_identifier);


 
list_name= ["1" , "2" , ["A" ," B" , ["22" ," 33"] , "tomal" ,["1","2","3"]] , "QQ", ["A", "B" ,"C", ["the" , "end"]]];
list_processor(list_name);    # function calling, argument passing to function definition A
                   
        