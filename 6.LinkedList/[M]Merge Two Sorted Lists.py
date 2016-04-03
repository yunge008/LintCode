# -*- coding: utf-8 -*-
__author__ = 'yunge008'

"""
Merge two sorted (ascending) linked lists and return it as a new sorted list.
The new sorted list should be made by splicing together the nodes of the two lists
and sorted in ascending order.

Example
Given 1->3->8->11->15->null, 2->null , return 1->2->3->8->11->15->null.

Definition of ListNode
"""


class ListNode(object):
    def __init__(self, val, next2=None):
        self.val = val
        self.next = next2


class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """

    def mergeTwoLists(self, l1, l2):
        return_node = ListNode(0)
        dummy_node = return_node
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                dummy_node.next = l1
                l1 = l1.next
            else:
                dummy_node.next = l2
                l2 = l2.next
            dummy_node = dummy_node.next
        if l1 is not None:
            dummy_node.next = l1
        if l2 is not None:
            dummy_node.next = l2
        return return_node.next


n15 = ListNode(15)
n11 = ListNode(11, n15)
n8 = ListNode(8, n11)
n3 = ListNode(3, n8)
n1 = ListNode(1, n3)

n5 = ListNode(880)
n4 = ListNode(150, n5)
n2 = ListNode(110, n4)

s = Solution()
head2 = s.mergeTwoLists(n1, n2)
while head2:
    print head2.val,
    print "->",
    head2 = head2.next
print "None"
