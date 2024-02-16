x=int(input())
y=int(input())
t=x^y
ct=0
while t:
    if t%2==1:
        ct+=1
    t=t//2
print(ct)