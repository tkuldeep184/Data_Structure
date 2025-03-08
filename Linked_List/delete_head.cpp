#include<iostream>
using namespace std;

struct Node{
    int val;
    Node *next;

    Node(int x){
        this->val = x; //this likh rahe hai aise hi , par agar int x ki jagah int val likha hota to this likhna zaruri hota 
        this->next = NULL;
    } 
    //Node(int x): val(x),next(NULL){} alternate for line 8-11
};

void PrintLL(Node*head){
    Node*temp = head;
    while(temp != nullptr){
        cout << temp->val <<" ";
        temp = temp->next;
    }
    cout << "\n";
}
Node* deletefnode(Node * head){
    Node * temp = head;
    if(head != nullptr){
        head = head -> next;
    }
    free(temp);
    return head;
}

int main()
{
    Node*N1 = new Node(10);
    Node*head = N1;
    Node*N2 = new Node(20);
    N1->next = N2;
    Node*N3 = new Node(30);
    N2->next = N3;
    Node*N4 = new Node(40);
    N3->next = N4;
    Node*N5 = new Node(50);
    N4->next = N5;
    PrintLL(head);
    head = deletefnode(head);
    PrintLL(head);
    return 0;
}

