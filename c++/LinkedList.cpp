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
    node10->next = NULL;
	printListNode(node1);
	printListNode(node6);
    printCommonPart(node1, node6);
    removeLastKthNode(node1, 2);
    printListNode(node1);
    removeMidNode(node6);
    printListNode(node6);
	system("pause");
    return 1;
}




