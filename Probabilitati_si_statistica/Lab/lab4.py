import random
import matplotlib.pyplot as plt
def ex1(change_choice):
    castig = 0
    n = 10000
    for i in range(n):
        masina = random.randint(0, 2)
        alegere = random.randint(0, 2)
        posibilitati_host = [door for door in range(3) if door != alegere and door != masina]
        host = random.choice(posibilitati_host)
        
        if change_choice:
            alegere = [door for door in range(3) if door != alegere and door != host][0]
        if alegere == masina:
            castig += 1
    return castig / n

castiguri_schimb = ex1(change_choice=True)
castiguri_fara_schimb = ex1(change_choice=False)

print(f"Castigul cand schimbi: {castiguri_schimb * 100}%")
print(f"Castigul cand nu schimbi: {castiguri_fara_schimb * 100}%")


import random
import matplotlib.pyplot as plt

def ex1(change_choice):
    castig = 0
    n = 10000
    for i in range(n):
        masina = random.randint(0, 2)
        alegere = random.randint(0, 2)
        posibilitati_host = [door for door in range(3) if door != alegere and door != masina]
        host = random.choice(posibilitati_host)
        
        if change_choice:
            alegere = [door for door in range(3) if door != alegere and door != host][0]
        if alegere == masina:
            castig += 1
    return castig / n

def plot(n_games):
    castig_schimb = []
    castig_fara_schimb = []
    suma_schimb = 0
    suma_fara_schimb = 0
    
    for i in range(1, n_games + 1):
        masina = random.randint(0, 2)
        alegere = random.randint(0, 2)
        posibilitati_host = [door for door in range(3) if door != alegere and door != masina]
        host = random.choice(posibilitati_host)
        
        change_alegere = [door for door in range(3) if door != alegere and door != host][0]
        if change_alegere == masina:
            suma_schimb += 1
            
        if alegere == masina:
            suma_fara_schimb += 1
            
        castig_schimb.append((suma_schimb / i) * 100)
        castig_fara_schimb.append((suma_fara_schimb / i) * 100)
    
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, n_games + 1), castig_schimb, label='schimbi alegerea', color='blue')
    plt.plot(range(1, n_games + 1), castig_fara_schimb, label='nu schimbi alegerea', color='orange')
    
    plt.xlabel('n')
    plt.ylabel('procent castig (%)')
    plt.legend()
    plt.grid(True)
    
    plt.show()
plot(n_games=1000)

import random
import matplotlib.pyplot as plt

def ex1_generalized(k, change_choice):
    castig = 0
    n = 10000
    for i in range(n):
        masina = random.randint(0, k - 1)
        alegere = random.randint(0, k - 1)
        # Host will reveal one of the non-winning and non-chosen doors
        posibilitati_host = [door for door in range(k) if door != alegere and door != masina]
        host = random.choice(posibilitati_host)
        
        if change_choice:
            # Player changes choice to one of the remaining doors (excluding initial choice and host's revealed door)
            alegere = [door for door in range(k) if door != alegere and door != host][0]
        
        if alegere == masina:
            castig += 1
    return castig / n

def plot_generalizat(k, n_games):
    castig_schimb = []
    castig_fara_schimb = []
    suma_schimb = 0
    suma_fara_schimb = 0
    
    for i in range(1, n_games + 1):
        masina = random.randint(0, k - 1)
        alegere = random.randint(0, k - 1)
        posibilitati_host = [door for door in range(k) if door != alegere and door != masina]
        host = random.choice(posibilitati_host)
        
        change_alegere = [door for door in range(k) if door != alegere and door != host][0]
        if change_alegere == masina:
            suma_schimb += 1
            
        if alegere == masina:
            suma_fara_schimb += 1
            
        castig_schimb.append((suma_schimb / i) * 100)
        castig_fara_schimb.append((suma_fara_schimb / i) * 100)
    
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, n_games + 1), castig_schimb, label='schimbi alegerea', color='blue')
    plt.plot(range(1, n_games + 1), castig_fara_schimb, label='nu schimbi alegerea', color='orange')
    
    plt.xlabel('n')
    plt.ylabel('procent castig (%)')
    plt.title(f'generalizare numar de usi (k={k})')
    plt.legend()
    plt.grid(True)
    
    plt.show()

plot_generalizat(k=8, n_games=1000)
