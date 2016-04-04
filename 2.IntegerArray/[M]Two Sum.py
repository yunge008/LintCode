# -*- coding: utf-8 -*-
__author__ = 'yunge'

'''
Given an array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where
index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.

Example
numbers=[2, 7, 11, 15], target=9
return [1, 2]

Note
You may assume that each input would have exactly one solution

Challenge
Either of the following solutions are acceptable:
O(n) Space, O(nlogn) Time
O(n) Space, O(n) Time
'''

def twoSum(numbers,target):
    num_map = {}
    for i in range(len(numbers)):
        x = numbers[i]
        if target - x in num_map.keys():
            return [num_map[target - x] + 1, i + 1]
        else:
            num_map[x] = i


numbers1=[0,4,3,0]
target1= 0

print(twoSum(numbers1, target1))