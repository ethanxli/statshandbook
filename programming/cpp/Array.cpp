#import <iostream>
using namespace std;

//binarysearch
int binarysearch(int arr[], int len, int s){
  int left = 0;
  int right = len;
  int idx;

  while(left<=right){
    idx = (left+right)/2;
    if(arr[idx] < s){
        left = idx + 1;

    } else if(arr[idx] > s){
       right = idx-1;
    } else{
      return idx;
    }

  }

  return -1;

}


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


/*
Given an array A your task is to tell at which position the equilibrium
first occurs in the array. Equilibrium position in an array is a position
such that the sum of elements below it is equal to the sum of elements after it.
*/

int equilibrium(int arr[], int n){
  if(n==1){
    return 0;
  }

  int sum = 0;

  for(int i = 0; i < n; i++){
    sum+=arr[i];
  }

  int sum2 = 0;

  for(int i = 0; i <n; i++){


    if(sum2 == sum-sum2-arr[i]){
      return i;
    }

    sum2+=arr[i];

  }

  return -1;

}





//////////////////////////////////////////
//Determine if there exists two elements whose sum is x
////////////////////////////////////////////////

#define MAX 100000

void printPairs(int arr[], int arr_size, int sum)
{
  int i, temp;
  bool binMap[MAX] = {0}; /*initialize hash map as 0*/

  for (i = 0; i < arr_size; i++)
  {
      temp = sum - arr[i];
      if (temp >= 0 && binMap[temp] == 1)
         printf("Pair with given sum %d is (%d, %d) \n",
                 sum, arr[i], temp);
      binMap[arr[i]] = 1;
  }
}

/* Driver program to test above function */
int main()
{
    int A[] = {1, 4, 45, 6, 10, 8};
    int n = 16;
    int arr_size = sizeof(A)/sizeof(A[0]);

    printPairs(A, arr_size, n);

    getchar();
    return 0;
}


int main(){

  int arr[] = {1,3,5,2,2,4,3};

  cout << equilibrium(arr,7) <<endl;

}
