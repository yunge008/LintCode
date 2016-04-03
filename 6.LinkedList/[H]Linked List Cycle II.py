# -*- coding: utf-8 -*-
__author__ = 'yunge008'
'''
Given a linked list, return the node where the cycle begins.
If there is no cycle, return null.

Example
Given -21->10->4->5, tail connects to node index 1，return 10

Challenge
Can you solve it without using extra space?
'''

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

    def detectCycle(self, head):
        if head:
            node_set = set()
            current = head
            count = 0
            while current:
                node_set.add(current)
                print current.val + ' -> ',
                if len(node_set) == count:
                    print
                    return current.val
                count = len(node_set)
                current = current.next
        return None


s_test1 = '-21->10->17->8->4->26->5->35->33->-7->-16->27->-12->6->29->-12->5->9->20->14->14->2->13->-24->21->23->-21->5'
s_test2 = '0 -> null'
s_test3 = 'null'
s_test4 = '0->1->2->3->4'
node_dict = buildList(s_test3, -1)
if not node_dict:
    head2 = None
else:
    head2 = node_dict['node0']
node2 = head2
print 'Count of the linked list is: ' + str(len(node_dict))
s = Solution()
print s.detectCycle(node2)
