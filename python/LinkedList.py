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


def addList1(head1, head2):
    if head1 == None or head2 == None:
        raise Exception("Input error!")
    s1 = []
    s2 = []
    while head1 != None:
        s1.append(head1.val)
        head1 = head1.next
    while head2 != None:
        s2.append(head2.val)
        head2 = head2.next
    carry = 0
    pre = None
    while s1 or s2:
        num1 = 0 if not s1 else s1.pop()
        num2 = 0 if not s2 else s2.pop()
        sum = num1 + num2 + carry
        node = Node(sum % 10)
        node.next = pre
        pre = node
        carry = sum // 10
    if carry == 1:
        node = Node(1)
        node.next = pre
        pre = node
    return pre


def addList2(head1, head2):
    if head1 == None or head2 == None:
        raise Exception("Input Error!")
    head1 = reverseList(head1)
    head2 = reverseList(head2)
    pre1 = head1
    pre2 = head2
    pre = None
    carry = 0
    while pre1 != None or pre2 != None:
        sum = pre1.val + pre2.val + carry
        node = Node(sum % 10)
        node.next = pre
        pre = node
        carry = sum // 10
        pre1 = pre1.next
        pre2 = pre2.next
    if carry == 1:
        node = Node(1)
        node.next = pre
        pre = node
    reverseList(head1)
    reverseList(head2)
    return pre


#删除无序单链表中值重复出现的节点
def removeRepeatNode(head):
    if head == None or head.next == None:
        return head
    hashSet = set()
    pre = head
    cur = head.next
    hashSet.add(head.val)
    while cur != None:
        next = cur.next
        if cur.val not in hashSet:
            hashSet.add(cur.val)
            pre = cur
        else:
            pre.next = next
        cur = next

#单链表的选择排序
def selectionSort(head):
    def getSmallestPre(head):
        if head == None:
            return None
        pre = head
        smallest = head
        smallPre = None
        head = head.next
        while head != None:
            if head.val < smallest.val:
                smallest = head
                smallPre = pre
            pre = head
            head = head.next
        return smallPre
    
    if head == None or head.next == None:
        return head
    tail = None
    newHead = None
    cur = head
    small = None
    while cur != None:
        smallPre = getSmallestPre(cur) #获取最小节点的前一个节点，方便删除节点
        if smallPre != None:
            small = smallPre.next
            smallPre.next = small.next
        else:
            small = cur
            cur = cur.next
        if tail == None:
            tail = small
            newHead = tail
        else:
            tail.next = small
            tail = small
    return newHead

#向有环的环形链表中插入新节点
def inSertNum(head, num):
    node = Node(num)
    if head == None:
        node.next = node
        return node
    pre = head
    cur = head.next
    while cur != head:
        if pre.val < num and num < cur.val:
            break
        pre = cur
        cur = cur.next
    pre.next = node
    node.next = cur
    return head if head.val < num else node

#合并两个有序的单链表
def mergeTwoLinks(head1, head2):
    if head1 == None or head2 == None:
        return head1 if head2 == None else head2
    cur1 = head1
    cur2 = head2
    head = head1 if head1.val < head2.val else head2
    pre = None
    while cur1 != None and cur2 != None:
        if cur1.val <= cur2.val:
            if pre == None:
                pre = cur1
            else:
                pre.next = cur1
                pre = cur1
            cur1 = cur1.next
        else:
            if pre == None:
                pre = cur2
            else:
                pre.next = cur2
                pre = cur2
            cur2 = cur2.next
    if cur1 != None:
        pre.next = cur1
    if cur2 != None:
        pre.next = cur2
    return head

#按照左右半区的方式重新组合单链表
def reCombination(head):
    if head == None or head.next == None:
        return head
    mid = head
    right = head.next
    while right != None and right.next.next != None:
        mid = mid.next
        right = right.next.next
    right = mid.next
    mid.next = None
    cur = head
    while cur.next != None:
        right_next = right.next
        right.next = cur.next
        cur.next = right
        cur = right.next
        right = right_next
    cur.next = right
    return head

if __name__ == '__main__':
    arr1 = [1,3,5,7,9]
    arr2 = [2,4,6,8,10]
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
    # head = listPartition(t1, 3)
    # head = addList2(t1, t2)
    # removeRepeatNode(t1)
    # head = t1
    # head = selectionSort(t1)
    # test2.next = t2
    # head = inSertNum(t2, 7)
    # head = mergeTwoLinks(t1, t2)
    head = reCombination(t2)
    while head != None:
        print(head.val)
        head = head.next




