#include <iostream>
#include <stdio.h>

using namespace std;


/* Function to calculate x raised to the power y */
// runtime : o(log y)
int power(int x, int y){
  if(y==0){
    return 1;
  }

  int temp = power(x, y/2);
  if(y%2==0){
    return temp * temp;
  } else{
    return x * temp * temp;
  }
}


//a and b are sorted arrays.
//find the median of a and b
/*
1) Calculate the medians m1 and m2 of the input arrays ar1[]
   and ar2[] respectively.
2) If m1 and m2 both are equal then we are done.
     return m1 (or m2)
3) If m1 is greater than m2, then median is present in one
   of the below two subarrays.
    a)  From first element of ar1 to m1 (ar1[0...|_n/2_|])
    b)  From m2 to last element of ar2  (ar2[|_n/2_|...n-1])
4) If m2 is greater than m1, then median is present in one
   of the below two subarrays.
   a)  From m1 to last element of ar1  (ar1[|_n/2_|...n-1])
   b)  From first element of ar2 to m2 (ar2[0...|_n/2_|])
5) Repeat the above process until size of both the subarrays
   becomes 2.
6) If size of the two arrays is 2 then use below formula to get
  the median.
    Median = (max(ar1[0], ar2[0]) + min(ar1[1], ar2[1]))/2
*/

int median(int a[], int b[]){
  int merge[2*a.size()];

  for(int i = 0; i < 2*n; i++){

  }

}

int main(){
  cout << power(5,5) << endl;
}
