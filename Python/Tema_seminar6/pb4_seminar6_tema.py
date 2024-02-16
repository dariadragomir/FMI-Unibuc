n = int(input())
A = [int(x) for x in input().split()]
S = int(input())

def backtr(ind, s_aux, rez):
    for i in range(ind, n):
        if s_aux + A[i] < S:
            rez.append(A[i])
            backtr(i + 1, s_aux + A[i], rez)
            rez.pop()
        elif s_aux + A[i] == S:
            rez.append(A[i])
            print(rez, Sep='\n')
            rez.pop()

backtr(0, 0, [])
