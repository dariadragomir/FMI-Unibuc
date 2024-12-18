import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
def needle_dropping(num_drops=10000, needle_length=1, line_spacing=2):
    def setup_figure(ax):
        ax.cla()
        ax.set_aspect('equal', 'box')
        ax.set_xlim((-2 - needle_length / 2, 2 + needle_length / 2)) 
        ax.set_ylim((-(line_spacing + needle_length) / 2, 
                    (line_spacing + needle_length) / 2))

    def draw_lines(ax):
        ax.axhline(line_spacing / 2, color='g', linewidth=1)
        ax.axhline(-line_spacing / 2, color='g', linewidth=1)

    def draw_needle(ax, center_x, center_y, angle, intersects):
        x = [
            center_x - 0.5 * needle_length * np.cos(angle),
            center_x + 0.5 * needle_length * np.cos(angle)
        ]
        y = [
            center_y - 0.5 * needle_length * np.sin(angle),
            center_y + 0.5 * needle_length * np.sin(angle)
        ]
        color = 'blue' if intersects else 'red'
        ax.plot(x, y, color=color)

    fig, ax = plt.subplots()
    setup_figure(ax)
    draw_lines(ax)

    intersections = 0
    for _ in range(num_drops):
        center_x = np.random.uniform(-2, 2)
        center_y = np.random.uniform(-line_spacing / 2, line_spacing / 2)
        angle = np.random.uniform(0, np.pi)
        delta_y = (needle_length / 2) * np.sin(angle)
        
        intersects = (center_y + delta_y >= line_spacing / 2) or (center_y - delta_y <= -line_spacing / 2)
        if intersects:
            intersections += 1
        draw_needle(ax, center_x, center_y, angle, intersects)

    empirical_prob = intersections / num_drops
    theoretical_prob = (2 * needle_length) / (line_spacing * np.pi)

    print(f"Empirical probability: {empirical_prob}")
    print(f"Theoretical probability: {theoretical_prob}")

    plt.show()

    estimated_pi = (2 * needle_length) / (line_spacing * empirical_prob)
    print(f"Approximated π: {estimated_pi}")

needle_dropping()

def f(x):
    return np.sin(1 / (x + 0.01))

N_sample = 1000 
x_samples = np.random.uniform(0, 1, N_sample)
f_samples = f(x_samples)
mean_f = np.mean(f_samples)
variance = np.var(f_samples)

epsilon = 1e-2  
z = 1.96 
N = int((z * np.sqrt(variance) / epsilon) ** 2)
print(f"numarul necesar de mostre pentru eroare mai mica de {epsilon}: {N}")

x_final_samples = np.random.uniform(0, 1, N)
integral_estimate = np.mean(f(x_final_samples))
print(f"estimarea integralei: {integral_estimate}")
