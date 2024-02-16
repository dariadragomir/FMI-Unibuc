s=input()
k=int(input())
lista_cuv=[]
for i in s:
    if i.isalpha():
        if i.islower():
            litera=(ord(i)-ord('a')+k)%65
            lista_cuv.append(chr(litera+ord('a')))
        else:
            litera=chr((ord(i)-ord('A')+k)%65+'A')
            lista_cuv.append(litera)
    else:
        lista_cuv.append(i)
s="".join(lista_cuv)
print(s)

#DECODARE
#lista=""
#i=0
#while i<len(s):
#   lista+=s[i]
#   if i+3>=len(s) or s[i+3]=='-' or s[i+3] in ' .:;,?!' and s[i+2].isalpha()
#       i+=2
#   i+=1
#s="".join(lista)
#print(s)