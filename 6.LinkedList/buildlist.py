# -*- coding: utf-8 -*-
__author__ = 'yunge008'


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def buildList(node_string, index):
    s_list = node_string.replace(' ', '').split("->")
    if s_list[0] == 'null':
        node_dic = {}
    elif s_list[-1] != 'null' and index != -1:
        node_dic = {('node' + str(len(s_list) - 1)): ListNode(s_list[-1])}
        for i in range(len(s_list) - 2, -1, -1):
            node_dic['node' + str(i)] = ListNode(s_list[i], node_dic['node' + str(i + 1)])
        node_dic['node' + str(len(s_list) - 1)].next = node_dic['node' + str(index)]
    else:
        node_dic = {('node' + str(len(s_list) - 2)): ListNode(s_list[-2])}
        for i in range(len(s_list) - 3, -1, -1):
            node_dic['node' + str(i)] = ListNode(s_list[i], node_dic['node' + str(i + 1)])
        node_dic['node' + str(len(s_list) - 2)].next = None
    return node_dic


# s_test = '1 -> 2'
# s_test4 = '0->1->2->3->4'
# head2 = buildList(s_test, 1)['node0']
# while head2:
#     print head2.val,
#     print "->",
#     head2 = head2.next
