#!/usr/bin/python 
#-*- coding:utf-8 -*-
from __future__ import division
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

def removeByRatio(head, a, b):
    if head == None or a < 1 or a > b:
        return head
    cur = head
    len = 0
    while cur:
        cur = cur.next
        len += 1
    print "len = %d" % len
    n = math.ceil(a / b * len) 
    print "n = %d" % n 
    if n == 1:
        return head.next
    cur = head
    while n-1 != 1:
        cur = cur.next
        n -= 1
    cur.next = cur.next.next
    return head
    
#反转单向和双向链表
def reverseList(head):
    if head == None:
        return
    pre = None
    while head != None:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre

def reverseDoubleList(head):
    if head == None:
        return
    pre = None
    while head != None:
        next = head.next
        head.pre = next
        head.next = pre
        pre = head
        head = next
    return pre

#反转部分链表
def reversePart(head, start, end):
    if head == None or head.next == None:
        return head
    fPre = None
    tPos = None
    node1 = head
    len = 0
    while node1 != None: #找出需反转的起始节点的前一个节点，和结束节点的后一个节点
        len += 1
        fPre = node1 if len == start - 1 else fPre
        tPos = node1 if len == end + 1 else tPos
        node1 = node1.next
    if start > end or start < 1 or end > len:
        return head
    node1 = head if fPre == None else fPre.next
    node2 = node1.next
    node1.next = tPos
    next = None
    while node2 != tPos:
        next = node2.next
        node2.next = node1
        node1 = node2
        node2 = next
    if fPre != None:
        fPre.next = node1
        return head
    return node1

#环形单链表的约瑟夫问题
def josephusKill1(head, m):
    if head == None or head.next == None or m < 1:
        return head
    pre = head
    while pre.next != head:
        pre = pre.next
    count = 1
    while head != pre:
        if count != m:
            count += 1
            head = head.next
            pre = pre.next
        else:
            pre.next = head.next
            head = pre.next
            count = 1
    return head

def josephusKill2(head, m):
    def getLive(n, m):
        if n == 1:
            return 1
        return (getLive(n-1, m) + m - 1) % n + 1
    if head == None or head.next == None or m < 1:
        return head
    n = 1
    cur = head
    while cur.next != head:
        n += 1
        cur = cur.next
    n = getLive(n, m)
    while n - 1 != 0:
        n -= 1
        head = head.next
    head.next = head
    return head

#判断一个链表是否为回文结构
def isPalindrome1(head):
    if head == None or head.next == None:
        return True
    cur = head
    stack = []
    while cur != None:
        stack.append(cur)
        cur = cur.next 
    while stack:
        if stack.pop().val != head.val:
            return False
        head = head.next
    return True 

def isPalindrome2(head):
    if head == None or head.next == None:
        return True
    pre = head
    cur = head
    while cur.next != None and cur.next.next != None:
        pre = pre.next
        cur = cur.next.next
    stack = []
    while pre != None:
        stack.append(pre)
        pre = pre.next
    while stack:
        if stack.pop().val != head.val:
            return False
        head = head.next
    return True

def isPalindrome3(head):
    if head == None or head.next == None:
        return True
    pre = head
    cur = head
    while cur.next != None and cur.next.next != None:
        pre = pre.next
        cur = cur.next.next
    node = pre.next
    node_pre = None
    while node != None:
        next = node.next
        node.next = node_pre
        node_pre = node
        node = next
    res = True
    node = node_pre
    while node_pre != None and head != None:
        if node_pre.val != head.val:
            res = False
            break
        node_pre = node_pre.next
        head = head.next
    pre = node.next
    node.next = None
    while pre != None:
        next = pre.next
        pre.next = node
        node = pre
        pre = next
    return res

#将单向链表按某值划分成左边小，中间相等，右边大的形式
def listPartition(head, pivot):
    def partition(nodeArr, pivot):
        left = -1
        right = len(nodeArr)
        index = 0
        while index < right:
            if nodeArr[index].val < pivot:
                left += 1
                nodeArr[left], nodeArr[index] = nodeArr[index], nodeArr[left]
                index += 1
            elif nodeArr[index].val == pivot:
                index += 1
            else:
                right -= 1
                nodeArr[index], nodeArr[right] = nodeArr[right], nodeArr[index]

    if head == None or head.next == None:
        return head
    cur = head
    n = 0
    while cur != None:
        n += 1
        cur = cur.next
    nodeArr = []
    cur = head
    while cur != None:
        nodeArr.append(cur)
        cur = cur.next
    partition(nodeArr, pivot)
    for i in range(n - 1):
        nodeArr[i].next = nodeArr[i + 1]
    nodeArr[-1].next = None
    return nodeArr[0]

if __name__ == '__main__':
    arr1 = [1,3,4,3,1]
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
    # head = removeMidNode(t2)
    # head = removeByRatio(t2, 2, 5)
    # head = reverseList(t2)
    # head = reversePart(t2, 2, 4)
    # test2.next = t2
    # head = josephusKill1(t2, 2)
    # head = josephusKill2(t2, 2)
    # print isPalindrome1(t1)
    # print isPalindrome2(t1)
    # print isPalindrome3(t1)
    head = listPartition(t1, 3)
    while head != None:
        print(head.val)
        head = head.next




