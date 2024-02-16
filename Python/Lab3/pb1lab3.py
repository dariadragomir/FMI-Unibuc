#ciurul eratostene
n=int(input())
prime=[1 for i in range (n+1)]
for i in range (2, sqrt(n+1)):
    if prime[i]==1:
        for j in range (i*2, n+1, i):
            prime[j]=0
for i in range (2, n+1):
    if prime[i]==1:
        print(i)
