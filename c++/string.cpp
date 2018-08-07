#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <math.h>
#include <algorithm>
using namespace std;

//判断两个字符串是否为变形词
bool isDeformation(string str1, string str2)
{
    if(str1.empty() || str2.empty() || str1.size() != str2.size())
    {
        return false;
    }
    vector<int> map(256);
    for(int i=0; i < str1.size(); i++)
        ++map[str1[i]];
    for(int i=0; i < str2.size(); i++)
    {
        --map[str2[i]];
        if(map[str2[i]] < 0)
            return false;
    }
    return true;
}

//字符串中数字子串的求和
int numSum(string str)
{
    if(str.empty() || str.size() == 0)
        return 0;
    int res=0, num=0, cur=0;
    bool posi = true;
    for(int i=0; i < str.size(); i++)
    {
        cur = str[i] - '0';
        if(cur < 0 || cur > 9)
        {
            res += num;
            num = 0;
            if(str[i] == '-')
            {
                if( i - 1 >= 0 && str[i-1] == '-')
                    posi = true;
                else
                    posi = false;
            }
            else
                posi = true;
        }
        else
        {
            num = num * 10 + (posi ? cur : -cur);
        }
    }
    res += num;
    return res;
}

//去掉字符串中连续出现的K个0的子串
string removeKZore(string str, int K)
{
    if(str.empty() || K < 1)
        return str;
    int count =0;
    string new_str;
    for(int i = 0; i < str.size(); i++)
    {
        if(str[i] == '0')
        {
            ++count;
        }
        else
        {
            if(count != K)
                new_str += str.substr(i - count, count+1);
            else
                new_str += str[i];
            count = 0;
        }
    }
    return new_str;
}

string removeKZore_1(string str, int K)
{
    if(str.empty() || K < 1)
        return str;
    int count =0;
	int start = -1;
    for(int i = 0; i < str.size(); i++)
    {
        if(str[i] == '0')
        {
            ++count;
			start = (start == -1 ? i : start);
        }
        else
        {
			if (count == K)
			{
				str.erase(str.begin() + start, str.begin() + start + K);
				if (i < str.size()) //str.erase 后str的len已变，i的值需要重新赋值为0
					i = 0;
			}
			count = 0;
			start = -1;
        }
    }

	if (count == K)
	{
		str.erase(str.begin() + start, str.begin() + start + K);
	}
	return str;
}

//判断两个字符串是否互为旋转词
bool is_Rotation(string str1, string str2)
{
    if(str1.empty() || str2.empty() || str1.size() != str2.size())
        return false;
    string str3 = str1 + str1;
    return str3.find(str2) == string::npos ? false : true;   
}
//利用KMP算法匹配
vector<int> getNextArray(string str)
{
    if(str.size() == 1)
        return vector<int> {-1};
    
    vector<int> next = vector<int>(str.size());
    next[0] = -1;
    next[1] = 0;
    int pos = 2;
    int cn = 0;
    while(pos < next.size())
    {
        if(str[pos -1] == str[cn])
        {
            next[pos++] = ++cn;
        }
        else if(cn > 0){
            cn = next[cn];
        }else{
            next[pos++] = 0;
        }
    }
    return next;
}

int KMP(string str1, string str2)
{
    if(str1.size() < str2.size())
        return -1;
    int si = 0;
    int mi = 0;
    vector<int> next = getNextArray(str2);
    while(si < str1.size() && mi < str2.size())
    {
        if(str1[si] == str2[mi])
        {
            si++;
            mi++;
        }
        else if(next[mi] == -1){
            si++;
        }else{
            mi = next[mi];
        }
    }
    return mi == str2.size() ? si - mi : -1;
}

bool is_Rotation_KMP(string str1, string str2)
{
    if(str1.empty() || str2.empty() || str1.size() != str2.size())
        return false;
    string str3 = str1 + str1;
    return KMP(str3, str2) != -1;
}

bool isValid(string str)
{
    if(str[0] != '-' && (str[0] < '0' || str[0] > '9'))
        return false;
    if(str[0] == '-' && (str.size() == 1 || str[1] =='0'))
        return false;
    if(str[0] == '0' && str.size() > 1)
        return false;
    for(int i = 1; i < str.size(); i++)
        if(str[i] < '0' || str[i] > '9')
            return false;
    return true;
}

int convert(string str)
{
    if(str.empty())
        return 0;
    if(!isValid(str))
        return 0;

    bool posi;
    if(str[0] == '-')
        posi = false;
    else
        posi = true;
    int cur = 0;
    int res = 0;
    int minq = (-1 << 31) / 10; //python2.7 和 C++表现不一致
    int minr = (-1 << 31) % 10;
    for(int i = (posi ? 0 : 1); i < str.size(); i++)
    {
        cur = '0' - str[i];
        if(res < minq || (res == minq && cur < minr))
            return 0;
        res = res * 10 + cur;
    }
    if(posi && res == (-1 << 31))
        return 0;
    
     return posi ? -res : res;
}

