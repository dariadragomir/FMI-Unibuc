n = int(input())
A = [int(i) for i in input().split()]

def backtr(ct, rez):
    if len(rez) > 0:
        print(rez)

    for i in range(ct, n):
        if rez and rez[-1] >= A[i]:
            rez.append(A[i])
            backtr(i + 1, rez)
            rez.pop()

backtr(0, [])