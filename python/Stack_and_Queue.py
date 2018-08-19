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
    print sortByStack([4, 3, 2, 1, 5, 6])
    
        