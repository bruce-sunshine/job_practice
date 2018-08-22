#include <iostream>
#include <stdlib.h>
#include <stack>
#include <math.h>
#include <algorithm>
#include <vector>
using namespace std;

#define MAXSIZE 0xffff

template<class type>
class my_stack
{
	int top;
	type* my_ptr;
	int maxsize;

public:
	my_stack() :top(-1), maxsize(MAXSIZE)
	{
		my_ptr = new type[maxsize];
		if (my_ptr == NULL)
		{
			cerr << "my_stack alloc memory failed" << endl;
			exit(-1);
		}
	}

	my_stack(int size) :top(-1), maxsize(size)
	{
		my_ptr = new type[maxsize];
		if (my_ptr == NULL)
		{
			cerr << "my_stack alloc memory failed" << endl;
			exit(-1);
		}
	}

	~my_stack()
	{
		delete[] my_ptr;
	}

	bool Empty();
	type Top();
	void Push(type tp);
	void Pop();
	int Size();

};

template<class type>
    bool my_stack<type>::Empty()
    {
        if(top == -1)
            return true;
        else
            return false;
    }

template<class type>
    type my_stack<type>::Top()
    {
        if(top == -1)
        {
            cerr << "my_stack is empty" << endl;
            exit(-1);
        }
        else
        {
            return my_ptr[top];
        }
    }

	template<class type>
    void my_stack<type>::Push(type tp)
    {
        if(top + 1 < maxsize)
            my_ptr[++top] = tp;		//++top, not top++
        else
        {
            cout << "my_stack is full" << endl;
			exit(-1);
        }
    }

	template<class type>
    void my_stack<type>::Pop()
    {
        if(top == -1)
        {
            cerr << "my_stack is full" << endl;
            exit(-1);
        }
        else
        {
            top--;
        }
    }

	template<class type>
    int my_stack<type>::Size()
    {
        return top + 1;
    }


template<class type>
class NewStack
{
public:
	NewStack() :size(MAXSIZE){}

    NewStack(int Size):size(Size){}

    void Push(type ty)
    {
        if(stackData.size() + 1 < size)
        {
            stackData.push(ty);
            if (stackMin.size() == 0 || ty < getMin())
                stackMin.push(ty);
        }
        else
        {
            cerr << "NewStack is full" << endl;
            exit(-1);
        }
    }

    type Pop()
    {
        if(stackData.empty())
        {
            cerr << "NewStack is empty" << endl;
            exit(-1);
        }

        type value = stackData.top();
        if(value == getMin())
            stackMin.pop();
        stackData.pop();
    }

    type getMin()
    {
        if(stackData.size() == 0)
        {
            cerr << "NewStack is empty" << endl;
            exit(-1);
        }
        return stackMin.top();
    }

private:
    stack<type> stackData;
    stack<type> stackMin;
    int size;
};


// 由两个栈组成的队列
// 1.如果stackPush要往stackPop压入数据，那么必须一次性把stackPush中数据全部压入。 
// 2.如果stackPop不为空，stackPush绝对不能向stackPop压入数据。 
template <class type>
class TwoStackQueue
{
    public:
        void add(type num)
        {
            stackPush.push(num);
        }

        void poll()
        {
            if(stackPush.empty() && stackPop.empty())
            {
                cerr << "Queue is empty!" << endl;
                exit(-1);
            }
            else if(stackPop.empty())
            {
                while(!(stackPush.empty()))
                {
                    stackPop.push(stackPush.top());
                    stackPush.pop();
                }
            }
            return stackPop.pop();
        }

        type peek()
        {
            if(stackPush.empty() && stackPop.empty())
            {
                cerr << "Queue is empty!" << endl;
                exit(-1);
            }
            else if(stackPop.empty())
            {
                while(!(stackPush.empty()))
                {
                    stackPop.push(stackPush.top());
                    stackPush.pop();
                }
            }
            return stackPop.top();
        }

    private:
        stack<type> stackPush;
        stack<type> stackPop;

};

