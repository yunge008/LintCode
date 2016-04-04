# -*- coding: utf-8 -*-
__author__ = 'yunge'

'''
Given an integer array, find a subarray with sum closest to zero. Return the indexes of the first number and last number.

Example
Given [-3, 1, 1, -3, 5], return [0, 2], [1, 3], [1, 1], [2, 2] or [0, 4].

Challenge
O(nlogn) time
'''

def subarraySumClosest(nums):
    target = 0
    index1 = index2 = 0
    if len(nums) > 1:
        sum_nums = [[nums[0], 0]]
        for i in xrange(1,len(nums)):
            sum_nums.append([sum_nums[i - 1][0] + nums[i], i])
        sum_nums.sort()
        min_subsum = abs(sum_nums[0][0])
        for j in xrange(1,len(sum_nums)):
            if min_subsum > abs(sum_nums[j][0] - sum_nums[j - 1][0] - target):
                min_subsum =  abs(sum_nums[j][0] - sum_nums[j - 1][0] - target)
                index1 = min(sum_nums[j][1], sum_nums[j - 1][1]) + 1
                index2 = max(sum_nums[j][1], sum_nums[j - 1][1])
    return [min(index1,index2), max(index1, index2)]

A = [6,-4,-8,3,1,7]
print(subarraySumClosest(A))