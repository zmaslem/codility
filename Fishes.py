__author__ = 'kawrobel'
A = [4, 3, 2, 1, 5, 6, 10, 7, 8, 9, 11, 15]
B = [0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1]
def solution(A, B):
    length = len(A)
    C = []
    for i in range(0, length):
        if(len(C) == 0):
            C.append(i)
        else:
            while(len(C) > 0 and B[i] - B[C[-1]] == -1 and A[C[-1]] < A[i]):
                C.pop()
            if(len(C) > 0):
                if(B[i] - B[C[-1]] != -1):
                    C.append(i)
            else:
                C.append(i)
    return len(C)
print(solution(A,B))