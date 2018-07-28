#include <iostream>
#include <string>
#include <vector>
#include <map>
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

int main()
{
    // string str1 = "abccde";
    // string str2 = "ccedba";
    // cout << "str1 and str2 is Deformation ? " << (isDeformation(str1, str2)? "true" : "false") << endl;
    string str=removeKZore("000ABC000a000ABC",3);
    cout << "str is " << str <<endl;
    system("pause");
}
