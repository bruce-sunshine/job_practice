#!/usr/bin/python 
#-*- coding:utf-8 -*-

import math
import random

class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class DoubleNode:
    def __init__(self, val = None):
        self.val = val
        self.pre = None
        self.next = None

#打印两个有序链表的公共部分
def printCommonPart(head1, head2):
    if head1 == None or head2 == None:
        return
    print("Two List common part is:")
    while head1 != None and head1 != None:
        if head1.val > head2.val:
            head2 = head2.next
        elif head1.val < head2.val:
            head1 = head1.next
        else:
            print(head1.val)
            head1 = head1.next
            head2 = head2.next

#在单链表中删除倒数第K个节点
def removeLastKthNode(head, k):
    if head == None or k < 1:
        return head
    cur = head
    while cur != None:
        k -= 1
        cur = cur.next
    if k == 0:
        return head.next
    if k < 0:
        cur = head
        while k + 1 != 0:
            cur = cur.next
            k += 1
        cur.next = cur.next.next
    return head

#删除链表中间节点
def removeMidNode(head):
    if head == None or head.next == None:
        return head
    if head.next.next == None:
        return head.next
    pre = head
    cur = head.next.next
    while cur.next != None and cur.next.next != None:
        pre = pre.next
        cur = cur.next.next
    pre.next = pre.next.next
    return head



if __name__ == '__main__':
    arr1 = [1,3,4,5,7]
    arr2 = [3,4,5,6,8]
    test1 = Node()
    t1 = test1
    test2 = Node()
    t2 = test2
    for i in range(len(arr1)):
        test1.val = arr1[i]
        test2.val = arr2[i]
        if i < len(arr1)-1:
            test1.next = Node()
            test2.next = Node()
            test1 = test1.next
            test2 = test2.next
    # printCommonPart(t1, t2)
    # print "After remove Last 2th Node, is "
    # head =  removeLastKthNode(t1, 2)
    head = removeMidNode(t2)
    while head != None:
        print(head.val)
        head = head.next




