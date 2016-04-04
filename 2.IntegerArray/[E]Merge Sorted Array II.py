# -*- coding: utf-8 -*-
__author__ = 'yunge'

'''
Merge two given sorted integer array A and B into a new sorted integer array.


Example
A=[1,2,3,4]
B=[2,4,5,6]
return [1,2,2,3,4,4,5,6]

Challenge
How can you optimize your algorithm if one array is very large and the other is very small?
'''

def mergeSortedArray(A, B):
    i = j = 0
    C = []
    while i + j <= len(A) + len(B):
        if i == len(A):
            C += B[j:]
            break
        elif j == len(B):
            C += A[i:]
            break
        elif A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    return C


A=[1]
B=[1]
print(mergeSortedArray(A, B))