def bubblesort(A):
    swapped = True
    while swapped:
        swapped=False
        for i in range(1,len(A)):
            if A[i-1]>A[i]:
                A[i-1], A[i] = A[i], A[i-1]
                swapped=True
    return A

def selectionsort(A):
    for i in range(0,len(A)-1):
        jMin=i
        for j in range(i+1,len(A)):
            if A[j]<A[jMin]:
                jMin=j
        if jMin!=i:
            A[i],A[jMin] = A[jMin], A[i]
    return A

def insertionsort(A):
    for i in range(1,len(A)):
        j=i
        while j>0 and A[j-1]>A[j]:
            A[j-1], A[j] = A[j], A[j-1]
            j-=1
    return A