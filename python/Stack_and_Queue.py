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

if __name__ == "__main__":
    stack = NewStack()
    stack.push(123)
    stack.push(456)
    stack.push(789)
    print (stack.getMin())
    print (stack.pop())
        