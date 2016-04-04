# -*- coding: utf-8 -*-
__author__ = 'yunge008'

'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Example
For example, given array S = {1 0 -1 0 -2 2}, and target = 0. A solution set is:
(-1, 0, 0, 1)
(-2, -1, 1, 2)
(-2, 0, 0, 2)

Note
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
'''

'''
# time exceed answer but correct
def fourSum(numbers, target):
    numbers.sort()
    pairs = {}
    four_list_sum = []
    if numbers > 4:
    # create pairs with key:sum_value and value:index
        for i in xrange(len(numbers)):
            for j in xrange(i + 1, len(numbers)):
                sum_ij = numbers[i] + numbers[j]
                if sum_ij not in pairs.keys():
                    pairs[sum_ij] = []
                pairs[sum_ij].append([i, j])
                sum1 = numbers[i] + numbers[j]
                sum2 = target - sum1
                if sum2 in pairs.keys():
                    for list_sum2 in pairs[sum2]:
                        temp_list = [i, j, list_sum2[0], list_sum2[1]]
                        four_list = [numbers[i], numbers[j], numbers[list_sum2[0]], numbers[list_sum2[1]]]
                        four_list.sort()
                        if len(set(temp_list)) == 4 and four_list not in four_list_sum:
                            four_list_sum.append(four_list)
    return four_list_sum
    '''


def fourSum(numbers, target):
    answer = []
    numbers.sort()
    length = len(numbers)
    for k in range(length-3):
        if numbers[k] + numbers[k+1] + numbers[k+2] + numbers[k+3] > target:
                break
        for i in range(k+1,length-2):
            low = i+1
            high = length - 1
            while low < high:
                temp = numbers[i] + numbers[low] + numbers[high] + numbers[k]
                if temp == target:
                    ans = [numbers[i], numbers[low], numbers[high], numbers[k]]
                    ans.sort()
                    low += 1
                    high -= 1
                    if ans not in answer:
                        answer.append(ans)
                    while low < high and numbers[high+1] == numbers[high]:  ##speed up, jump the same value
                        high -= 1
                    while low < high and numbers[low] == numbers[low-1]:
                        low += 1
                elif temp > target:
                    high -= 1
                else:
                    low += 1
    return answer



S = [1, 0, -1, 0, -2, 2]
print(fourSum(S,0))

