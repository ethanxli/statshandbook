
#include <iostream>
#include <vector>
#include <deque>
#include <stdlib.h>

using namespace std;



struct Node{
    int data;
    Node* next;

    Node(int data){
      this->data = data;
    }
};


int main(){

  Node n(2);
  Node n2(1);
  Node n3(2);
  Node n4(2);
  Node n5(2);
  Node n6(2);

  return 0;
}
