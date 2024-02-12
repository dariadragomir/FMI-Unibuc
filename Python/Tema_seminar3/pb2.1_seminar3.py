a="amar"
b="mara"
d={}
ok=0 #sunt anagrame
ap=[0 for i in range(125)]
for i in a:
    ap[ord(i)]+=1
for i in b:
    ap[ord(i)]-=1
for i in range(ord('A'), ord('z')+1):
    if ap[i]:
        ok=1 #nu sunt anagrame
        break
if ok==0:
    for i in range(len(a)):
        poz=b.find(a[i])
        b=b.replace(a[i], " ", 1)
        d[i+1]=poz+1
print(d)