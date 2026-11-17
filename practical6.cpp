#include <iostream>
using namespace std;
class node{
public:
	int Roll_No;
      char Name[10]; 
      float Marks;
	node* next;
};
class LinkedList{
public:
	node* create(node *n);
	node* insertNode(node *n); //Add
	void display(node *n);     //Display
	node* deleteNode(node *n); //Delete
      node* update(node *n);     //Update
      node* search(node *);      //Search
	node* sort(node *n);        //Sort
};
node* LinkedList :: create(node *n){
	int N;
	cout<<"\nEnter the No. of node of list ";
	cin>>N;
	n = new node();
	n->next = NULL;
	cout<<"\nEnter Roll No, Name, Marks : ";
	cin>>n->Roll_No>>n->Name>>n->Marks;
	for(int i=1;i<N;i++)
		n = insertNode(n);
	return n;
}
node* LinkedList :: insertNode(node *n){
	node *p, *q;
	q = n;
	p = new node();
	p->next = NULL;
	cout<<"\nEnter Roll No, Name, Marks : ";
	cin>>p->Roll_No>>p->Name>>p->Marks;
	while(q->next!=NULL)
		q = q->next;
	q->next = p;
	return n;
}
void LinkedList :: display(node *n){
	node *p;
	p = n;
	cout<<"\nThe Students Records are\n";
	while(p){
		cout<<p->Roll_No<<” ”<<p->Name<<” ”<<p->Marks;
		p=p->next;
	}
}
node* LinkedList :: deleteNode(node *n){
	node *p,*q;
	p = n;
	int V;
	cout<<"\nEnter Roll No to be deleted: ";
	cin>>V;
	if(n->Roll_No == V){
		q = n;
		n = n->next;
		q->next = NULL;
		delete q;
	}
	else{
		while(p->next){
			q = p->next;
			if(q->Roll_No == V){
				p->next = q->next;
				delete q;
				break;
			}
			else
				p = p->next;
		}
	}
	return n;
}
void LinkedList :: update(node *n){
node *p,*q;
	p = n;
	int V;
	cout<<"\nEnter Roll No to be update: ";
	cin>>V;
	while(p->next){
		if(p->Roll_No == V){
			cout<<"\nEnter Roll No, Name, Marks : ";
			cin>>p->Roll_No>>p->Name>>p->Marks;
			break;
		}
		else
			p = p->next;
	}

}
void LinkedList :: search(node *n){
     node *p,*q;
	p = n;
	int V;
	cout<<"\nEnter Roll No to be search: ";
	cin>>V;
	while(p->next){
		if(p->Roll_No == V){
			cout<<”Record Found”;
			break;
		}
		else
			p = p->next;
	}
}
node *linkedList :: sort(node *head){
	node *p;
	p = head;
	while(p->next!=NULL){
		node *q;
		q = p;
		while(q!=NULL){
			if(q->roll_no < p->roll_no){
				int temp1 = q->roll_no;
				q->roll_no = p->roll_no;
				p->roll_no = temp1;

				int temp2 = q->name;
				q->name = p->name;
				p->name = temp2;

				int temp3 = q->marks;
				q->marks = p->marks;
				p->marks = temp3;
			}
			q=q->next;
		}
		p=p->next;
	}
	return head;
}

/*node* LinkedList :: sort(node *head){
	// Initialize previous and current nodes
    Node* prev = (*head);
    Node* curr = (*head)->next;

    // Traverse list
    while (curr != NULL)
    {
        // If curr is smaller than prev, 
        // then it must be moved to head
        if (curr->Roll_No < prev->Roll_No)
        {
            // Detach curr from linked list
            prev->next = curr->next;

            // Move current node to beginning
            curr->next = prev;
            prev = curr;

            // Update current
            curr = prev;
        }

        // Nothing to do if current 
        // element is at right place
        else
            prev = curr;

        // Move current
        curr = curr->next;
    }
return head;

}*/
int main() {
	LinkedList l;
	node *n;
	n = l.create(n); //create linked list
	l.display(n);    //display linked list
	n = l.deleteNode(n); //delete node
	l.display(n);    //display node
      l.update(node *n); //update node
      l.search(node *);  //search node
	n = l.sort();      //sort node
      l.display(n);    //display node
	return 0;
}


