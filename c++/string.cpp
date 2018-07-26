#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

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


int main()
{
    // string str1 = "abccde";
    // string str2 = "ccedba";
    // cout << "str1 and str2 is Deformation ? " << (isDeformation(str1, str2)? "true" : "false") << endl;
    string str = "123BB-58A33";
    cout << "str numSum is " << numSum(str) <<endl;
    system("pause");
}
