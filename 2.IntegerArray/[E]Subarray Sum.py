# -*- coding: utf-8 -*-
__author__ = 'yunge'

'''
Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.

Example
Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].
Note
There is at least one subarray that it's sum equals to zero.
'''

def subarraySum(nums):
    indexN = []
    if len(nums) == 1:
        indexN = [0, 0]
    else:
        for i in range(0,len(nums) - 1):
            sumN = nums[i]
            for j in range(i + 1 ,len(nums)):
                if sumN == 0:
                    j -= 1
                    break
                else:
                    sumN += nums[j]
            if sumN == 0:
                indexN = [i, j]
                break
    return indexN


num1 = [-3, 1, 2, -3, 4]
num2 = [1,-1]
num3 = [-5, 10, 5, -3, 1, 1, 1, -2, 3, -4]
print(subarraySum(num1))
print(subarraySum(num2))
print(subarraySum(num3))