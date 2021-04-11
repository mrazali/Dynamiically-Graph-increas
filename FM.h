#include <iostream>
using namespace std;

struct node{
	string name;
	int no;
	node *ptr;
};

class tree{
	public:
		node *root;
		tree();
		~tree();
		void Multitree(node *);
		void destroy(node *);
};

tree::tree(){
	root=NULL; 
}

tree::~tree(){
	destroy(root);
	delete root;
}

void tree::Multitree(node *temp){
	node *temp1;
	if(root==NULL){
		root=new node;
		cout<<"Enter subervisor"<<endl;
		cin>>root->name;
		cout<<"Enter number of subcodinates "<<endl;
		cin>>root->no;
		if(root->no){
			root->ptr=new node[root->no];
			temp=root->ptr;
			for(int i=0; i<root->no; i++){
				cout<<"super : "<<root->name<<endl;
				Multitree(temp);
				cout<<endl<<endl;
				temp++;
			}
		}else{
			root->ptr=NULL;
		}return;
	}else{
		cout<<"Enter subervisor"<<endl;
		cin>>temp->name;
		cout<<"Enter number of subcodinates "<<endl;
		cin>>temp->no;
		if(temp->no){
			temp->ptr=new node[temp->no];
			temp1=temp;
			temp=temp->ptr;
			for(int i=0; i<temp1->no; i++){
				cout<<"super : "<<temp1->name<<endl;
				Multitree(temp);
				cout<<endl<<endl;
				temp++;
			}
		}else{
			temp->ptr=NULL;
		}return;
	}
}

//void tree::printing(node *temp){
//	node *temp1;
//	if(temp==root){
//		cout<<"supervisor  : "<<temp->name<<endl;
//	}
//	
//	if(temp==NULL)
//		return;
//	if(temp->no==0)
//		return;	
//	temp1=temp;
//	temp=temp->ptr;
// 	for(int i=0; i<temp1->no; i++){
// 		cout<<"supervisor  : "<<temp->name<<endl;
//		printing(temp);
//		temp++;
//	}	
//	return;
//}

void tree::destroy(node *temp){
	node *temp1;
	if(temp==NULL)
		return;
	if(temp->no==0)
		return;	
	temp1=temp;
	temp=temp->ptr;
 	for(int i=0; i<temp1->no; i++){
		temp++;
	}
	delete []temp1;
	return;
}

//int main(){
//	tree te;
//	te.Multitree(te.root);
//	te.printing(te.root);
//	return 0;
//}
