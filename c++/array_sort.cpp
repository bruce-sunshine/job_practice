#include <iostream>
#include <vector>
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

void shell_sort(int array[], int len)
{
    int step = len / 2;
    while(step > 0)
    {
        for(int i=step; i<len; i++)
        {
            int key = array[i];
            int j = i;
            while(j>0 && key < array[j-step])
            {
                array[j] = array[j-step];
                j -= step;
            }
            array[j] = key;
        }
        step /= 2;
    }
}

void merge(int a[], int left_a, int right_a, int left_b, int right_b)
{
    int n = (right_a - left_a + 1) + (right_b - left_b + 1);
    vector<int> c(n);
    int i = left_a; int j = left_b;
    int k = 0;
    while(i <= right_a && j <= right_b)
    {
        if(a[i] < a[j])
        {
            c[k++] = a[i++];
        }
        else
        {
            c[k++] = a[j++];
        }
    }
    while(i <= right_a)
            c[k++] = a[i++];
    while(j <= right_b)
            c[k++] = a[j++];
    for(int m=0; m<n; m++)
        a[left_a + m] = c[m];
}

void merge_sort(int array[], int start, int end)
{
	if (start < end)
	{
		int middle = (end + start) / 2;
		merge_sort(array, start, middle);
		merge_sort(array, middle + 1, end);
		merge(array, start, middle, middle + 1, end);
	}
}

int main(int argc, char** agrv)
{
    int array[] = {100,88,120,66,180,68,168,888,666,999};
//    vector<int> array_a{100,88,120,66,180,68,168,888,666,999};
//    bubbleSort(array,sizeof(array)/sizeof(int));
//    quick_sort(array, 0 , sizeof(array)/sizeof(int) - 1);
//    select_sort(array, sizeof(array)/sizeof(int));
//    insert_sort(array, sizeof(array)/sizeof(int));
//    merge_sort(array, 0 , sizeof(array)/sizeof(int) - 1);
    shell_sort(array,sizeof(array)/sizeof(int));
	for(int i=0; i<sizeof(array)/sizeof(int); i++)
		cout<<array<<" ";
	cout << endl;
	system("pause");
}