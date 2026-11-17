#include<iostream>
using namespace std;
//create a structure of node
class node  

{
    public:
        int data;
        node *left; //left link
        node *right;    //right link
};


class Tree
{
public:
    	void insert(node *,node *); //function to insert node
    	void Inorder(node *);
	void Preorder(node *);
	void Postorder(node *);
	node *MinNode(node* );
	node *DeleteNode(node *, int);
	int Search(node*, int);
};
void Tree::insert(node *root, node *s)  //root = 15 s = 9
{
    //insert at right
    if(s->data >= root->data)//false
    {
        if(root->right == NULL)//true
            root->right = s;
        else
            insert(root->right, s);//root = 10, s = 9
    }




    //insert at left
    if(s->data < root->data)//true
    {
        if(root->left == NULL)//false
            root->left = s;
        else
            insert(root->left,s);
    }
}
void Tree::Inorder(node *root)
{
    if(root!=NULL)
    {
        Inorder(root->left);//left
        cout<<" "<<root->data;//root
        Inorder(root->right);//right
    }




}
void Tree::Preorder(node *T)
{
    if(T)
    {
	cout<<" "<<T->data;//root        
	Preorder(T->left);//left
        Preorder(T->right);//right
    }




}
void Tree::Postorder(node *T)
{
    if(T)
    {
        Postorder(T->left);//left
        Postorder(T->right);//right
	cout<<" "<<T->data;//root
    }
}
node *Tree::MinNode(node* root)
{
    if(root)
    {
        while(root->left)
            root = root->left;
    }
    return root;
}
node *Tree::DeleteNode(node *root, int key)
{
    node *temp;
    if(root)
    {
	  if(key<root->data)
		root->left = DeleteNode(root->left, key);
	  else if(key>root->data)
		root->right = DeleteNode(root->right, key);
	  else{
         	if(root->left == NULL){
			temp = root->right;
			delete root;
			return temp;
		}
		else if(root->right == NULL){
			temp = root->left;
			delete root;
			return temp;
		}
		temp = MinNode(root->right);
		root->data = temp->data;
		root->right = DeleteNode(root->right, temp->data);
	  }
    }
if(root->left == root->right == NULL)
	Delete root
    return root;
}
int Tree::Search(node* root, int k)
{
    int Flag = 0;
    if(root!=NULL)
    {
        if(k == root->data)
            return 1;
        else if(k < root->data)
            Flag = Search(root->left, k);
        else
            Flag = Search(root->right, k);
    }
    return Flag;
}


int main()
{
    int ch,c, key;
    char temp;
    node *root,*s;
    Tree t;


    root = new node;    //allocate memory for new node
    root = NULL;    //initially root is NULL


    do{
        cout<<"\n 1. Create & Insert New Node"
            <<"\n 2. Display-Inorder"
            <<"\n 3. Display-Preorder"
            <<"\n 4. Display-Postorder"
	    <<"\n 5. Delete Node"
	    <<"\n 6. Search Node"
            <<"\n 7. Exit"<<endl;
        cout<<"\n Enter your choice ";
        cin>>ch;
        switch(ch)
        {
            case 1:
                do{
                    s=new node; //allocate memory for new node
                    s->left=NULL;   //assign left child as NULL
                    s->right=NULL;  //assign right child as NULL


                    cout<<"\n"<<"ENTER DATA::";
                    cin>>s->data;


                    //check whether root is NULL
                    if(root == NULL)
                        root = s;
                    else
                        t.insert(root, s);


                    cout<<"\n"<<"WANT TO ENTER MORE ELEMENTS(y/n)::";
                    cin>>temp;




                }while(temp=='y');
                break;
            case 2:
                t.Inorder(root);
                break;
            case 3:
                t.Preorder(root);
                break;
            case 4:
                t.Postorder(root);
                break;
	    case 5:
		int key;
		cout<<"\nEnter key to be deleted :";
		cin>>key;
		root = t.DeleteNode(root,key);
		break;
	    case 6:
		cout<<"\nEnter key to be search :";
		cin>>key;
		int Flag; 
		Flag = t.Search(root, key);
		if(Flag == 1)
			cout<<"\nNode Found";
		else
			cout<<"\nNode not Found";
		break;
            default:
                cout<<"\n You are successfully exited \n";
                break;
        }
    }while(ch != 7);




    return 0;
}






