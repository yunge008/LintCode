# -*- coding: utf-8 -*-
__author__ = 'yunge008'

class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        # write your code here
        if len(B) > len(A):
            return False
        a = []
        b = []
        for i in range(len(B)):
            a.append(A[i])
            b.append(B[i])
        for i in range(len(A)-len(B)):
            a.append(A[len(B)+i])
        for i in range(len(B)):
            try:
                a.remove(b[i])
            except ValueError:
                return False
        return True
x = "ABCD"
y = "ABE"
s = Solution()
print s.compareStrings(x,y)