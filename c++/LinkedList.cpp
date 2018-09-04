#include <iostream>
#include <math.h>
#include <algorithm>
using namespace std;

class ListNode
{
public:
    int val;
    ListNode *next;
    ListNode() {}
    ListNode(int value)
    {
        val = value;
        next = NULL;
    } 
};

class DoubleListNode
{
public:
    int val;
    DoubleListNode *pre;
    DoubleListNode *next;
    DoubleListNode() {}
    DoubleListNode(int value)
    {
        val = value;
        pre = NULL;
        next = NULL;
    } 
};

//输出链表信息
void printListNode(ListNode* head)
{
	ListNode *pNode = head;
    while(pNode)
    {
        cout << pNode->val << " ";
		pNode = pNode->next;
    }
    cout << endl;
}

//获取链表长度
int getLength(ListNode* head)
{
    int nLength = 0;
    ListNode *pNode = head;
    while(pNode != NULL)
    {
        ++nLength;
        pNode = pNode->next;
    }
    return nLength;
}

//打印两个有序链表的公共部分
void printCommonPart(ListNode* head1, ListNode* head2)
{
	if (head1 == NULL || head2 == NULL)
		return;
	cout << "Common part is: " << endl;
	while (head1 != NULL && head2 != NULL)
	{
		if (head1->val > head2->val)
		{
			head2 = head2->next;
		}
		else if (head1->val < head2->val)
		{
			head1 = head1->next;
		}
		else
		{
			cout << head1->val << " ";
			head1 = head1->next;
			head2 = head2->next;
		}
	}
    cout << endl;
}

//单链表中删除倒数第K个节点
ListNode* removeLastKthNode(ListNode* head, int k)
{
    if(head == NULL || k < 1)
        return NULL;
    ListNode* pNode = head;
    while(pNode != NULL)
    {
        --k;
        pNode = pNode->next;
    }
    if(k == 0)
        return head->next;
    else if(k < 0)
    {
        pNode = head;
        while(k + 1 != 0)
        {
            pNode = pNode->next;
            ++k;
        }
        pNode->next = pNode->next->next;
    }
    return head;
}

//删除链表中间节点和a/b处节点
ListNode* removeMidNode(ListNode* head)
{
    if(head == NULL || head->next == NULL)
        return head;
    if(head->next->next == NULL)
        return head->next;
    ListNode* pre = head;
    ListNode* cur = head->next->next;
    while(cur->next != NULL && cur->next->next != NULL)
    {
        pre = pre->next;
        cur = cur->next->next;
    }
    pre->next = pre->next->next;
    return head;
}

ListNode* removeByRatio(ListNode* head, int a, int b)
{
    if(head == NULL || a < 1 || a > b)
    {
        return head;
    }
    int len = 0;
    ListNode* cur = head;
    while(cur != NULL)
    {
        ++len;
        cur = cur->next;
    }
    int n = ((double)a / (double)b) * len;
    cur = head;
    while(n - 1 != 1)
    {
        cur = cur->next;
        --n;
    }
    cur->next = cur->next->next;
    return head;
}

//反转单向链表和双向链表
ListNode* reverseList(ListNode* head)
{
    if(head == NULL)
        return NULL;
    ListNode* pre = NULL;
    ListNode* next;
    while(head != NULL)
    {
        next = head->next;
        head->next = pre;
        pre = head;
        head = next;
    }
    return pre;
}

DoubleListNode* reverseDoubleList(DoubleListNode* head)
{
    if(head == NULL)
        return NULL;
    DoubleListNode* pre = NULL;
    DoubleListNode* next;
    while(head != NULL)
    {
        next = head->next;
        head->pre = next;
        head->next = pre;
        pre = head;
        head = next;
    }
    return pre;
}

//反转部分单向列表
ListNode* reversePart(ListNode* head, int start, int end)
{
    if(head == NULL || head->next == NULL)
        return head;
    int len = 0;
    ListNode* fPre = NULL;
    ListNode* tPos = NULL;
    ListNode* node1 = head;
    while(node1 != NULL)
    {
        ++len;
        fPre = (len == start - 1 ? node1 : fPre);
        tPos = (len == end + 1 ? node1 : tPos);
        node1 = node1->next;
    }
    if(start < 1 || start > end || end > len)
        return head;
    node1 = (fPre == NULL ? head : fPre->next);
    ListNode* node2 = node1->next;
    node1->next = tPos;
    ListNode* next;
    while(node2 != tPos)
    {
        next = node2->next;
        node2->next = node1;
        node1 = node2;
        node2 = next;
    }
    if(fPre != NULL)
    {
        fPre->next = node1;
        return head;
    }
    return node1;
}

//环形单链表的约瑟夫问题
ListNode* josephusKill1(ListNode* head, int m)
{
    if(head == NULL || head->next == NULL || m < 1)
        return head;
    ListNode* pre = head;
    while(pre->next != head)
        pre = pre->next;
    int count = 1;
    while(head != pre)
    {
        if(count != m)
        {
            head = head->next;
            pre = pre->next;
            ++count;
        }
        else
        {
            pre->next = head->next;
            head = pre->next;
            count = 1;
        }
    }
    return head;
}

int getLive(int n, int m)
{
    if(n == 1)
        return 1;
    return (getLive(n - 1, m) + m - 1) % n + 1;
}

ListNode* josephusKill2(ListNode* head, int m)
{
    if(head == NULL || head->next == NULL || m < 1)
        return head;
    int n = 1;
    ListNode* cur = head;
    while(cur->next != head)
    {
        ++n;
        cur = cur->next;
    }
    n = getLive(n, m);
    while(n - 1 != 0)
    {
        --n;
        head = head->next;
    }
    head->next = head;
    return head;
}

int main()
{
    ListNode* node1 = new ListNode(1);
    ListNode* node2 = new ListNode(3);
    ListNode* node3 = new ListNode(4);
    ListNode* node4 = new ListNode(5);
    ListNode* node5 = new ListNode(7);
    ListNode* node6 = new ListNode(3);
    ListNode* node7 = new ListNode(4);
    ListNode* node8 = new ListNode(5);
    ListNode* node9 = new ListNode(6);
    ListNode* node10 = new ListNode(8);
    node1->next = node2;
    node2->next = node3;
    node3->next = node4;
    node4->next = node5;
    node5->next = NULL;
    node6->next = node7;
    node7->next = node8;
    node8->next = node9;
    node9->next = node10;
//    node10->next = NULL;
//	printListNode(node1);
//	printListNode(node6);
//  printCommonPart(node1, node6);
//  removeLastKthNode(node1, 2);
//  printListNode(node1);
//  removeMidNode(node6);
//  removeByRatio(node6, 2, 4);
//	reverseList(node6);
    // printListNode(reverseList(node6));
    // printListNode(reversePart(node6, 2, 4));
	node10->next = node6;
    // josephusKill1(node6,2);
    josephusKill2(node6,2);
	system("pause");
    return 1;
}




