L=[int(x) for x in input().split(" ")]
n=L[0]
L=L[1:]
L1=[0 for i in range (101)]
for i in L:
    L1[i]=L1[i]+1
s=0
for i in range(101):
    s+=(L1[i]//2)
print(s)