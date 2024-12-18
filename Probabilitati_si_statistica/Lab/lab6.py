import numpy as np
import matplotlib.pyplot as plt

N = 10**5
n = 10
p = 0.3
def bernoulli(p, N):
    X = (np.random.random(N) < p)
    return X

def binomial(n, p, N):
    X = np.sum(np.random.random((N, n)) < p, axis = 1)
    return X

def geometric_varianta_aproximare_poisson(p, N):
    X = np.ceil(np.log(1 - np.random.random(N)) / np.log(1 - p)).astype(int)
    return X

def geometric(p, N):
    X = np.zeros(N, dtype=int)
    for i in range(N):
        numar_incercari = 0
        while True:
            numar_incercari += 1
            if np.random.random() < p:
                break 
        X[i] = numar_incercari
    return X
    
X_bernoulli = bernoulli(p, N)
X_binomial = binomial(n, p, N)
X_geometric = geometric(p, N)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

axes[0].hist(X_bernoulli, bins=[-0.5, 0.5, 1.5], density=True, edgecolor='red')
axes[0].set_xticks([0, 1])
axes[0].set_title(f'Bernoulli(p={p})')

axes[1].hist(X_binomial, bins=np.arange(-0.5, n + 1.5, 1), density=True, edgecolor='red')
axes[1].set_xticks(np.arange(0, n + 1))
axes[1].set_title(f'Binomiala(n={n}, p={p})')

max_geometric = np.max(X_geometric)
axes[2].hist(X_geometric, bins=np.arange(0.5, max_geometric + 1.5, 1), density=True, edgecolor='red')
axes[2].set_xticks(np.arange(1, min(max_geometric, 20) + 1))
axes[2].set_xlim(1, min(max_geometric, 20))
axes[2].set_title(f'Geometrica(p={p})')

plt.show()
