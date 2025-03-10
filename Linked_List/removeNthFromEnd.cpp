#include<iostream>
using namespace std;

struct ListNode{
    int val;
    ListNode* next;

    ListNode(int x){
        val = x;
        next = nullptr;
    }
};
 
ListNode* removeNthFromEnd(ListNode* head, int n) {
        /**if(head == nullptr)return head;
        
        int cnt = 0;
        ListNode* temp = head;
        while(temp){
            cnt++;
            temp = temp->next;
        }
        if(n > cnt)return head;
        int target = cnt - n;
        if(target == 0){
            ListNode*newHead = head->next;
            delete head;
            return newHead;
        }
        temp = head;
        for(int i = 0; i< target-1; i++){
            temp = temp->next;
        }
        ListNode* node2delete = temp->next;
            temp->next = temp->next->next;
            delete node2delete;
            return head;**/
    int cnt =0;
    ListNode* temp = head;
    while(temp){
        cnt++;
        temp = temp->next;
    }
    if(n > cnt)return head;

    ListNode* fast = head;
    ListNode* slow = head;

    for(int i = 0; i < n; i++)
        fast = fast->next;
    if(fast == nullptr)return head->next;

    while (fast->next != nullptr){
        fast = fast->next;
        slow = slow->next;
    }
    ListNode* delnode = slow->next;
    slow->next = slow->next->next;
    delete delnode;
    return head;
    }

void PrintLL(ListNode*head){
    ListNode*temp = head;
    while(temp != nullptr){
        cout << temp->val << " ";
        temp = temp->next;
    }
    cout << "\n";
}

int main()
{
    ListNode* n1 = new ListNode(10);
    ListNode* head = n1;
    ListNode* n2 = new ListNode(20);
    n1->next = n2;
    ListNode* n3 = new ListNode(30);
    n2->next = n3;
    ListNode* n4 = new ListNode(40);
    n3->next = n4;
    ListNode* n5 = new ListNode(50);
    n4->next = n5;
    PrintLL(head);
    head = removeNthFromEnd(head,6);
    PrintLL(head);
    return 0;
}
