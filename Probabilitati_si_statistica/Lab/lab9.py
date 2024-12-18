'''
# n = nr de apartamente 
# j = cel mai bun apartament 
Sk = "gasesc apartamentul cel mai bun respingand primele k si alegand primul mai bun decat ele"
Aj = "aleg apartamentul j"
Bj = "apartamentul j este cel mai bun"
prob_aj_interesctat_bj = prob_aj_conditionat_la_bj * prob_bj
prob_aj_conditionat_la_bj = k/ (j-1)
prob_bj = 1/n 
prob_sk = 0
for j in range(k+1, n+1):
    prob_sk += k/n * a/(j-1)
    
# pentru fiecare k, plot probabilitatea ca sa aleg cel mai bun apartament 
'''

import matplotlib.pyplot as plt

n = 15  #nr de aprtamente
k_values = range(1, n)  # nr ap respinse

probabilities = []
for k in k_values:
    prob_sk = 0
    for j in range(k + 1, n + 1):
        prob_sk += (k / n) * (1 / (j - 1))  
    probabilities.append(prob_sk)

plt.figure(figsize=(10, 6))
plt.plot(k_values, probabilities, marker='o', label='P(Sk)')
plt.title("Probabilitatea de a alege cel mai bun apartament in functie de k")
plt.xlabel("k (numarul de apartamente respinse)")
plt.ylabel("Probabilitatea P(Sk)")
plt.xticks(k_values)
plt.grid(True)
plt.legend()
plt.show()
