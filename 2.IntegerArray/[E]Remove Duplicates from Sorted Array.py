# -*- coding: utf-8 -*-
__author__ = 'yunge'

'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.

Example
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2].
'''

def removeDuplicates(A):
    if not A:
        return 0
    else:
        j = 0
        for i in range(0, len(A)):
            if A[j] != A[i]:
                A[j+1], A[i] = A[i], A[j+1]
                j += 1
        return j + 1

A1 = [-10,-10,0,1,2,3]
A2 = []
# A3 = [-14,-14,-13,-13,-13,-13,-13,-13,-13,-12,-12,-12,-12,-11,-10,-9,-9,-9,-8,-7,-5,-5,-5,-5,-4,-3,-3,-2,-2,-2,-2,-1,-1,-1,-1,-1,0,1,1,1,1,2,2,2,3,3,3,4,4,4,4,5,5,5,6,6,6,6,7,8,8,8,9,9,9,10,10,10,11,11,11,12,12,12,13,14,14,14,14,15,16,16,16,18,18,18,19,19,19,19,20,20,20,21,21,21,21,21,21,22,22,22,22,22,23,23,24,25,25]
print(removeDuplicates(A1))
print(removeDuplicates(A2))
# print(removeDuplicates(A3))