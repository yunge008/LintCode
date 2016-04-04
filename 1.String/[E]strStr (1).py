# -*- coding: utf-8 -*-
__author__ = 'yunge008'
'''
strstr (a.k.a find sub string), is a useful function in string operation. Your task is to implement this function.
For a given source string and a target string, you should output the first index(from 0) of target string in source string.
If target does not exist in source, just return -1.

Example
If source = "source" and target = "target", return -1.
If source = "abcdabcdefg" and target = "bcd", return 1.
Challenge
O(n2) is acceptable. Can you implement an O(n) algorithm? (hint: KMP)
'''

class Solution:
    def strStr(self, source, target):
        # write your code here
        if (source is None) and (target is None):
            return -1
        elif source == target:
            return 0
        elif target == "" and source:
            return 0
        elif (not source) or (not target):
            return -1
        elif len(source) < len(target):
            return -1
        for i in range(len(source)-len(target)+1):
            if target == source[i:i+len(target)]:
                return i
        return -1

s = Solution()
print s.strStr("source", "target")