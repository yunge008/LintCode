# -*- coding: utf-8 -*-
__author__ = 'yunge008'
class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        # write your code here
        if len(s) != len(t):
            return False
        S = []
        T = []
        for i in range(len(s)):
            S.append(s[i])
            T.append(t[i])
        S.sort()
        T.sort()
        if S == T:
            return True
        return False


a = Solution()
print a.anagram('sa','sa')