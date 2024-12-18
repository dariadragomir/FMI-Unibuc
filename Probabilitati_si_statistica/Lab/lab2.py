
def ex1_a():
    lit_mici = 26
    lit_mari = 26
    cifre = 10
    total = lit_mici + lit_mari + cifre
    caractere = 8
    return total ** caractere

def ex1_b():
    parole_pe_secunda = 10**6  # 1 milion de parole pe secundă
    secunde_in_an = 60 * 60 * 24 * 365
    total_parole = ex1_a()
    timp_in_ani = total_parole / (parole_pe_secunda * secunde_in_an)

    print(f"(a) Numărul total de parole posibile este: {total_parole}")
    print(f"(b) Timpul necesar pentru a încerca toate parolele este: {timp_in_ani} ani")
    
def ex1_c():
    total_parole = ex1_a()
    parole_pe_secunda = 10**6  # 1 milion de parole pe secundă
    secunde_in_saptamana = 60 * 60 * 24 * 7
    parole_testate_pe_sapt = parole_pe_secunda * secunde_in_saptamana
    probabilitate = parole_testate_pe_sapt / total_parole
    print(f"c) Probabilitatea de a ghici parola după o săptămână de încercări este: {probabilitate}")
    
def ex1_d():
    total = 26 + 10
    caractere = 8
    parole = total ** caractere
    parole_pe_secunda = 10**6
    secunde_pe_an = 60 * 60 * 24 * 365
    timp = parole / (parole_pe_secunda * secunde_pe_an)
    secunde_pe_saptamana = 60 * 60 * 24 * 7
    parole_pe_saptamana = parole_pe_secunda * secunde_pe_saptamana
    probabilitate = parole_pe_saptamana / parole

    print(f"(d) Numărul total de parole posibile fără litere mari este: {parole}")
    print(f"(d) Timpul necesar pentru a încerca toate parolele fără litere mari este: {timp} ani")
    print(f"(d) Probabilitatea de a ghici parola după o săptămână de încercări este: {probabilitate}")

ex1_b()
ex1_c()
ex1_d()

def ex2():
    parola_caractere_distincte = 62*61*60*59*58*57*56*55
    total_parole = ex1_a()
    probabilitate1 = parola_caractere_distincte/total_parole
    parola_caractere_dist_fara_cifra = 52*61*60*59*58*57*56*55
    probabilitate2 = parola_caractere_dist_fara_cifra/total_parole
    print(f"Probabilitatea de a ghici o parolă cu 8 caractere distincte este: {probabilitate1}")
    print(f"Probabilitatea de a ghici o parolă cu 8 caractere distincte la care primul caracter nu e cifra este: {probabilitate2}")
    
def ex3():
    import math
    #3 din 10 foldere au fost infestate Combinari de 10 luate cate 3
    foldere = 10
    infestare = 3
    combinari = math.comb(foldere, infestare)
    print(combinari)
    #c de 13 luate cate 3 * comb de 7 luate cate 3  / comb de 20 luate cate 6

def combinari(n, k):
    import math
    return math.comb(n, k)
def ex5():
    def ex5_a():
        carti = 52
        asi = 4
        non_asi = 48
        carti_de_ales = 5
        asi_de_ales = 3
        non_asi_de_ales = 2

        #moduri de a alege 5 carti din 52
        total_moduri = combinari(carti, carti_de_ales)

        #moduri de a alege 3 asi din 4 si 2 carti care nu sunt asi din 48
        moduri_de_alegere_asi = combinari(asi, asi_de_ales)
        moduri_de_alegere_non_asi = combinari(non_asi, non_asi_de_ales)
        
        probabilitate = (moduri_de_alegere_asi * moduri_de_alegere_non_asi) / total_moduri
        print(f"\n5. Probabilitatea de a extrage exact 3 ași este: {probabilitate}")
        
    def ex5_b():
        # Total cărți în pachet, total ași și numărul de cărți extrase
        carti = 52
        asi = 4
        non_asi = 48
        carti_de_ales = 5

        #moduri de a alege 5 carti din 52
        total_moduri = combinari(carti, carti_de_ales)

        # probabilitatea pentru fiecare numar de asi (0, 1, 2, 3, 4)
        probabilities = []
        for k in range(5):
            ways_to_choose_aces = combinari(asi, k)
            ways_to_choose_non_aces = combinari(non_asi, carti_de_ales - k)
            probability = (ways_to_choose_aces * ways_to_choose_non_aces) / total_moduri
            probabilities.append(probability)
            print(f"Probabilitatea de a extrage {k} ași este: {probability:.6f}")

        most_probable_aces = probabilities.index(max(probabilities))

        print(f"5. b) Cel mai probabil, vei extrage {most_probable_aces} ași.")
    ex5_a()
    ex5_b()
ex5()
