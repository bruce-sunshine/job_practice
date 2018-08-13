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

#在有序但含有空的数组中查找字符串,返回str1在strlist中出现最左的位置
def getIndex(strlist, str1):
    if strlist == None or str1 == None or len(strlist) == 0:
        return -1
    res = -1
    left = 0
    right = len(strlist) - 1
    while left <= right:
        mid = (left + right) // 2
        if strlist[mid] == str1:
            res = mid
            right = mid -1
        elif strlist[mid] != None:
            if strlist[mid] < str1:
                left = mid + 1
            else:
                right = mid -1
        else:
            i = mid
            while strlist[i] == None and i >= left:
                i = i - 1
            if strlist[i] < str1:
                left = mid + 1
            else:
                res = i if strlist[i] == str1 else res
                right = i -1
    return res
            
def rotate(str, size):
    if str == None or len(str) == 0 or size < 0 or size > len(str):
        return
    def reverse(chas, start, end):
        while start < end:
            chas[start], chas[end]= chas[end], chas[start]
            start += 1
            end -= 1
    chas = list(str)
    reverse(chas, 0, size - 1)
    reverse(chas, size, len(chas) - 1)
    reverse(chas, 0, len(chas) - 1)
    return chas

#数组中两个字符串的最小值
def minDistance(strlist, str1, str2):
    if strlist == None or str1 == None or str2 == None:
        return -1
    if str1 == str2:
        return 0
    last1 = -1
    last2 = -1
    mindistance = sys.maxsize
    print minDistance
    for i in range(len(strlist)):
        if strlist[i] == str1:
            if last2 != -1:
                dist = i - last2
                mindistance = min(mindistance, dist)
            last1 = i
        if strlist[i] == str2:
            if last1 != -1:
                dist = i - last1
                mindistance = min(mindistance, dist)
            last2 = i
    return mindistance if mindistance != sys.maxsize else -1

def getPalindrome_1(str):
    def getdp(str):
        dp = [[0 for i in range(len(str))] for j in range(len(str))]
        for j in range(1, len(str)):
            dp[j-1][j] = 0 if str[j-1] == str[j] else 1
            for i in range(j-2, -1, -1):
                if str[i] == str[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
        return dp
    
    if str == None or len(str) < 2:
        return str
    dp = getdp(str)
    res = [0 for i in range(len(str) + dp[0][len(str)-1])]
    i = 0
    j = len(str) -1
    resl = 0
    resr = len(res) - 1
    while i <= j:
        if str[i] == str[j]:
            res[resl] = str[i]
            res[resr] = str[j]
            i += 1
            j -= 1
        elif dp[i+1][j] < dp[i][j-1]:
            res[resl] = str[i]
            res[resr] = str[i]
            i += 1
        else:
            res[resl] = str[j]
            res[resr] = str[j]
            j -= 1
        resl += 1
        resr -= 1
    return ''.join(res)

def getPalindrome_2(str, strlps):
    if str == None or len(str) == 0 or strlps == None or len(strlps) == 0:
        return 
    
    res = [""  for i in range(2 * len(str) - len(strlps))]
    lstr = 0
    rstr = len(str) - 1
    llps = 0
    rlps = len(strlps) - 1
    lres = 0
    rres = len(res) - 1

    while llps <= rlps:
        temp1 = lstr
        temp2 = rstr
        while str[lstr] != strlps[llps]:
            lstr += 1
        while str[rstr] != strlps[rlps]:
            rstr -= 1       
        for i in range(temp1, lstr):
            res[lres] = str[i]
            res[rres] = str[i]
            lres += 1
            rres -= 1
        for i in range(temp2, rstr, -1):
            res[lres] = str[i]
            res[rres] = str[i]
            lres += 1
            rres -= 1
        res[lres] = str[lstr]
        res[rres] = str[rstr]
        lstr += 1
        rstr -= 1
        lres += 1
        rres -= 1
        llps += 1
        rlps -= 1
    return ''.join(res)
        

def getVaule(exp):
    # 计算乘法和除法
    def addNum(deque, pre):
        if deque:
            top = deque.pop()
            if top == '+' or top == '-':
                deque.append(top)
            else:
                cur = int(deque.pop())
                pre = cur * pre if top == '*' else cur / pre
        deque.append(pre)

    # 计算加法和减法
    def getNum(deque):
        res = 0
        add = True
        while deque:
            cur = deque.pop(0)
            if cur == '+':
                add = True
            elif cur == '-': 
                add = False
            else:
                res += int(cur) if add else -int(cur)
        return res
    
    def value(exp, i):
        deque = []
        pre = 0
        while i < len(exp) and exp[i] != ')':
            if ord(exp[i]) >= ord('0') and ord(exp[i]) <= ord('9'):
                pre = 10 * pre + int(exp[i])
                i += 1
            elif exp[i] != '(':
                addNum(deque, pre)
                deque.append(exp[i])
                i += 1
                pre = 0
            else:
                bra = value(exp, i + 1)
                pre = bra[0]
                i = bra[1] + 1
        addNum(deque, pre)
        return [getNum(deque), i]

    return value(exp, 0)[0]

#拼接所有字符串产生字典顺序最小的大字符串
def lowestString(chas):
    if chas == None or len(chas) == 0:
        return ""
    from functools import cmp_to_key
    chas = sorted(chas, key = cmp_to_key(lambda x,y : 1 if x + y > y + x else -1))
    return ''.join(chas)

#找到字符串的最长无重复字符子串的长度
def maxUniqueStr(str):
    if str == None or len(str) == 0:
        return 0
    map = {}
    pre = -1
    length = 0
    for i in range(len(str)):
        if str[i] in map:
            pre = max(pre, map[str[i]])
        length = max(length, i - pre)
        map[str[i]] = i #记录上一次的index
    return length



def minLength(str1, str2):
    if str1 == None or str2 == None or len(str1) < len(str2):
        return 0   
    map = [ 0 for i in range(256)]
    for i in range(len(str2)):
        map[ord(str2[i])] += 1
    left = 0
    right = 0
    match = len(str2)
    minlength = sys.maxsize
    while right < len(str1):
        map[ord(str1[right])] -= 1
        if map[ord(str1[right])] >= 0:
            match -= 1
        if match == 0:
            while map[ord(str1[left])] < 0:
                map[ord(str1[left])] += 1
                left += 1       #可以不写?     
            minlength = min(minlength, right - left + 1)
            print "minlength = %d, right= %d, left=%d" % (minlength, right, left)
            match += 1
            map[ord(str1[left])] += 1 #接着向后搜索
            left += 1
        right += 1 
    return minlength if minlength != sys.maxsize else 0


if __name__ == '__main__':
#    print(isDeformation1("132", "123"))
#    print(isDeformation2("abccd", "ccdba"))
#    print(numSum("123BB---58A33"))
#    print(removeKZores("000ABC000a000ABC",3))
#    print(is_Rotation("abcd", "cdab"))
#    print(is_Rotation_KMP("abcd", "cdab"))
#    print(convert("2147483647"))
    # print(replace("abcbcebcf", "bc", "123"))
    # print isUnique("bacd")
    # print(getIndex([None, 'a', None, 'b', 'b', None, 'c'], 'b'))
    # print rotate("abcdefg", 0)
    # print minDistance(["abc", None, None, None, "abc", None, "123", None, "123"],"abc", "123")
    # print getPalindrome_2("A1B21C", "121")
    # print getVaule("50*((10-5)-3)+68*1")
    # print lowestString(["de", "abc", "123"])
    # print maxUniqueStr("abcdacd")
    print minLength("abceeeeeeac", "ac")