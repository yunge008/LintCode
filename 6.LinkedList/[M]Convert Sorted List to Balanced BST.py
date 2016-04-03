# -*- coding: utf-8 -*-
__author__ = 'yunge008'
"""
Given a singly linked list where elements are sorted in ascending order,
convert it to a height balanced BST.

               2
1->2->3  =>   / \
             1   3
"""


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        # write your code here
        pass


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
head2 = s.sortedListToBST(n11)
while head2:
    print head2.val,
    print "->",
    head2 = head2.next
print "None"
