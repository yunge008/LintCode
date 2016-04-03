# -*- coding: utf-8 -*-
__author__ = 'yunge008'
"""
Given a list, rotate the list to the right by k places, where k is non-negative.

Example
Given 1->2->3->4->5 and k = 2, return 4->5->1->2->3.

    def rotateRight(self, head, k):
        current = head
        dummy_i = 0
        if head and head.next:
            while current.next:
                current = current.next
                if dummy_i == k - 1:
                    tail = current
                dummy_i += 1
            current.next = head
            return_head = tail.next
            tail.next = None
        else:
            return_head = head
        return return_head
"""


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    # @param head: the list
    # @param k: rotate to the right k places
    # @return: the list after rotation
    def rotateRight(self, head, k):
        current = head
        next_head = head
        last = head
        if current and k:
            nodes = 0
            while current:
                nodes += 1
                current = current.next
            k %= nodes
            current = head
            if nodes >= 2:
                for i in xrange(k):
                    current = current.next
                if current:
                    while current.next:
                        current = current.next
                        last = last.next
                current.next = head
                next_head = last.next
                last.next = None
        return next_head




n16 = ListNode(2)

n15 = ListNode(1)
n11 = ListNode(2, n15)
n8 = ListNode(3, n11)
n3 = ListNode(2, n8)
n1 = ListNode(1, n3)

s = Solution()
head2 = s.rotateRight(n1, 1)
while head2:
    print head2.val,
    print "->",
    head2 = head2.next
print "None"
