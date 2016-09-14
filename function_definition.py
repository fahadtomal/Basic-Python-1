# -*- coding: utf-8 -*-
"""
Created on Sun May 22 14:03:39 2016

@author: Tomal- PC
"""
#function definition + finding prime number
#prerequisite : what is prime number and how  it can be found

def isprime(n):
    if n == 1:
        print("1 is special")
        return False
    for x in range(2, n):
        if n % x == 0:
            print("{} equals {} x {}".format(n, x, n // x))
            return False
    else:
        print(n, "is a prime number")
        return True

for n in range(1,50):
    isprime(n)
    
    
    
    
    
    """new function range()"""
 
    ''' help(range)
       range(...)
    range(stop) -> list of integers
    range(start, stop[, step]) -> list of integers
    
    Return a list containing an arithmetic progression of integers.
    range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
    When step is given, it specifies the increment (or decrement).
    For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
    These are exactly the valid indices for a list of 4 elements.
    '''
    
    
    
    
    
    
    
    
    
    