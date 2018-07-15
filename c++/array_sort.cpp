#include <iostream>
using namespace std;

void bubbleSort(int array[], int len)
{
    for(int i=0; i<len-1; i++)
    {
        for(int j=0; j<len-i-1; j++)
        {
            if(array[j]>array[j+1])
            {
                int temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
            }
        }
    }
}

void quick_sort(int array[], int left, int right)
{
    if(left >= right)
        return;
    int low = left;
    int high = right;
    int key = array[low];

    while(low<high)
    {
        while(low<high && array[high]>key)
            --high;
        array[low] = array[high]; 
        while(low<high && array[low]<=key)
            ++low; 
        array[high] = array[low];
    }
    array[high] = key;
    quick_sort(array, 0, low-1);
    quick_sort(array, low+1, right);  
}

void select_sort(int array[], int len)
{
    for(int i=0; i<len-1; i++)
    {
        int min = i;
        for(int j=i+1; j<len-1; j++)
        {
            if(array[j] < array[min])
                min = j;
        }
        int temp = array[min];
        array[min] = array[i];
        array[i] = temp;
    }
}

void insert_sort(int array[], int len)
{
    for(int i=0; i<len; i++)
    {
        int key = array[i];
        int j = i-1;
        while(j>=0 && array[j]>key)
        {
            array[j+1] = array[j];
            --j;
        }
        array[j+1] = key;
    }
}

int main(int argc, char** agrv)
{
    int array[] = {100,88,120,66,180,68,168,888,666,999};
//    bubbleSort(array,sizeof(array)/sizeof(int));
//    quick_sort(array, 0 , sizeof(array)/sizeof(int) - 1);
//    select_sort(array, sizeof(array)/sizeof(int));
    insert_sort(array, sizeof(array)/sizeof(int));
	for(int i=0; i<10; i++)
		cout<<array[i]<<" ";
	cout << endl;
	system("pause");
}