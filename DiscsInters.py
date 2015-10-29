__author__ = 'kawrobel'


def foo(A):
    sum = 0
    for i in range (0, len(A), 2):
        sum = sum + A[i]
    print(sum%10)

A = [1, 5, 2, 6, 2, 56, 8]
foo(A)