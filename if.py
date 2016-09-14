# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:45:15 2016

@author: Tomal- PC
"""
''' new use of format() function '''
a ,b = 4 ,1;

if a>b :
    print("a is greater than b");
else :
    print("b is greater than a");
    
    # using fromat() function ;  "string".format()
a ,b = 4 ,1;

if a>b :
    print("a({}) is greater than b({})".format(a,b));
else :
    print("b ({}) is greater than a({})".format(a,b));
    
    #short if else
    
a , b = 1 , 2 ;
print("a>b" if a>b else "b>a");