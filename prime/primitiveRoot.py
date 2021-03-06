# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 01:04:34 2020

@author: Do Quang Tuan
"""

import collections
from prime.primeFactorization import primeFactorization
from prime.isPrime import isPrime

def hasPrimitiveRoot(n):
    if isPrime(n) or n == 4:
        return True
    
    factors = primeFactorization(n)
    counter = collections.Counter(factors)
    if counter[2] > 1:
        return False
    factors = list(set(factors))    
    if len(factors) > 2:
        return False
    if len(factors) == 2:
        if 2 not in factors:
            return False
    if not isPrime(factors[0]):
        return False
    
    return True

def isPrimitiveRoot(g, n):
    assert(isPrime(n))
    assert(0 < g and g < n)
    flag = True
    
    factors = list(set(primeFactorization(n-1)))
    for f in factors:
        if pow(g, (n-1)//f, n) == 1:
            flag = False
            break
    
    return flag

def getPrimitiveRootList(n):
    assert(isPrime(n))
    primitiveRootList = []
    
    for num in range(2, n):
        if isPrimitiveRoot(num, n):
            primitiveRootList.append(num)
            
    return len(primitiveRootList), primitiveRootList
        