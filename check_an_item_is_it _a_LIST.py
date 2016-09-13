# -*- coding: utf-8 -*-
"""
Created on Wed May 18 02:15:30 2016

@author: Tomal- PC
"""
#   isinstance() BIF
# find out nested lists in list and print them out 
#important technique


main_list = ["a" , "b", ["1" ,"2" , "3"] , "c", "d" , ["4" , "5"] , "e" ];


for tomal_1 in main_list :
    if isinstance(tomal_1 , list) :
     for tomal_2 in tomal_1 :
       print(tomal_2);
    else :
       print(tomal_1);


# tomal_1 and tomal_2 is called target identifier,
#target identifier is used to process a list(process each item of a list )
# each execution->target identifier = current data/item of list
#list in a list = nested list, here ["1","2","3"] ["4","5"]       
       