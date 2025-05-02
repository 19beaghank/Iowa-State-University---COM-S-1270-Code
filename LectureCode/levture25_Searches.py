# linear search

def linearSearch(arr,val):
    for i in range(0,len(arr)):
        if arr[i]==val:
            return i
    return -1

# binary search

def binarySearch(arr, val):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] <val:
            left = mid+1
        elif arr[mid] > val:
            right = mid+1
        else:
            return mid
    return -1

def binarySearchLeft(A, T):  #array and target
    retVal = None
    left = 0
    right = len(A)-1
    while left < right:
        middle = (left+right)//2
        if A[middle] <T:
            left = middle+1
        else:
            return middle
    if A[left] == T:
        retVal=left
    return retVal