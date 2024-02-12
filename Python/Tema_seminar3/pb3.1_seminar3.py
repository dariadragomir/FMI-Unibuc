import re
with open("exemplu.txt","r") as intrare:
    text=intrare.read()

cuvinte=set(re.findall("\w+",text))

lungimi_cuvinte={}
for cuvant in cuvinte:
    lungime=len(cuvant)
    if lungime in lungimi_cuvinte:
        lungimi_cuvinte[lungime].append(cuvant)
    else:
        lungimi_cuvinte[lungime]=[cuvant]

dictionar_sortat=dict(sorted(lungimi_cuvinte.items(),reverse=True))

with open("grupe_cuvinte","w") as iesire:
    for lungime in dictionar_sortat:
        dictionar_sortat.get(lungime).sort()
        cuvant_string=", ".join(dictionar_sortat.get(lungime))
        iesire.write(f"Lungime {lungime}: {cuvant_string.lower()}\n")