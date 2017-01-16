
#include <iostream>
#include <vector>
#include <deque>
#include <stdlib.h>

using namespace std;


void BFS(){


}


struct LinkedListNode{
    int data;
    LinkedListNode* next;

    LinkedListNode(int data){

    }
};

struct Node{
  int data;
  Node* left;
  Node* right;

  Node(int n){
    data = n;
    left=NULL;
    right=NULL;
  }

  void setLeft(Node* left){
    this->left = left; //we have access to -this- pointer
  }
};

// the height of a tree is the max of its left and right heights

int height(Node* tree){
  if(tree==NULL){
    return 0;
  }

  return 1 + max(height(tree->left), height(tree->right));

}


void visit(Node* node){
  cout<<node->data<<endl;
}

void DFTraversal(Node* root){

  if(root==NULL){
    return;
  }

  visit(root);

  if(root->left){
    DFTraversal(root->left);
  }

  if(root->right){
    DFTraversal(root->right);
  }

}


//    3
//  1  2
// 4  2 3

/* --------------------------------------------------------*/
/* ----------------  Longest Unique Path -----------------*/
/* --------------------------------------------------------*/

int isIn(int data,deque<int>& uniques){
    for(int i = 0; i<uniques.size(); i++){
      if(uniques[i]==data)return 0;
    }
    return 1;
}

int longestUniquePathHelper(Node* tree, deque<int>& visited){
  if (tree == NULL){
    return 0;
  }

  //cout<<"pushing"<< tree->data<<endl;
  //cout<<tree->data<<','<<visited.size()<<endl;

  int u = isIn(tree->data, visited);
  visited.push_front(tree->data);

  int lmax = 0;
  int rmax = 0;

  lmax = u + longestUniquePathHelper(tree->left,  visited);
  rmax = u + longestUniquePathHelper(tree->right,  visited);

  visited.pop_front();
  //cout << "popping" <<endl;

  return max(lmax,rmax);

}

int longestUniquePath(Node* root){
  deque<int> visited;
  return longestUniquePathHelper(root, visited);
}

/* --------------------------------------------------------*/
/* ------------- IsBalanced    ----------------------------*/
/* --------------------------------------------------------*/
/*
a tree is balanced if the max difference in height of each of its
subtrees is at most one
*/


bool isBalanced(Node* tree){

  return false;
}


int main(){

  Node n(2);
  Node n2(1);
  Node n3(2);
  Node n4(2);
  Node n5(2);
  Node n6(2);

  n.left = &n2;
  n.right = &n3;
  n2.left = &n4;
  n2.right = &n5;
  n3.right = &n6;

  //DFTraversal(&n);

  //cout << longestUniquePath(&n) << endl;
  cout << height(&n) << endl;

  return 0;
}
