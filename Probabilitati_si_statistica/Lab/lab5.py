import random
import numpy as np

n = 20
def simulare_empirica(n, lungime_consecutiva, nr_simulari=10000):
    succese = 0
    for _ in range(nr_simulari):
        secventa = [random.choice(['H', 'T']) for _ in range(n)]
        secventa_str = ''.join(secventa)
        if 'H' * lungime_consecutiva in secventa_str:
            succese += 1
    return succese / nr_simulari

probabilitate_empirica_trei = simulare_empirica(n, 3)
probabilitate_empirica_patru = simulare_empirica(n, 4)
print("Probabilitate empirica trei consecutive cu siruri:", probabilitate_empirica_trei)
print("Probabilitate empirica patru consecutive cu siruri:", probabilitate_empirica_patru)

def simulare_empirica_convolutie(n, lungime_consecutiva, nr_simulari=10000):
    succese = 0
    for _ in range(nr_simulari):
        secventa = np.random.randint(0, 2, size=n)
        count_consecutive = np.convolve(secventa, np.ones(lungime_consecutiva, dtype=int), mode='valid')
        if np.any(count_consecutive == lungime_consecutiva):
            succese += 1
    return succese / nr_simulari

probabilitate_empirica_trei = simulare_empirica_convolutie(n, 3)
probabilitate_empirica_patru = simulare_empirica_convolutie(n, 4)
print("Probabilitatea empirica trei cap consecutive, convolutie:", probabilitate_empirica_trei)
print("Probabilitatea empirica patru cap consecutive, convolutie:", probabilitate_empirica_patru)

def teoretic_secv_de_3(n):
    #recursivitate: P(An) = 1/8 + 1/2*P(An-1) + 1/4*P(An-2) + 1/8*P(An-3)
    if n<3:
        return 0
    elif n==3:
        return 1/8
    return (1/8 + 
            1/2 * teoretic_secv_de_3(n-1) + 
            1/4 * teoretic_secv_de_3(n-2) + 
            1/8 * teoretic_secv_de_3(n-3))
    
print("Teoretic secventa de 3 cap", teoretic_secv_de_3(n))
def teoretic_secv_de_4(n):
    if n < 4:
        return 0
    elif n == 4:
        return 1 / 16
    
    return (1/16 + 
            1/2 * teoretic_secv_de_4(n-1) + 
            1/4 * teoretic_secv_de_4(n-2) + 
            1/8 * teoretic_secv_de_4(n-3) + 
            1/16 * teoretic_secv_de_4(n-4))
    
print("Teoretic secventa de 4 cap", teoretic_secv_de_4(n))

#ex 2
import numpy as np

def simulare_spam_loterie(nr_emailuri=100000):
    emailuri = np.random.choice([1, 0], size=nr_emailuri, p=[0.3, 0.7])
    loterie_in_spam = np.random.rand(nr_emailuri) < 0.8
    loterie_in_non_spam = np.random.rand(nr_emailuri) < 0.05
    
    loterie = np.where(emailuri == 1, loterie_in_spam, loterie_in_non_spam)
    
    # Calculăm probabilitatea empirică a evenimentului spam | loterie
    numar_spam_loterie = np.sum((emailuri == 1) & (loterie == True))
    numar_total_loterie = np.sum(loterie)
    
    # Probabilitatea ca un email cu "loterie" să fie spam
    prob_spam_given_loterie = numar_spam_loterie / numar_total_loterie if numar_total_loterie > 0 else 0
    return prob_spam_given_loterie

probabilitate_empirica = simulare_spam_loterie()
print("Probabilitatea empirica ca un email care contine 'loterie' sa fie spam este:", probabilitate_empirica)
