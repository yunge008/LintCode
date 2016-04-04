# -*- coding: utf-8 -*-
__author__ = 'yunge'

'''
Given an array and a value, remove all occurrences of that value in place and return the new length.
The order of elements can be changed, and the elements after the new length don't matter.

Example
Given an array [0,4,4,0,0,2,4,4], value=4
return 4 and front four elements of the array is [0,0,0,2]
'''


"""
@param A: A list of integers
@param elem: An integer
@return: The new length after remove
"""
def removeElement(A, elem):
    # write your code here
    if not A:
        return A
    for i in range(0,len(A)):
        try:
            A.remove(elem)
        except ValueError:
            break
    return A


A1 = [7,25,21,2,20,7,24,9,24,24,6,22,5,1,26,17,18,29,25,9,8,27,6,26,8,5,27,5,0,29,26,29,24,18,23,14,25,17,15,20,11,22,4,17,15,0,26,3,21,21,12,0,10,10,26,19,15,23,16,7,14,12,7,8,0,0,14,26,18,22,8,21,6,12,0,21,4,26,16,26,18,21]
elem1 = 26
A2 = [0,4,4,0,4,4,4,0,2]
elem2 = 4
print(removeElement(A1,elem1))


