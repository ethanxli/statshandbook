#import <iostream>

using namespace std;


//Write a program to print all permutations of a given string
void swap(char* x, char* y){
  char temp;
  temp = *y;
  *y = *x;
  *x = temp;
}

/* Function to print permutations of string
   This function takes three parameters:
   1. String
   2. Starting index of the string
   3. Ending index of the string. */
void permute(char *a, int l, int r)
{
   int i;
   if (l == r)
     printf("%s\n", a);
   else
   {
       for (i = l; i <= r; i++)
       {
          swap((a+l), (a+i));
          permute(a, l+1, r);
          swap((a+l), (a+i)); //backtrack
       }
   }
}





void permuteWithSpace(char* a, int len){
  if(len==0){
    cout << a;
  }else{

  }
  permuteWithSpace(a+l, len-1);
}


/* Driver program to test above functions */
int main()
{
    char str[] = "ABC";
    int n = strlen(str);
    permute(str, 0, n-1);
    return 0;
}
