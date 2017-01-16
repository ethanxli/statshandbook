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



int main(){

  int arr[] = {1,-2,-3,4,5};

  cout << maxarraysum(arr, 5) << endl;

}
