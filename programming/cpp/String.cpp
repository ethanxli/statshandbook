#include <iostream>

using namespace std;



void reverse(char s[])
{
    int length = strlen(s);
    int c, i, j;

    for (i = 0, j = length - 1; i < j; i++, j--)
    {
        c = s[i];
        s[i] = s[j];
        s[j] = c;
    }
}

//recursive reverse
void reverse(char *s, size_t len)
{
    if ( len <= 1 || !s ) return;

    std::swap(s[0], s[len-1]);// swap first and last simbols
    s++; // move pointer to the following char
    reverse(s, len-2); // shorten len of string
}


int main(){

  

  return 0;
}
