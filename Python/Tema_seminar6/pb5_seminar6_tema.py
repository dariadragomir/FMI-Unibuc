n = int(input())
A = [int(i) for i in input().split()]
s = int(input())
dp = [[0 for i in range(0, s + 1)] for j in range(0, n + 1)]
rez = []

for i in range(n + 1):
    dp[i][0] = 1

for i in range(1, n + 1):
    for j in range(1, s + 1):
        if j < A[i - 1]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j - A[i - 1]] + dp[i - 1][j]

lin = n
col = s
while lin > 0 & col > 0:
    if dp[lin - 1][col]:
        lin -= 1
    else:
        rez.append(A[lin - 1])
        lin -= 1
        col -= A[lin - 1]

print(rez[::-1])