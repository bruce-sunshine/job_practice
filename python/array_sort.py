#!/usr/bin/python
#-*- coding:utf-8 -*-

def bubbleSort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if(array[j]>array[j+1]):
                array[j], array[j+1] = array[j+1], array[j] 
    return array

def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while low < high:
        while low < high and array[high] > key:
            high -= 1
        array[low] = array[high]
        while low < high and array[low] <= key:
            low += 1
        array[high] = array[low]
    array[high] = key
    quick_sort(array, 0, low - 1)
    quick_sort(array, low + 1, right)           


if __name__ == '__main__':
    array = [100,88,120,66,180,68,168,888,666,999]
#    print bubbleSort(array)
    quick_sort(array, 0, len(array)-1 )
    print array
