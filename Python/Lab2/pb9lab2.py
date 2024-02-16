s=input()
i,j=0,0
nr=1
suma=0
while i<len(s):
    if s[i].isnumeric():
        nr=int(ord(s[i])-ord('0'))
        i+=1
        j=i
        while j<len(s) and s[j].isnumeric():
            nr=nr*10+int(ord(s[j])-ord('0'))
            j+=1
            i+=1
        suma+=nr
        print(suma)
    else:
        i+=1
print(suma)