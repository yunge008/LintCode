# -*- coding: utf-8 -*-
__author__ = 'yunge008'
"""
Remove Nth Node From End of List
Given a linked list, remove the nth node from the end of list and return its head.


Notice
The minimum number of nodes in list is n.

Challenge
O(n) time

Example
Given linked list: 1->2->3->4->5->null, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5->null.
"""

"""
Definition of ListNode
"""


class ListNode(object):
    def __init__(self, val, next2=None):
        self.val = val
        self.next = next2


class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """

    def removeNthFromEnd(self, head, n):
        if head.next:
            noOfNode = 1
            cur_node = head
            while cur_node.next:
                cur_node = cur_node.next
                noOfNode += 1
            dummy_i = 1
            cur_node = head
            if noOfNode - n == 0:
                head = cur_node.next
            else:
                while noOfNode - n > dummy_i:
                    cur_node = cur_node.next
                    dummy_i += 1
                cur_node.next = cur_node.next.next
            return head
        return None


s = Solution()
n5 = ListNode(5)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
head1 = n4

head2 = s.removeNthFromEnd(head1, 2)
while head2:
    print head2.val
    head2 = head2.next
