#!/usr/bin/python
#-*- coding:utf-8 -*-

def bubbleSort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if(array[j]>array[j+1]):
                array[j], array[j+1] = array[j+1], array[j] 
    return array

if __name__ == '__main__':
    array = [100,88,120,66,180,68,168,888,666,999]
    print bubbleSort(array)
