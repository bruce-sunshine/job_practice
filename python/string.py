#!/usr/bin/python
#-*- coding=utf-8 -*-

import sys
#判断两个字符串是否为变形词
#使用数组进行判断，前提是假设字符的编码值在0~255之间，即是ASCII编码，那么先申请一个长度为256的整型数组array
def isDeformation1(str1, str2):
    if str1 == None or str2 == None or len(str1) != len(str2):
        return False
    array = [0 for i in range(256)]
 #   print array
    for i in range(len(str1)):
        array[ord(str1[i])] += 1
    for i in range(len(str2)):
        array[ord(str2[i])] -= 1
        if array[ord(str2[i])] < 0:
            return False
    return True

#使用哈希表来判断
def isDeformation2(str1, str2):
    if str1 == None or str2 == None or len(str1) != len(str2):
        return False
    map = {}
    for i in range(len(str1)):
        if str1[i] not in map:
            map[str1[i]] = 1
        else:
             map[str1[i]] =  map[str1[i]] + 1
    for i in range(len(str2)):
        if str2[i] not in map:
            return False
        else:
            map[str2[i]] = map[str2[i]] - 1
            if map[str2[i]] < 0:
                return False
    return True


if __name__ == '__main__':
    print(isDeformation1("132", "123"))
    print(isDeformation2("abccd", "ccdba"))