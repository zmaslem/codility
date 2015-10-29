__author__ = 'kawrobel'


A = [-100, 3, 0, 2, 2, 3, 4, 6, 23, 2, 234, 4, 5, 66, -3, -2, -5, -5, 6, 6, 4, 34, 1]

def localMin(A):
    numberOfMins = 0
    mins = []
    l = len(A)
    if(A[0] < A[1]):
        mins.append(A[0])
        numberOfMins += 1
        numberOfMins += 1
    for i in range(1, l-1):
        if(A[i-1] > A[i] and A[i] < A[i+1]):
            mins.append(A[i])
            numberOfMins += 1
    if(A[l-1] < A[l-2]):
        mins.append(A[l-1])
    print(mins)
    print(numberOfMins)

localMin(A)