# -*- coding: utf-8 -*-
__author__ = 'yunge008'
"""
Reverse a linked list.
"""


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list.
                  Reverse it in-place.
    """

    def reverse(self, head):
        perious = None
        current = head
        while current:
            nxt = current.next
            current.next = perious
            perious = current
            current = nxt
        return perious


n16 = ListNode(2)
n15 = ListNode(5, n16)
n11 = ListNode(2, n15)
n8 = ListNode(3, n11)
n3 = ListNode(4, n8)
n1 = ListNode(1, n3)

s = Solution()
head2 = s.reverse(n1)
while head2:
    print head2.val,
    print "->",
    head2 = head2.next
print "None"