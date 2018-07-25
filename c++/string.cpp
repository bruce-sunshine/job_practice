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

int main()
{
    string str1 = "abccde";
    string str2 = "ccedba";
    cout << "str1 and str2 is Deformation ? " << (isDeformation(str1, str2)? "true" : "false") << endl;
    system("pause");
}
