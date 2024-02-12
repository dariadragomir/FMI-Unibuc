s="Propozitie Cu Semne ,.:?"
semne=[",", "!", "?", ".", ";", ":"]
litere_mici=0
litere_mari=0
semne_punctuatie=0
for i in s:
    if i.islower():
        litere_mici+=1
    if i.isupper():
        litere_mari+=1
    if i in semne:
        semne_punctuatie+=1
print("litere mici:", litere_mici)
print("litere mari", litere_mari)
print("semne punctuatie", semne_punctuatie)