int getAndRemoveLast(stack<int>& stk)
{
    int result = stk.top();
    stk.pop();
    if(stk.size() == 0)
    {
        return result;	//返回栈底元素
    }
	else {
		int i = getAndRemoveLast(stk);	//得到栈底元素
		stk.push(result);	//栈顶元素压栈
		return i;
	}
}

void reverse(stack<int>& stk)
{
	if (stk.size() == 0)
	{
		return;
	}
    int i = getAndRemoveLast(stk);
    reverse(stk);
    stk.push(i);
}



void sortByStack(stack<int>& stk)
{
    if(stk.size() < 2)
        return;
    stack<int> help_stk;
    while(stk.size() != 0)
    {
        int cur = stk.top();
		stk.pop();
        if(help_stk.size() == 0 || help_stk.top() >= cur)
        {
            help_stk.push(cur);
        }
        else{
            while(help_stk.size() != 0)
            {
                stk.push(help_stk.top());
                help_stk.pop();
            }
			help_stk.push(cur);
        }        
    }
    while(help_stk.size() != 0)
    {
        stk.push(help_stk.top());
        help_stk.pop();
    }
}

vector<int> getMaxWindow(vector<int> arr, int w)
{
    if(arr.size() == 0 || w < 1 || arr.size() < w)
        return vector<int>{};
    
    deque<int> deq;
    vector<int> res;
    for(int i = 0; i < arr.size(); i++)
    {
        while(!deq.empty() && arr[deq.back()] <= arr[i])
            deq.pop_back();
        deq.push_back(i);
        if(deq.at(0) == i - w)
            deq.pop_front();
        if(i >= w - 1)
            res.push_back(arr[deq.at(0)]);
    }
    return res;
}

int maxRecFromBottom(vector<int>& height)
{
    if(height.size() == 0)
        return 0;
    stack<int> stack;
    int maxArea = 0;
    for(int i = 0; i < height.size(); i++)
    {
        while(!stack.empty() && height[stack.top()] >= height[i])
        {
            int j = stack.top();
            stack.pop();
            int k = stack.empty() ? -1 : stack.top();
            maxArea = max(maxArea, (j-k+1)*height[j]);
        }
        stack.push(i);
    }
    while(!stack.empty())
    {
        int j = stack.top();
        stack.pop();
        int k =  stack.empty() ? -1 : stack.top();
        maxArea = max(maxArea, (j-k+1)*height[j]);
    }
    return maxArea;
}

int maxRecSize(vector<vector<int>>& arr)
{
    if(arr.size() == 0)
        return 0;
    vector<int> height(arr[0].size(), 0);
    int maxArea = 0;

    for(int i = 0; i < arr.size(); i++)
    {
        for(int j = 0; j < arr[0].size(); j++)
        {
            height[j] = (arr[i][j] == 0 ? 0 : height[j] + 1);
        }
        maxArea = max(maxArea , maxRecFromBottom(height));
    }
    return maxArea;
}

int main()
{
    // my_stack<int> stk(500);
    // for(int i = 0; i < 200; i++)
    //     stk.Push(i);
    // cout << "my_stack size = " << stk.Size() << endl;
    // NewStack<int> new_stk(500);
    // new_stk.Push(123);
    // new_stk.Push(456);
    // new_stk.Push(789);
    // cout <<"getMin is " << new_stk.getMin() <<endl;
    // TwoStackQueue<int> queue;
    // queue.add(123);
    // queue.add(456);
	// cout << queue.peek() << endl;
    // queue.poll();
	// cout << queue.peek() << endl;
    // queue.poll();

//     stack<int> stk;
//     stk.push(4);
//     stk.push(3);
//     stk.push(2);
//     stk.push(1);
//     stk.push(5);
//     stk.push(6);
// //    reverse(stk);
//     sortByStack(stk);
//     cout << "stk, top = " << stk.top() << endl;
    // vector<int> vec = {4, 3, 5, 4, 3, 3, 6, 7};
    // vector<int> res;
    // res = getMaxWindow(vec, 3);
    // for(int i = 0; i < res.size(); i++)
    //     cout << res[i] << " ";
    vector<vector<int>> arr = {{1,0,1,1}, {1,1,1,1}, {1,1,1,0}};
    cout << maxRecSize(arr) <<endl;

	system("pause");
    return 0;
}