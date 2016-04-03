# -*- coding: utf-8 -*-
__author__ = 'yunge008'
"""
Given a linked list and a value x, partition it such that all nodes less than x come before
nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Example,
Given 1->4->3->2->5->2->null and x = 3,
return 1->2->2->4->3->5->null.
"""

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of linked list.
    @param x: an integer
    @return: a ListNode
    """
    def partition(self, head, x):
        dummy_node = head
        p_less = ListNode(0)
        p_more = ListNode(0)
        p_more_backup = p_more
        return_node = p_less
        numberOfNode = 0
        while dummy_node:
            numberOfNode += 1
            if dummy_node.val < x:
                p_less.next = dummy_node
                p_less = p_less.next
            else:
                p_more.next = dummy_node
                p_more = p_more.next
            dummy_node = dummy_node.next
        p_less.next = p_more_backup.next
        p_more.next = None
        return return_node.next

n16 = ListNode(2)
n15 = ListNode(5, n16)
n11 = ListNode(2, n15)
n8 = ListNode(3, n11)
n3 = ListNode(4, n8)
n1 = ListNode(1, n3)

n5 = ListNode(880)
n4 = ListNode(150, n5)
n2 = ListNode(110, n4)

s = Solution()
head2 = s.partition(n1, 3)
while head2:
    print head2.val,
    print "->",
    head2 = head2.next
print "None"
