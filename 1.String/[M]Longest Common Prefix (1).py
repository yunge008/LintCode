# -*- coding: utf-8 -*-
__author__ = 'yunge'

'''
Given k strings, find the longest common prefix (LCP).

Example
For strings "ABCD", "ABEF" and "ACEF", the LCP is "A"
For strings "ABCDEFG", "ABCEFG" and "ABCEFA", the LCP is "ABC"
'''
class Solution:
    # @param strs: A list of strings
    # @return: The longest common prefix
    def longestCommonPrefix(self, strs):
        # write your code here
        try:
            LCP = strs[0]
            for str1 in strs:
                for i in range(len(LCP),0,-1):
                    if str1[0:i] != LCP:
                        LCP = LCP[0:i-1]
                    else:
                        break
            return LCP
        except IndexError:
            return ""

s = Solution()
x1 = ("ACERRR", "AEERR" ,"AFERSAD")
x2 = ("","ABCDEFG", "ABCEFG" , "ABCEFA")
x3 = ["ABC"]
print s.longestCommonPrefix(x3)