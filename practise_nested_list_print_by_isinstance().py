# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


 #nested list print using for() , if , isinstance() BIF
#IMPORTANT TECHNIQUE

LIST = [1 ,2 , ["a" , "v"] , 4, 6 , ["tomal" , "fahad" ] , ["mostaque"]];

for target_identifier in LIST :
  if isinstance(target_identifier , list) :          #important list
    for target_identifier_2 in target_identifier :
        print(target_identifier_2);
  else:   print(target_identifier);
   
