with open("numere.txt","r") as intrare:
    numere=intrare.read()

lista_numere = numere.split()
cifre=[]
for cifra in lista_numere:
    cifre.append(cifra)

contor=0
if "0" in cifre:
    for i in range(contor):
        contor+=1
        cifre.remove("0")
cifre_sortate_desc=''.join(sorted(cifre))
#inseram 0-urile din lista sortata crescator dupa prima cifra
minim = cifre_sortate_desc[0] + "0"*contor + cifre_sortate_desc[1:]

print("Minim:", minim)
print("Maxim:", ''.join(sorted(cifre, reverse=True))+'0'*contor)
