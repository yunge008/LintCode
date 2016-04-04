# -*- coding: utf-8 -*-
__author__ = 'yunge'

'''
Given an integers array A.
Define B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1], calculate B WITHOUT divide operation.

Example
For A = [1, 2, 3], return [6, 3, 2].
'''

def productExcludeItself(A):
    B = [1] * len(A)
    for i in range(len(A)):
        for j in range(len(A)):
            if j != i:
                B[i] *= A[j]
    return B

A = [1, 2, 3]
print(productExcludeItself(A))
