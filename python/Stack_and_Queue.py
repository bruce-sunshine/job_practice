#!/usr/bin/python
#-*- coding:utf-8 -*-

class NewStack:
    def __init__(self):
        self.stackData = []
        self.stackMin = []
    
    def push(self, newNum):
        self.stackData.append(newNum)
        if len(self.stackMin) == 0 or newNum <= self.getMin():
            self.stackMin.append(newNum)

    def pop(self):
        if len(self.stackData) == 0:
            raise Exception("stack is empty")
        value = self.stackData.pop()
        if value == self.getMin():
            self.stackMin.pop()
        return value

    def getMin(self):
        if len(self.stackMin) == 0:
            raise Exception("stack is empty")
        return self.stackMin[-1]


#两个栈组成队列
class TwoStackQueue:
    stackPush = []
    stackPop = []

    def add(self, newNum):
        self.stackPush.append(newNum)
    
    def poll(self):
        if not self.stackPush and not self.stackPop:
            raise Exception("Queue is empty!")
        elif not self.stackPop:
            while self.stackPush:
                self.stackPop.append(self.stackPush.pop())
        return self.stackPop.pop()

    def peek(self):
        if not self.stackPush and not self.stackPop:
            raise Exception("Queue is empty!")
        elif not self.stackPop:
            while self.stackPush:
                self.stackPop.append(self.stackPush.pop())
        return self.stackPop[-1]

#如何仅用递归函数和栈操作逆序一个栈
def reverse(stack):
    def getAndRemoveLast(stack):
        result = stack.pop()
        if len(stack) == 0:
            return result
        else:
            i = getAndRemoveLast(stack)
            stack.append(result)
            return i
    
    if len(stack) == 0:
        return 
    i = getAndRemoveLast(stack)
    reverse(stack)
    stack.append(i)
    return stack

#用一个栈实现另一个栈的排序
def sortByStack(stack):
    if len(stack) < 2:
        return stack
    help_stack = []
    while stack:
        cur = stack.pop()
        if len(help_stack) == 0 or help_stack[-1] >= cur:
            help_stack.append(cur)
        else:
            while help_stack:
                stack.append(help_stack.pop())
            help_stack.append(cur)
    while help_stack:
        stack.append(help_stack.pop())
    return stack

def getMaxWindow(arr, w):
    if len(arr) == 0 or w < 1 or len(arr) < w:
        return
    deq = []
    res = []
    for i in range(len(arr)):
        while(deq and arr[deq[-1]] <= arr[i]): #note here, deq store index, not value of arr
            deq.pop()
        deq.append(i)
        if deq[-1] == i - w:
            deq.pop(0)
        if i >= w-1:
            res.append(arr[deq[0]])
    return res

#求最大子矩阵的大小
def maxRecsize(map):
    def maxRecFromBottom(height):
        if height == None or len(height) == 0:
            return 0
        stack = []
        maxArea = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] >= height[i]:
                j = stack.pop()
                k = stack[-1] if stack else -1
                maxArea = max(maxArea, (j-k+1)*height[j])
            stack.append(i)
        while stack:
            j = stack.pop()
            k = stack[-1] if stack else -1
            maxArea = max(maxArea, (j-k+1)*height[j])
        return maxArea
    
    if map == None or len(map) == 0 or len(map[0]) == 0:
        return 0
    height = [0 for i in range(len(map[0]))]
    print "len of map = %d" % len(map)
    maxArea = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            height[j] = 0 if map[i][j] == 0 else height[j] + 1
        maxArea = max(maxArea, maxRecFromBottom(height))
    return maxArea


if __name__ == "__main__":
    # stack = NewStack()
    # stack.push(123)
    # stack.push(456)
    # stack.push(789)
    # print (stack.getMin())
    # print (stack.pop())
    # queue = TwoStackQueue()
    # queue.add(123)
    # queue.add(456)
    # print (queue.peek())
    # print (queue.poll())
    # print (queue.peek())
    # print (queue.poll())
    # print (reverse([1, 2, 3, 4, 5]))
    # print sortByStack([4, 3, 2, 1, 5, 6])
    # print getMaxWindow([4, 3, 5, 4, 3, 3, 6, 7], 3)
    print(maxRecsize([[1,0,1,1], [1,1,1,1], [1,1,1,0]]))
    
        