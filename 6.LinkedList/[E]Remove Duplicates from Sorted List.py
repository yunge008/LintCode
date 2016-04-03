# -*- coding: utf-8 -*-
__author__ = 'yunge008'
"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        dummy_node = head
        while dummy_node is not None and dummy_node.next is not None:
            cur_val = dummy_node.val
            next_node = dummy_node.next
            if next_node.val != cur_val:
                dummy_node = dummy_node.next
            else:
                dummy_node.next = dummy_node.next.next
        return head


n15 = ListNode(15)
n112 = ListNode(11, n15)
n11 = ListNode(11, n112)
n8 = ListNode(8, n11)
n3 = ListNode(3, n8)
n1 = ListNode(1, n3)

s = Solution()
head2 = s.deleteDuplicates(n1)
while head2:
    print head2.val,
    print "->",
    head2 = head2.next
print "None"
