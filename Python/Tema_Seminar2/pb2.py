A=[]
n=int(input())
if n==1:
    x=int(input())
    print(x)
    exit(0)
for i in range (0, n):
    A.append(int(input()))
#fiecare element apare de 2^(n-1) ori, adica de un nr par de ori, pt n>=2
# -> se anuleaza
print("0")