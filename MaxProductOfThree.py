__author__ = 'kawrobel'


def MaxProductOfThree():
    A = [3, 2, 1, 8]
    print(mergeSort(A))


def mergeSort(list):
    buf = 0
    lg = len(list)
    if lg == 2:
        return sort(list)
    elif lg == 1:
        return list
    manageDevided(list[:int(lg/2)], list[int(lg/2):])



def sort(list):
    if(list[0] > list[1]):
        buf = list[0]
        list[0] = list[1]
        list[1] = buf
    return list

def manageDevided(list1, list2):
    list1 = mergeSort(list1)
    list2 = mergeSort(list2)
    lg =  len(list1) if len(list1) > len(list2) else len(list2)




MaxProductOfThree()