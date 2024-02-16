s=input()
voc=['a', 'e', 'i', 'o', 'u']
lista=""
for c in s:
    lista+=c
    if c in voc:
        lista+='p'+c
print(lista)