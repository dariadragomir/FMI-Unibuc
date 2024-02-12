s="Cifrul lui Cezar"
k=4
rezultat=""
for i in s:
    if i.isalpha():
        if i.isupper():
            rezultat += chr((ord(i)+k-65)%26+65)
        else:
            rezultat += chr((ord(i)+k-97)%26+97)
print(rezultat)
