a="amar"
b="mara"
ok=0
ap=[0 for i in range(125)]
for i in a:
    ap[ord(i)]+=1
for i in b:
    ap[ord(i)]-=1
for i in range(ord('A'), ord('z')+1):
    if ap[i]:
        print("nu sunt anagrame")
        ok=1
if ok==0:
    print("sunt anagrame")
