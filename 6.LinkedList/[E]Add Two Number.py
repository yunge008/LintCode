# -*- coding: utf-8 -*-
__author__ = 'yunge008'

"""
You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1's digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.

Example
Given 7->1->6 + 5->9->2. That is, 617 + 295.
Return 2->1->9. That is 912.

Given 3->1->5 and 5->9->2,
return 8->0->8.
"""
# Definition for singly-linked list.

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2
    def addLists(self, l1, l2):
        current_l1, current_l2 = l1, l2
        head = ListNode(None)
        current = head
        carry = 0
        while current_l1 or current_l2:
            l1_num, l2_num = 0, 0
            if current_l1:
                l1_num = current_l1.val
            if current_l2:
                l2_num = current_l2.val
            current.val = (l1_num + l2_num + carry) % 10
            current.next = ListNode(None)
            carry = (l1_num + l2_num + carry) // 10
            # next node
            if current_l1:
                current_l1 = current_l1.next
            if current_l2:
                current_l2 = current_l2.next
            current = current.next
        # delete tail zeros
        current.val = carry
        last, current = head, head
        while current:
            if current.next is None and current.val == 0:
                last.next = None
            last = current
            current = current.next
        return head

n15 = ListNode(8)
n14 = ListNode(8, n15)
n13 = ListNode(8, n14)
n12 = ListNode(8, n13)
n11 = ListNode(9, n12)

n19 = ListNode(1)
n20 = ListNode(1, n19)
n21 = ListNode(1, n20)
n22 = ListNode(1, n21)
n23 = ListNode(1, n22)

s = Solution()
head2 = s.addLists(n11, n23)
while head2:
    print head2.val,
    print "->",
    head2 = head2.next
print "None"