#include <iostream>

using namespace std;


/*----------------------------------------*/
/* 0,1 Knapsack porblem
Given weights and values of n items, put these items in a knapsack of capacity W
to get the maximum total value in the knapsack.

In other words, given two integer arrays val[0..n-1] and wt[0..n-1]
which represent values and weights associated with n items respectively, and
an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that :
sum of the  weights of this subset <= to W.
-------------------------------------------*/


// Returns the maximum value that can be put in a knapsack of capacity W
int knapsack(int W, int wt[], int val[], int n){

  int dpm[n+1][W+1]; //value of n items, maximum W weight

  //iterate through possible items and possible weights.
  //O(n*W) where W is maximum weight

  for(int i =0; i < n; i++){

    //iterate through possible weights
    for(int j =0; j < W; j++){

        if(i==0|| j==0){ //max value of 0 items is 0
          dpm[i][j] =0;
        }else if(wt[i-1] <= W){
          //if weight of 1 items less than w.. check

          //current max weight is max of:
          dpm[i][j] = max(
            val[i-1] + dpm[i-1][j - wt[i-1]],  //previous item val + max value of ith item
            dpm[i-1][j]
          );

        } else{ //otherwise the max value for this weight iteration is just previous value of items
          dpm[i][j] = dpm[i-1][j];
        }
    }

  }

  return dpm[n][W];

}

// Find the number of paths from (1,1) to (n,n) in a matrix where you can go right and down.
// Find maximum sum path from (1,1) to (n,n) in a matrix.
//



//fibonacci sequence

int fibonacci(int n){
  int arr[n];

  for(int i = 0; i < n; i++){
    if(i==0 || i==1){
      arr[i] = 1;
    } else{
      arr[i] = arr[i-1] + arr[i-2];
    }
    cout<<arr[i]<<endl;
  }

  return arr[n];
}


/*
You are given an array of integers, A1, A2, ..., An, including negatives and positives,
and another integer S. Now we need to find three different integers in the array,
whose sum is closest to the given integer S. If there exists more than one solution,
any of them is ok. Is there an algorithm to find the three integers in O(n^2) time?
*/

void closestSum(int[] arr, int n, int s, int[] sol){

  for(int i = 0; i < n; i++){
    diff = s - arr[i];

    mindiff =
    for(int j = i+1; j<n; j++){
        if
    }


  }

}



////////////////////////////////////////////////


//Given a snake and ladder board of order 5x6 , find the minimum number of dice
//throws required to reach the destination or last cell (30th cell) from source (1st cell) .

int snakeLadder(){

  int minrolls[30][30]; //minrols[i][j] = min number of rolls it takes to get from i to j

  int ladders[20]; // ladders connecting ladders[i] and ladders[i-1];

  int endPoints[10];
  int beginPoints[10];

  for(int i = 30; i >0; i--){
    for(int j= 30; j > 0; j--){

    }
  }


}


int main(){
  fibonacci(9);
}
