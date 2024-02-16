import math
n=int(input())
k=1+int(math.log2(n))    #lungimea lui n      +1
masca=(1<<k)-1
n_invers=n^masca
ct=0
while n_invers:
    if n_invers%2==1:
        ct+=1
    n_invers=n_invers//2
print(ct)