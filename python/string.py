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

#字符串中数字子串的求和
def numSum(str):
    if str == None or len(str) == 0:
        return 0
    ''' res为累加和，num为当前收集到的数字，posi表示num的正负性'''
    res = 0
    num = 0
    cur = 0
    posi = True
    for i in range(len(str)):
        cur = ord(str[i]) - ord('0')
        if cur < 0 or cur > 9:
            res += num
            num = 0
            if str[i] == '-':
                if i - 1 >= 0  and str[i-1] == '-':
                    posi = True
                else:
                    posi = False
            else:
                posi = True
        else:
            num = num * 10 + (cur if posi else -cur)    #note here, python2.7 must add () here, otherwise it went wrong
    '''最后一个数字字符要累加进去'''
    res += num
    return res

#去掉字符串中连续出现的K个0的子串
def removeKZores(str, k):
    if str == None or k < 1:
        return str
    start = -1
    count = 0
    str1 = list(str)    #python里的字符串是不可变的
    for i in range(len(str1)):
        if str[i] == '0':
            if start == -1:
                start = i
            count += 1
        else:
            if count == k:
                while count > 0:
                    str1[start] = ''
                    start += 1
                    count -= 1
            start = -1
            count = 0
    if count == k:
        while count > 0:
            str1[start] = ''
            start += 1
            count -= 1
    return ''.join(str1)



if __name__ == '__main__':
#    print(isDeformation1("132", "123"))
#    print(isDeformation2("abccd", "ccdba"))
#    print(numSum("123BB---58A33"))
    print(removeKZores("000ABC000a000ABC",3))