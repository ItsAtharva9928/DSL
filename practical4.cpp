#include <iostream>
using namespace std;

class Stack{
public:
	string s[20], R[20];
	int top, rtop;
	
Stack(){
		top = -1;   //Stack S  
		rtop = -1;  //Stack R
	}
	void push(string x){   //Stack S
		s[++top] = x;
	}
	string pop(){              //Stack S
		return s[top--];
	}
	void rpush(string x){  //Stack R
		R[++rtop] = x;
	}
	string rpop(){         //Stack R
		return R[rtop--];
	}
	void display(){     //Display Stack S
		for(int i= 0; i<=top; i++)
			cout << s[i] <<" ";
	}
};
int main() {
	Stack t;  //object of class
    	string x, r;  //input string
	char ch;   //Choice option (y/n)
	int choice;  //Switch case choice
	do{
		cout<<"\n1. Create Document";
		cout<<"\n2. Undo";
		cout<<"\n3. Redo";
		cout<<"\n4. Display Document State";
		cout<<"\n5. Exit";
		cout<<"\nEnter your choice: ";
		cin>>choice;
		switch(choice){
			case 1:
				cout<<"\nEnter Word in Document:";
				cin>>x;
				t.push(x);   //S Stack
				cout<<"\nDocument Contents are :\n";
				t.display();
				break;
			case 2:
				r = t.pop();  //S Stack
				cout<<r;
				t.rpush(r);  //R Stack

				cout<<"\nDocument Contents after undo operations :\n";
				t.display();
				break;
			case 3:
				x = t.rpop();  //R Stack
				t.push(x);    //S Stack
				cout<<"\nDocument Contents after redo operations :\n";
				t.display();
				break;
			case 4:
				cout<<"\nDocument Contents are :\n";
				t.display();
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

