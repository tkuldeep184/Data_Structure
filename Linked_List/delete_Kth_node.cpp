#include<iostream>
using namespace std;

struct Node
{
    int val;
    Node* next;

    Node(int x){
        this->val = x;
        this->next = nullptr;
    }
};
Node* deleteK(Node*head , int k){
    if(head == nullptr) return head;
    if (k==1)
    {
        Node*temp = head;
        head = temp->next;
        free(temp);
        return head;
    }

    int cnt = 0;
    Node*temp = head;
    Node*prev = nullptr;

    while(temp != nullptr){
        cnt++;
        if (cnt == k)
        {
            prev->next = prev->next->next;
            delete temp;
            break;
        }
        prev = temp;
        temp = temp->next;
    }
    return head;
}

void PrintLL(Node* head){
    Node*temp = head;
    while(temp){
        cout << temp->val << " ";
        temp = temp->next;
    }
    cout << "\n";
}

int main()
{
    Node* n1 = new Node(10);
    Node*head = n1;
    Node* n2 = new Node(20);
    n1->next = n2;
    Node* n3 = new Node(30);
    n2->next = n3;
    Node* n4 = new Node(40);
    n3->next = n4;
    Node* n5 = new Node(50);
    n4->next = n5;
    PrintLL(head);
    head = deleteK(head,1);
    PrintLL(head);
    return 0;
}

