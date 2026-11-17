#include<iostream>
using namespace std;     
#define Max 20
class Queue{
public:
	int front, rear, Q[Max];
	Queue(){
		front = rear = -1;
	}
	void addCall(int x){
		if(rear == Max-1)
			cout<<”Queue is full”
		else
			Q[++rear] = x; 
	}
	int answerCall(){
		if(isQueueEmpty() == 1)
			cout<<”Queue is empty”
		else
			return Q[++front];
	}
	void viewQueue(){
		for(int i = front+1; i<=rear; i++)
			cout<< Q[i] << " ";
	}
	bool isQueueEmpty(){
		if(front == rear)
			return true;
		return false;
	}
};
int main(){
	Queue q;
	char ch;
	int choice,cid;
	do{
		cout<<"\n1.Add a call to the queue with the customer ID ";
		cout<<"\n2.Answer and remove the first call from the queue ";
		cout<<"\n3.View all calls currently in the queue ";
		cout<<"\n4.Check if the queue is empty ";
		cout<<"\n5.Exit ";
		cout<<"\nEnter your choice: ";
		cin>>choice;
		switch(choice){
			case 1:
				cout<<"\nEnter Customer ID: ";
				cin>>cid;
				q.addCall(cid);
				break;
			case 2: 
				cout<<"Answerd call: "<< q.answerCall();			
				break;
			case 3:
				cout<<"\n View all calls currently in the queue ";
				q.viewQueue();
				break;
			case 4:
				cout<<"\n Empty status of queue "<< q.isQueueEmpty();	
				break;
			case 5:
				exit(0);
				break;
		}
		cout<<"\nDo you want to continue (y/n)";
		cin>>ch;
	}while(ch == 'y');

	return 0;
}


