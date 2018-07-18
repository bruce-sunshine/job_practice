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

def select_sort(array):
    for i in range(0, len(array)-1):
        min = i
        for j in range(i+1, len(array)):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]

def insert_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1        
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key    


def shell_sort(array):
    step = len(array) / 2
    while step > 0:
        for i in range(step, len(array)):
            key = array[i]
            j = i
            while j > 0 and key < array[j - step]:
                array[j] = array[j-step]
                j -= step 
            array[j] = key
        step = step / 2
        


def merge(a, b):
    c=[]
    i = j = 0
    while i<len(a) and j<len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i == len(a):
        for k in b[j:]:
            c.append(k)
    if j == len(b):
        for n in a[i:]:
            c.append(n)
    return c        

def merge_sort(array):
    if len(array) <= 1:
        return array
    middle = len(array) / 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    return merge(left, right)

def max_Heapify(array, i, N):
    child = 2 * i + 1 
    tmp = array[i]
    while child < N:
        if child < N-1 and array[child] < array[child+1]:
            child += 1
        if tmp < array[child]:
            array[i] = array[child]
            i = child
        else:
            break
        child = child * 2 + 1
    array[i] = tmp

def heap_sort(array):
    N = len(array)
    for i in range((N-2) // 2, -1, -1):
        max_Heapify(array, i, N)
    for i in range(N-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        max_Heapify(array, 0, i)


if __name__ == '__main__':
    array = [100,88,120,66,180,68,168,888,666,999]
#    print bubbleSort(array)
#    quick_sort(array, 0, len(array)-1 )
#    select_sort(array)
#    insert_sort(array)
#    print merge_sort(array)
#    shell_sort(array)
    heap_sort(array)
    print array

