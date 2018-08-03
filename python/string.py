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

#判断两个字符串是否互为旋转词
def is_Rotation(str1, str2):
    if str1 == None or str2 == None or len(str1) != len(str2):
        return False
    str3 = str1 + str1
    if str2 in str3:
        return True
    else: 
        return False

#利用KMP算法匹配
def is_Rotation_KMP(str1, str2):
    def KMP(str1, str2):
        if str1 == None or str2 == None or len(str2) == 1 or len(str1) < len(str2):
            return False
        next = getNextArray(str2)
        si = 0 
        mi = 0
        while si < len(str1) and mi < len(str2):
            if str1[si] == str2[mi]:
                si += 1
                mi += 1
            elif next[mi] == -1:
                si += 1
            else:
                mi = next[mi]
        return True if mi == len(str2) else False

    def getNextArray(str1):
        if len(str1) == 1:
            return [-1]
        next = [0 for i in range(len(str1))]
        next[0] = -1
        next[1] = 0
        pos = 2
        cn = 0
        while pos < len(str1):
            if str1[pos-1] == str1[cn]:
                next[pos] = cn + 1
                pos += 1
                cn += 1
            elif cn > 0:
                cn = next[cn]
            else:
                next[pos] = 0
                pos += 1
        return next

    if str1 == None or str2 == None or len(str1) != len(str2):
        return False
    str3 = str1 * 2
    return KMP(str3, str2)


#将整数字符串转成整数型
def convert(str):
    def isValid(str1):
        if str[0] != '-' and  (ord(str[0]) < ord('0') or ord(str[0]) > ord('9')):
            return False
        if str[0] == '-' and (len(str) == 1 or str[1] == '0'):
            return False
        if str[0] == '0' and len(str) > 1:
            return False
        for i in range(1, len(str)):
            if ord(str[i]) < ord('0') or ord(str[i]) > ord('9'):
                return False
        return True

    '''
    先判断字符串是否符合书写规范
    '''
    if str == None or str == "":
        return 0
    if not isValid(str):
        return 0
    
    '''
    再将字符串转换为整数型
    '''
    posi = False if str[0] == '-' else True
    minq = (-1 << 31) / 10 + 1  #python2.7 和 C++表现不一致，这样是为了保证余数为负数
    minr = (-1 << 31) % 10 - 10
#     print ("minq = %d, minr = %d\n" % (minq, minr))
    res = 0
    cur = 0
    for i in range(0 if posi else 1, len(str)):
        cur = ord('0') - ord(str[i])    #-2^31的绝对值比2^31-1大，采用负数来比较是否溢出 
        if res < minq or (res == minq and cur < minr):
            return 0 
        # print ("res = %d, cur = %d\n" % (res, cur))
        res = res * 10 + cur
    if posi and res == (-1 << 31):  #检查正数是否溢出
        return 0
    return -res if posi else res

def replace(str, fro, to):
    if fro == None or str == None or to == None or str == '' or fro == '':
        return str
    chas = list(str)
    match = 0
    #找到匹配的地方并置换为''
    for i in range(len(str)):
        if chas[i] == fro[match]:
            match += 1
            if(match == len(fro)):
                index = i
                while match > 0:
                    chas[index] = ''
                    index -= 1
                    match -= 1
        else:
            match = 0
            if chas[i] == fro[0]:   #如果相等，从当前字符重新匹配
                match += 1
    # print chas
    cur = ''
    res = '' 
    for i in range(len(str)):
        if chas[i] != '':
            cur = cur + chas[i]
        else:
            if i == 0 or chas[i-1] != '':
                res = res + cur + to
                cur = ''
        # print res
    if cur != '':
        res += cur
    return res

#判断字符数组中是否所有的字符只出现了一次
#时间复杂度O(N)的算法
def isUnique(str):
    if str == None or len(str) == 0:
        return True
    map = {}
    for i in range(len(str)):
        if str[i] in map:
            return False
        else:
            map[str[i]] = 1 
    return True


if __name__ == '__main__':
#    print(isDeformation1("132", "123"))
#    print(isDeformation2("abccd", "ccdba"))
#    print(numSum("123BB---58A33"))
#    print(removeKZores("000ABC000a000ABC",3))
#    print(is_Rotation("abcd", "cdab"))
#    print(is_Rotation_KMP("abcd", "cdab"))
#    print(convert("2147483647"))
    # print(replace("abcbcebcf", "bc", "123"))
    print isUnique("bacd")