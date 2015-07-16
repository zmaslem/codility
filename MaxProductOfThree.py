__author__ = 'kawrobel'
import random

def MaxProductOfThree():
    A = [-3, 1, 2, -2, 5, 6]
    B = random.sample(range(-2000, 4000), 5000)
    C = random.sample(range(-2000, 4000), 5000)
    A = mergeSort(A)
    plus = 0
    minus = 0
    sum = 0




def mergeSort(list):
    buf = 0
    lg = len(list)
    if lg == 2:
        return sort(list)
    elif lg == 1:
        return list
    return manageDevided(list[:int(lg / 2)], list[int(lg / 2):])


def sort(list):
    if (abs(list[0]) > abs(list[1])):
        buf = list[0]
        list[0] = list[1]
        list[1] = buf
    return list


def manageDevided(list1, list2):
    list1 = mergeSort(list1)
    list2 = mergeSort(list2)
    print('list1 =' + str(list1))
    print('list2 =' + str(list2))
    lg = len(list1) if len(list1) < len(list2) else len(list2)
    list = []
    j = 0
    i = 0
    for i in range(0, lg):
        while j < len(list2) :
            if abs(list1[i]) > abs(list2[j]):
                list.append(list2[j])
                j += 1
            elif abs(list1[i]) < abs(list2[j]):
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

    print('list =' + str(list))
    return list

def checkIfSorter(A):
    bool = True
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            bool = False
    return bool
print (MaxProductOfThree())