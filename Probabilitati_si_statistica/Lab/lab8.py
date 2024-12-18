import numpy as np
import matplotlib.pyplot as plt
fonduri_initiale = 1
numar_simulari = 3000

def aruncare_zar():
    probabilitate = np.random.random()
    
    if probabilitate < 1/6:
        return 1
    elif probabilitate < 2/6:
        return 2
    elif probabilitate < 3/6:
        return 3
    elif probabilitate < 4/6:
        return 4
    elif probabilitate < 5/6:
        return 5
    else:
        return 6

def simulare(fonduri_initiale, numar_simulari):
    fonduri = fonduri_initiale
    fonduri_rezultat = [fonduri]
    
    for _ in range(numar_simulari):
        roll = aruncare_zar()
        if roll == 6:
            fonduri *= 1.5
        elif roll in [2, 3, 4, 5]:
            fonduri *= 1.05
        elif roll == 1:
            fonduri *= 0.5
        fonduri_rezultat.append(fonduri)
    
    return fonduri_rezultat

def E():
    return (1/6 * 1.5 + 4/6 * 1.05 + 1/6 * 0.5)

def BEV():
    return (1.5 * 1.05**4 * 0.5)**(numar_simulari/6)

media_aritmetica = E()
media_geometrica = BEV()

print(f"Media aritmetica teoretica: {media_aritmetica:.4f}")
print(f"Media geometrica teoretica: {media_geometrica:.4f}")

fonduri_rezultat = simulare(fonduri_initiale, numar_simulari)

final_fonduri = fonduri_rezultat[-1]
print(f"Fonduri finale dupa {numar_simulari} pariuri: {final_fonduri:.2f}")

plt.plot(fonduri_rezultat, label="Fonduri")
plt.axhline(fonduri_initiale, color='red', linestyle='--', label="Fonduri initiale")
plt.title("Evolutia fondurilor pe parcursul jocului")
plt.xlabel("Pariu")
plt.ylabel("Fonduri")
plt.legend()
plt.show()
