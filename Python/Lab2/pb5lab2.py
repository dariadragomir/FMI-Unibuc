prop=input()
s=input()
t=input()
nr1=prop.count(s)
nr2=int(input())  #p
sir=prop.replace(s, t, nr2)
print(sir)
if nr1>nr2:
    print(f"textul contine prea multe greseli, doar {nr2} au fost corectate")