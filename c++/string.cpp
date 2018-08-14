#include <iostream>
#include <string>
#include <vector>
#include <deque>
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

string getPalindrome_2(string str, string strlps)
{
    if(str.empty())
        return str;
    
    string res;
    res.resize(2 * str.size() - strlps.size());
    int lstr = 0;
    int rstr = str.size() - 1;
    int llps = 0;
    int rlps = strlps.size() - 1;
    int lres = 0;
    int rres = res.size() - 1;
    int temp1, temp2;

    while(llps <= rlps)
    {
        temp1 = lstr;
        temp2 = rstr;
        while(str[lstr] != strlps[llps])
            ++lstr;
        while(str[rstr] != strlps[rlps])
            --rstr;
        for(int i = temp1; i < lstr; i++)
        {
            res[lres++] = str[i];
            res[rres--] = str[i];
        }
        for(int i = temp2; i > rstr; i--)
        {
            res[lres++] = str[i];
            res[rres--] = str[i];
        }
        res[lres] = str[lstr];
        res[rres] = str[rstr];
        ++lstr;
        --rstr;
        ++lres;
        --rres;
        ++llps;
        --rlps;
    }
    return res;
}

//计算乘除法
void addNum(deque<string> &deq, int pre)
{
    int cur;
    if(!deq.empty())
    {
        string top = deq.back();
        
        if(std::stoi(top) == int('*') || std::stoi(top) == int('/'))
        {
			deq.pop_back();
            cur = std::stoi(deq.back());
            deq.pop_back();
            if(std::stoi(top) == int('*'))
                pre = cur * pre;
            else if(std::stoi(top) == int('/'))
                pre = cur / pre;            
        }
    }
    deq.push_back(std::to_string(pre));
}
// 计算加减法
int getNum(deque<string> &deq)
{
    int res = 0;
    bool Add = true;
    string cur;
    while(!deq.empty())
    {
        cur = deq.at(0);
        deq.pop_front();
        if(std::stoi(cur) == int('+'))
            Add = true;
        else if(std::stoi(cur) == int('-'))
            Add = false;
            else
            {
                res += Add ? std::stoi(cur) : -std::stoi(cur);
            }
    }
    return res;
}

vector<int> value(string &exp, int i)
{
    vector<int> bra;
    deque<string> deq;
    int pre = 0;
    while(i < exp.size() && exp[i] != ')')
    {
        if(exp[i] >= '0' && exp[i] <= '9')
        {
            pre = pre * 10 + exp[i] - '0';
            i++;
        }
        else if(exp[i] != '(')
        {
            addNum(deq, pre);
            deq.push_back(to_string(exp[i]));
            i++;
            pre = 0;
        }
        else
        {
            bra = value(exp, i+1);
            pre = bra[0];
            i = bra[1] + 1;
        }
    }
    addNum(deq, pre);
    return vector<int> {getNum(deq), i};
}

int GetValue(string exp)
{
    return value(exp, 0)[0];
}

int minLength(string str1, string str2)
{
    if(str1.empty() || str2.empty() || str1.size() < str2.size())
        return 0;
    vector<int> map(256);
    for(int i = 0 ; i < str2.size(); i++)
    {
        map[str2[i]] += 1; 
    }
    int left = 0;
    int right = 0;
    int match = str2.size();
    int minlength = str1.size();
    while(right < str1.size())
    {
        map[str1[right]] -= 1;
        if(map[str1[right]] >= 0)
            match--;
        if(match == 0)
        {
            while(map[str1[left]] < 0)
            {
                left++;
                map[str1[left]] += 1;
            }
            minlength = min(minlength, right - left + 1);
            match++;
            map[str1[left]] += 1;
            left++;
        }
        right++;
    }
    return minlength == str1.size() ? 0 : minlength;
}

#define maxsize 256
int minCut(string str)
{
    if(str.empty())
        return 0;
    int N = str.size();
    vector<int> dp(N);
	bool array[maxsize][maxsize] = {false};
    for(int i = N - 1; i >= 0; i--)
    {
        dp[i] = maxsize;
        for(int j = i; j < N; j++)
        {
            if(str[i] == str[j] && (j - i < 2 || array[i+1][j-1]))
            {
                array[i][j] = true;
                dp[i] = min(dp[i], j + 1 == N ? 0 : (dp[j + 1] + 1));
            }
        }
    }
    return dp[0];
}

int main()
{
    string str = "A1B21C";
    string strlps = "121";
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
    // cout <<"getPalindrome is " << getPalindrome_2(str, strlps) <<endl;
    // cout << "getValue= " << GetValue("50*((10-5)-3)+68*1") <<endl;
    // cout << "minLength is " << minLength("abceeeeeeac", "ac") << endl;
    cout << "minCut= " << minCut("ACDCDCDAD") << endl;
    system("pause");
}
