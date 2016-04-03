# -*- coding: utf-8 -*-
__author__ = 'yunge008'
"""
Given a linked list, determine if it has a cycle in it.

Example
Given -21->10->4->5, tail connects to node index 1, return true

Challenge
Can you solve it without using extra space?
"""

import os
import sys

sys.path.append(os.getcwd())
from buildlist import *


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The first node of the linked list.
    @return: True if it has a cycle, or false
    """

    def hasCycle(self, head):
        index_1 = head
        index_2 = head
        if not index_2:
            return False
        else:
            while bool(index_1) & bool(index_2):
                index_1 = index_1.next
                if index_2.next:
                    index_2 = index_2.next.next
                    if index_2 == index_1:
                        return True
        return False

s_test = '3 -> null'
head2 = buildList(s_test)['node0']
node2 = head2

print head2.val
while head2.next:
    print "->",
    print head2.val
    head2 = head2.next
print len(buildList(s_test))

s = Solution()
print s.hasCycle(node2)
