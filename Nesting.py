__author__ = 'kawrobel'

s = ')('

def solution(S):
    nests = 0
    for letter in S:
        if(nests == 0 and letter == ')'):
            return 0
        if(letter == '('):
            nests += 1
        elif(letter == ')'):
            nests -= 1
    return 1 if nests == 0 else 0

print(solution(s))