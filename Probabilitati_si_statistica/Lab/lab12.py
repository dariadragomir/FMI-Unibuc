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
