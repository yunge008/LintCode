# -*- coding: utf-8 -*-
__author__ = 'yunge008'

class Solution:
    # @param str: a string
    # @return an integer
    def atoi(self, str111):
        # write your code here
        str111 = str111.strip()
        set1 = {"."}
        s = ""
        pORn = ""
        if str111 == "":
            s = 0
        else:
            if str111[0] in {"+","-"}:
                pORn = str111[0]
                str111 = str111[1:]
            for j in range(10): set1.update(set(str(j)))
            for i in range(len(str111)):
                if str111[i] in set1:
                    s += str111[i]
                else:
                    break
            if s == "":
                s = 0
            else:
                for k1 in range(len(s)):
                    if s[k1] != "0":
                        s = s[k1:]
                        break
                for k2 in range(len(s)):
                    if s[k2:k2+2] == "+-":
                        s = 0
                        break
                if s != 0 and "." in set(list(s)):
                    stemp = s.split(".")
                    if stemp[1] == "0":
                        s = stemp [0]
                if pORn == "-":
                    s = int("-" + str(s))
                if int(s) > 2147483647:
                    s = 2147483647
                elif int(s) < -2147483648:
                    s = -2147483648
        return s