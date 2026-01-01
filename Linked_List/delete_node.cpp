#include<iostream>
using namespace std;

struct Node{
    int val;
    Node* next;

    Node(int x){
        val = x;
        next = nullptr;
    }
};

Node* delete_node(Node* head, int el){
    if(head == nullptr)return head;
    if(head->val == el){
        Node*temp = head;
        head = temp->next;
        delete temp;
        return head;
    }
    Node*temp = head;
    Node*prev = nullptr;
    while(temp != nullptr){
        if(temp->val == el){
            prev->next = prev->next->next;
            delete temp;
            break;
        }
        prev = temp;
        temp = temp->next;
    }
    return head;
}

void PrintLL(Node*head){
    Node*temp = head;
    while(temp != nullptr){
        cout << temp->val << " ";
        temp = temp->next;
    }
    cout << "\n";
}

int main()
{
    Node* n1 = new Node(10);
    Node* head = n1;
    Node* n2 = new Node(20);
    n1->next = n2;
    Node* n3 = new Node(30);
    n2->next = n3;
    Node* n4 = new Node(40);
    n3->next = n4;
    Node* n5 = new Node(50);
    n4->next = n5;
    PrintLL(head);
    head = delete_node(head,20);
    PrintLL(head);
    return 0;
}
