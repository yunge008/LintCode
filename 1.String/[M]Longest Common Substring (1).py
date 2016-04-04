# -*- coding: utf-8 -*-
__author__ = 'yunge'


'''
Given two strings, find the longest common substring.
Return the length of it.

Example
Given A = "ABCD", B = "CBCE", return 2.

Note
The characters in substring should occur continuously in original string. This is different with subsequence.

Challenge
O(n x m) time and memory.
'''

class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        z = 0
        m = len(A)
        n = len(B)
        L = [([-1]*n) for k in range(m)]
        for i in range(0, m):
            for j in range(0, n):
                if A[i] == B[j]:
                    if i == 0 or j == 0:
                        L[i][j] = 1
                    else:
                        L[i][j] = L[i-1][j-1] + 1
                    if L[i][j] > z:
                        z = L[i][j]
                else:
                    L[i][j] = 0
        return z


s = Solution()
A1 = "ABCD"
B1 = "CBC"
print s.longestCommonSubstring(A1,B1)