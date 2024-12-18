import numpy as np
import matplotlib.pyplot as plt

def geometric_mean_bernoulli(x, p):
    geometric_mean = np.prod(np.power(x, p))
    return geometric_mean

x = np.array([1, 2, 6, 22, 200, 1000000]) #valorile
p = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])  # probabilitatile

result = geometric_mean_bernoulli(x, p)
print("Media geometrica a variabilei Bernoulli:", result)

w = 100000
#ce proportie alfa apartine[0,1] din suma initiala de w = 1000000 ar trebui sa platesc penru X ai sa raman cu media Bernouli 100000?
#alfa=? 
#BEV[x+(1-alfa)w] = w 
#pt w platesc alfa*w pt X

alpha_values = []
bev_values = []
def find_alpha(x, p, w, abatere=10**(-3)):
    left, right = 0, 1 
    alpha = (left + right)
    new_x = x + (1 - alpha) * w
    bev = geometric_mean_bernoulli(new_x, p)        
    alpha_values.append(alpha)
    bev_values.append(bev)
    
    while right - left > abatere:
        alpha = (left + right) / 2
        new_x = x + (1 - alpha) * w
        bev = geometric_mean_bernoulli(new_x, p)
        alpha_values.append(alpha)
        bev_values.append(bev)
        if abs(bev - w) < abatere:
            return alpha
        elif bev < w:
            right = alpha
        else:
            left = alpha
            
    return (left + right) / 2

alpha = find_alpha(x, p, w)
print("alpha=", alpha)
def plot():
    plt.figure(figsize=(10, 6))
    plt.plot(alpha_values, bev_values, label="BEV[X + (1 - alpha) * w]")
    plt.axhline(y=w, color='r', linestyle='--', label=f"w = {w}")
    plt.xlabel("alpha")
    plt.ylabel("bev")
    plt.title("graficul functiei BEV in functie de alpha")
    plt.legend()
    plt.grid(True)
    plt.show()
    
plot()
