__author__ = 'kawrobel'

H = [8, 8, 5, 7, 9, 8, 7, 4, 8]

def solution(H):
    numOfStones = 1
    I = [H[0]]
    for i in H:
        if(i > I[-1]):
            I.append(i)
            numOfStones += 1
        elif(i < I[-1]):
            while(len(I) > 0 and I[-1] > i ):
                I.pop()
            if(len(I) > 0 and I[-1] == i):
                continue
            I.append(i)
            numOfStones += 1
    return numOfStones

print(solution(H))
