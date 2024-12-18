import numpy as np
import matplotlib.pyplot as plt

def signal(t): #f(t)
    return np.sin(2 * t) + 0.3 * np.cos(10 * t) + 0.05 * np.sin(100 * t)

def gaussian_density(s, sigma2):
    return (1 / np.sqrt(2 * np.pi * sigma2)) * np.exp(-s**2 / (2 * sigma2))

def polar_monte_carlo_convolution(f, sigma2, t_values, num_samples=10000):
    F_sigma2 = []
    for t in t_values:
        R = np.random.exponential(scale=np.sqrt(sigma2), size=num_samples) 
        phi = np.random.uniform(0, 2 * np.pi, num_samples)
        s_samples = R * np.cos(phi)
        integral = np.mean(f(t - s_samples) * gaussian_density(s_samples, sigma2))
        F_sigma2.append(integral)
    return np.array(F_sigma2)

t_values = np.linspace(0, 4, 1000) 
sigma2 = 0.1
num_samples = 10000

filtered_signal = polar_monte_carlo_convolution(signal, sigma2, t_values, num_samples)

plt.figure(figsize=(10, 6))
plt.plot(t_values, signal(t_values), label="semnalul f(t)", alpha=0.7)
plt.plot(t_values, filtered_signal, label=f"semnal cu filtru Fσ²(t), σ²={sigma2}", linewidth=2)
plt.title("filtru gaussian aplicat semnalului (coord polare)")
plt.xlabel("timp (s)")
plt.ylabel("amplitudine")
plt.legend()
plt.grid()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

def simulate_exponential_mean(lambda_param, N, num_simulations):
    """Simulate the empirical mean of N exponential random variables."""
    exponential_samples = np.random.exponential(1 / lambda_param, size=(num_simulations, N))
    S_N = np.mean(exponential_samples, axis=1)
    return S_N

lambda_param = 2  
N = 50  
num_simulations = 10000 

S_N = simulate_exponential_mean(lambda_param, N, num_simulations)

E_X1 = 1 / lambda_param 
VAR_X1 = 1 / (lambda_param ** 2) 

empirical_mean = np.mean(S_N)
empirical_variance = np.var(S_N)

theoretical_mean = E_X1
theoretical_variance = VAR_X1 / N

print(f"Empirical Mean of S_N: {empirical_mean:.4f}, Theoretical Mean: {theoretical_mean:.4f}")
print(f"Empirical Variance of S_N: {empirical_variance:.4f}, Theoretical Variance: {theoretical_variance:.4f}")

plt.figure(figsize=(10, 6))
counts, bins, _ = plt.hist(S_N, bins=30, density=True, alpha=0.6, color="b", label="Histogram of S_N")

mu = theoretical_mean  
sigma = np.sqrt(theoretical_variance)

def normal_density(x, mu, sigma):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

x = np.linspace(bins[0], bins[-1], 1000)
plt.plot(x, normal_density(x, mu, sigma), 'r-', label="Approximating Normal Density")

plt.title("Histogram of S_N and Approximating Density")
plt.xlabel("Value of S_N")
plt.ylabel("Density")
plt.legend()
plt.grid()
plt.show()
