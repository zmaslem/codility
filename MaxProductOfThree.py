import sys

__author__ = 'kawrobel'
import random

def MaxProductOfThree():
    A = [-3, 1, 2, -2, 5, 6]
    print(findMaxNums(A))

def findMaxNums(A):
    lg = len(A)
    min1 = 0
    min2 = 0
    min3 = 0
    max1 = 0
    max2 = 0
    max3 = 0
    iszero = False
    max = []
    rmax = 0
    for i in range(0,lg):
        if(max1 == 0):
            if(A[i]>0):
                max1 = A[i]
        elif(max2 == 0):
            if(A[i]>= max1):
                max2 = max1
                max1 = A[i]
        elif(max3 == 0):
            if(A[i] >= max1):
                max3 = max2
                max2 = max1
                max1 = A[i]
        else:
            if(A[i] >= max3):
                if(A[i]>=max2):
                    if(A[i] >= max1):
                        max3 = max2
                        max2 = max1
                        max1 = A[i]
                    else:
                        max3 = max2
                        max2 = A[i]
                else:
                    max3 = A[i]
        if(min1 == 0):
            if(A[i]<0):
                min1 = A[i]
        elif(min2 == 0):
            if(A[i] <= min1):
                min2 = min1
                min1 = A[i]
        elif(min3 == 0):
            if(A[i] <= min2):
                min3 = min2
                min2 = min1
                min1 = A[i]
        else:
            if(A[i] <= min3):
                if(A[i] <= min2):
                    if(A[i] <= min1):
                        min3 = min2
                        min2 = min1
                        min1 = A[i]
                    else:
                        min3 = min2
                        min2 = A[i]
                else:
                    min3 = A[i]
        if(A[i] == 0):
            iszero = True

    if(len(A)==3):
        return A[0]*A[1]*A[2]
    i = 0
    if(max1 < 0):
        max.append(max1*max2*max3)
        i+= 1
    if(max1 > 0 and max2 > 0 and max3 > 0):
        if(min1 < 0 and min2 < 0):
            max.append(max1*min1*min2)
            i += 1
        max.append(max1*max2*max3)
        i+=1
    if(max1 > 0 and max2 > 0 and max3 < 0):
        if(min1 < 0 and min2 < 0):
            max.append(max1*min1*min2)
            i+=1
    if(max1 > 0 and max2 < 0):
        if(min1 < 0 and min2 < 0):
            max.append(min1*min2*max1)
            i+=1
    if(max1 == 0):
        if(iszero):
            return 0
        max.append(max1)
        i += 1
    for i in range(0,i):
        if(max[i] > rmax):
            rmax = max[i]
    return rmax

def A(A):
    A = mergeSort(A)
    print (A)
    max = []
    rmax = 0
    i = 0
    if(len(A) == 3):
        max.append(A[0]*A[1]*A[2])
        i+=1
    else:
        if (A[-1] > 0 and A[-2] > 0 and A[-3] > 0):
            if(A[0]<0 and A[1]<0):
                max.append(long(A[-1]*A[0]*A[1]))
                i += 1
            max.append(A[-1]*A[-2]*A[-3])
            i+=1
        if(A[-1]>0 and A[-2]>0 and A[-3]<=0):
            if(A[0]<0 and A[1]<0):
                max.append(A[-1]*A[0]*A[1])
                i+=1
        if(A[-1]>0 and A[-2] <=0):
            max.append(A[0]*A[1]*A[-1])
            i+=1
        if(A[-1]<=0):
            if(A[-1] == 0):
                max.append(0)
                i+=1
            else:
                max.append(A[-1]*A[-2]*A[-3])
    rmax = max[0]
    for i in range(1,i):
        if(max[i]> rmax):
            rmax = max[i]
    return rmax


def mergeSort(list):
    buf = 0
    lg = len(list)
    if lg == 2:
        return sort(list)
    elif lg == 1:
        return list
    return manageDevided(list[:int(lg / 2)], list[int(lg / 2):])



def sort(list):
    if list[0] > list[1]:
        buf = list[0]
        list[0] = list[1]
        list[1] = buf
    return list


def manageDevided(list1, list2):
    list1 = mergeSort(list1)
    list2 = mergeSort(list2)
    lg = len(list1) if len(list1) < len(list2) else len(list2)
    list = []
    j = 0
    i = 0
    for i in range(0, lg):
        while j < len(list2) :
            if list1[i] > list2[j]:
                list.append(list2[j])
                j += 1
            elif list1[i] < list2[j]:
                list.append(list1[i])
                break
            else:
                list.append(list2[j])
                j += 1
        if(j == len(list2)):
            break
    if(j == len(list2) and i < len(list1)):
        list += list1[i:]
    elif i == len(list1)-1 and j < len(list2):
        list += list2[j:]
    return list

def checkIfSorter(A):
    bool = True
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            bool = False
    return bool
print (MaxProductOfThree())