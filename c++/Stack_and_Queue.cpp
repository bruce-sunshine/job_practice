#include <iostream>
#include <stdlib.h>
//#include <math.h>
//#include <algorithm>
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


int main()
{
    my_stack<int> stk(500);
    for(int i = 0; i < 200; i++)
        stk.Push(i);
    cout << "my_stack size = " << stk.Size() << endl;

	system("pause");
    return 0;
}