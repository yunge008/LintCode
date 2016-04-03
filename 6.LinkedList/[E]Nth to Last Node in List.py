# -*- coding: utf-8 -*-
__author__ = 'yunge008'
"""
Find the nth to last element of a singly linked list.
The minimum number of nodes in list is n.

Example
Given a List  3->2->1->5->null and n = 2, return node  whose value is 1.
"""


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: Nth to last node of a singly linked list.
    """

    def nthToLast(self, head, n):
        current = head
        return_node = head
        for i in xrange(n - 1):
            current = current.next
        if current:
            while current.next:
                current = current.next
                return_node = return_node.next
        return return_node


n15 = ListNode(5)
n14 = ListNode(6, n15)
n13 = ListNode(7, n14)
n12 = ListNode(8, n13)
n11 = ListNode(9, n12)

n19 = ListNode(1)
n20 = ListNode(1, n19)
n21 = ListNode(1, n20)
n22 = ListNode(1, n21)
n23 = ListNode(1, n22)

s = Solution()
head2 = s.nthToLast(n11, 0)
while head2:
    print head2.val,
    print "->",
    head2 = head2.next
print "None"
