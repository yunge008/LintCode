# -*- coding: utf-8 -*-
__author__ = 'yunge'

'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Example
For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:
(-1, 0, 1)
(-1, -1, 2)
Note
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
'''


def threeSum(numbers):
    triples = []
    length = len(numbers)
    if length < 3:
        return triples

    numbers.sort()
    for i in xrange(length):
        target = 0 - numbers[i]
        dic = {}
        for j in xrange(i + 1, length):
            if (target - numbers[j]) in dic:
                triple = [numbers[i], target - numbers[j], numbers[j]]
                if triple not in triples:
                    triples.append(triple)
            else:
                dic[numbers[j]] = j
    return triples


A = [-1, 0, 1, 2, -1, -4]
print(threeSum(A))
