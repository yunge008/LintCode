# -*- coding: utf-8 -*-
__author__ = 'yunge008'


class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        # O(n), O(n)
        d = dict()
        for str in strs:
            # "lint" -> ['i','l','n','t'] -> "ilnt"
            sorted_str = ''.join(sorted(str))
            d[sorted_str] = [str] if sorted_str not in d else d[sorted_str] + [str]
        res = []
        for str in d:
            if len(d[str]) >= 2:
                res += d[str]
        return res



s = Solution()
x1 = ["ardent","compilations","complainants","lactated","lactated","overjoying","overjoying","ranted","repackage","repackage","stiflings","stiflings","tramps","tramps"]
x2 = ["","b",""]
x3 = ["tea","and","ate","eat","den"]
print s.anagrams(x3)