string replace(string str, string from, string to)
{
    if(str.empty() || from.empty() || to.empty())
        return str;
    
    int match = 0;
    int index = 0;
    for(int i=0; i < str.size(); i++)
    {
        if(str[i] == from[match++])
        {
            if(match == from.size())
            {
                index = i;
                while(match>0)
                {
                    str[index] = '*';
                    match--;
                    index--; 
                }
            }
        }
        else
        {
            match = 0;
            if(str[i] == from[0])
                match++;
        }
    }

    string cur = "";
    string res = "";
    for(int i = 0; i < str.size(); i++)
    {
        if(str[i] != '*')
            cur = cur + str[i];
        else
        {
            if(i == 0 || str[i-1] != '*')
            {
                res = res + cur + to;
                cur = "";
            }
        }
    }
    res += cur;
    return res;
}

bool isUnique(string str)
{
    if(str.empty())
        return false;
    vector<int>map = vector<int>(256,0);
    for(int i = 0; i < str.size(); i++)
    {
        if(map[str[i]])
            return false;
        else
            map[str[i]] = 1;
    }
    return true;
}

int getIndex(vector<string> strlist, string str1)
{
    if(strlist.empty() || str1.empty())
        return -1;

    int res = -1;
    int left = 0;
    int right = strlist.size() - 1;
    int mid = 0; 
    int i = 0;
    while(left <= right)
    {
        mid = (left + right) / 2;
        if(strlist[mid] == str1)
        {
            res = mid;
            right = mid - 1;
        }
        else if(strlist[mid] != "")
            {
                if(strlist[mid] < str1)
                    left = mid + 1;
                else
                    right = mid - 1;
            }
            else
            {
                i = mid;
                while(strlist[i] == "" && i >= left)
                    i--;
                if(strlist[i] < str1)
                    left = mid + 1;
                else
                {
                    if(strlist[i] == str1)
                        res = i;
                    right = i - 1;    
                }    
            }
    }
    return res;
}

void exchange(string & str, int start, int end, int size)
{
    int i = end - size + 1;
    while(size > 0)
    {
        char temp = str[start];
        str[start] = str[i];
        str[i] = temp;
        ++start;
        ++i;
        --size;
    }
}

string rotate(string str, int size)
{
    if(str.empty() || size < 0 || size > str.size())
        return str;
    
    int start = 0;
    int end = str.size() - 1;
    int lpart = size;
    int rpart = str.size() - size;
    int s = min(lpart, rpart);
    int d = lpart - rpart;

    while(1)
    {
        exchange(str, start, end, s);
        if(d == 0)
            break;
        if(d < 0)
        {
            rpart = -d;
            end -= s;
        }
        else
        {
            lpart = d;
            start += s;
        }
        s = min(lpart, rpart);
        d = lpart - rpart; 
    }
    return str;
}

vector<vector<int>> getDp(string str)
{
    vector<vector<int>> dp(str.size(), vector<int>(str.size()));
    for(int j = 1; j < str.size(); j++)
    {
        dp[j][j-1] = str[j-1] == str[j] ? 0 : 1;
        for(int i = j-2; i > -1; --i)
        {
            if(str[i] == str[j])
                dp[i][j] = dp[i+1][j-1];
            else
                dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1;
        }
    }
    return dp;
}

string getPalindrome_1(string str)
{
    if(str.size() < 2)
        return str;
    vector<vector<int>> dp = getDp(str);
    string res;
    int i = 0; 
    int j = str.size() - 1;
    int resl = 0;
    int resr = str.size() + dp[0][str.size() - 1];
    res.resize(resr + 1);

    while(i <= j)
    {
       if(str[i] == str[j])
       {
           res[resl++] = str[i++];
           res[resr--] = str[j--];
       } 
       else if(dp[i][j-1] < dp[i+1][j])
       {
           res[resl++] = str[j];
           res[resr--] = str[j--];
       }
       else
       {
           res[resl++] = str[i];
           res[resr--] = str[i++];
       }
    }
    return res;
}

int main()
{
    string str = "A1B21C";
    // vector<string> strlist = {"a", "", "b", "", "", "b", "c"};
    // string str1="b";
    // string from = "bc";
    // string to = "123";
    // string str1 = "apple";
    // string str2 = "leapp";
    // cout << "str1 and str2 is Deformation ? " << (isDeformation(str1, str2)? "true" : "false") << endl;
    // string str=removeKZore("000ABC000a000ABC",3);
    // cout << "str is " << str <<endl;
    // cout << "str1 and str2 is_Rotation_KMP ? " << is_Rotation_KMP(str1, str2) << endl;
    // cout << str << " convert str to integrate, "  << convert(str) << endl;
    // cout << str << " replace " << from << " by " << to  << " is " << replace(str, from, to) << endl;
    // cout << str << "isUnique ? " << isUnique(str) << endl;
    // cout << "getindex " << getIndex(strlist, str1) <<endl;
    // cout << str << "rotate is " << rotate(str, 5) << endl;
    cout << str << "getPalindrome is " << getPalindrome_1(str) <<endl;
    system("pause");
}
