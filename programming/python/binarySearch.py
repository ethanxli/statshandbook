import sys


def binarysearch(array,num):
    left = 0
    right = len(array)-1

    while(left<=right):

        mid = (left+right)//2

        if(array[mid]==num):
            return mid

        if(array[mid] < num):
            left = mid + 1
        elif(array[mid] > num):
            right = mid - 1

    return -1





print binarysearch([1,2,3,4,6],6)
