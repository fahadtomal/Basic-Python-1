# -*- coding: utf-8 -*-
"""
Created on Wed May 18 00:49:25 2016

@author: Tomal- PC
"""

# BASIC TASK OF  isinstance()
# check type of a data , gives boolean result(true / false )
# [show the result code  in  the python console]


print("_______________________________________________");

A=["1" , "2" , "3"];
print( type(A) );
print(isinstance(A , list));   #isinstance(it , type) is it # type ? true/false

lenght = len(A);
print(isinstance(lenght , list));
print(isinstance(len(A) , list));
print(type(len(A)))
print(isinstance(len(A) , int))

print("_________________________________________________");


b = 2;
print(type(b));
print("so...");
print(isinstance(b , float));
print(isinstance(b , list));
print(isinstance(b , long));
print(isinstance(b , int));

print("_________________________________________________");


c = 2.00000000;
print(type(c));
print("so...");
print(isinstance(c , float));
print(isinstance(c , list));
print(isinstance(c , long));
print(isinstance(c , int));

print("_________________________________________________");


d = "tomal";
print(type(d));
print("so...");
print(isinstance(d , float));
print(isinstance(d , list));
print(isinstance(d , long));
print(isinstance(d , int));
print(isinstance(d , str));

print("--------------------------------------------------");




# types : int , long , float , str , list
