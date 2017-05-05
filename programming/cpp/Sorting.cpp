#import <iostream>
using namespace std;


//returns the maximum sum over a subarray
int maxarraysum(int arr[], int len){

  int best = 0;
  int curBest = 0;
  for(int i =0; i< len; ++i){
      curBest += arr[i];

      if(curBest < 0){
        curBest = 0;
      }
      best = (best > curBest) ? best : curBest;

  }

  return best;
}

//////
//quicksort
//
/*
1. pick a pivot value
2. while left less than pivot and right greater, swap
3. recurse
*/
void quicksort(int arr[], int left, int right){
  int i = left;
  int j = right;
  int tmp;
  int pivot = arr[(left+right)/2];

  while(i<=j){
    while(arr[i] < pivot)
      i++;
    while(arr[j] > pivot)
      j--;
    if(i <= j){
      //swap
      tmp = arr[i];
      arr[i] = arr[j];
      arr[j] = tmp;
      i++;
      j--;
    }
  },

  if(left<j){
    quicksort(arr,left,j);
  }
  if(right > i){
    quicksort(arr,i,right);
  }


}


int main(){

  int arr[] = {1,-2,-3,4,5};

  cout << maxarraysum(arr, 5) << endl;

}





// bool myfunction (int i,int j) { return (i<j); }
//
// struct myclass {
//   bool operator() (int i,int j) { return (i<j);}
// } myobject;
//
// int main () {
//   int myints[] = {32,71,12,45,26,80,53,33};
//   std::vector<int> myvector (myints, myints+8);               // 32 71 12 45 26 80 53 33
//
//   // using default comparison (operator <):
//   std::sort (myvector.begin(), myvector.begin()+4);           //(12 32 45 71)26 80 53 33
//
//   // using function as comp
//   std::sort (myvector.begin()+4, myvector.end(), myfunction); // 12 32 45 71(26 33 53 80)
//
//   // using object as comp
//   std::sort (myvector.begin(), myvector.end(), myobject);     //(12 26 32 33 45 53 71 80)
//
//   // print out content:
//   std::cout << "myvector contains:";
//   for (std::vector<int>::iterator it=myvector.begin(); it!=myvector.end(); ++it)
//     std::cout << ' ' << *it;
//   std::cout << '\n';
//
//   return 0;
// }
