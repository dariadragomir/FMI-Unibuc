s=input()
t=input()
p=s.find(t)
while p!=-1:
    print(p, s[p:p+len(t)], '\n')
    s=s[p+1:]
    p=s.find(t)