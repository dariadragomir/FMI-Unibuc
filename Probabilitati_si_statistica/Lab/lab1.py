import numpy as np
import matplotlib.pyplot as plt

num_chords = 10000

def draw_circle_and_triangle(ax):
    circle = plt.Circle((0, 0), 1, color='w', linewidth=2, fill=False)
    ax.add_patch(circle)
    ax.plot([np.cos(np.pi / 2), np.cos(7 * np.pi / 6)],
            [np.sin(np.pi / 2), np.sin(7 * np.pi / 6)], linewidth=2, color='g')
    ax.plot([np.cos(np.pi / 2), np.cos(- np.pi / 6)],
            [np.sin(np.pi / 2), np.sin(- np.pi / 6)], linewidth=2, color='g')
    ax.plot([np.cos(- np.pi / 6), np.cos(7 * np.pi / 6)],
            [np.sin(- np.pi / 6), np.sin(7 * np.pi / 6)], linewidth=2, color='g')
    plt.show()


def bertrand_simulation(method_number):
    count = 0
    ct=0
    mean=0
    plt.style.use('dark_background') 
    ax = plt.gca()
    ax.cla()
    ax.set_aspect('equal', 'box')
    ax.set_xlim((-1, 1))
    ax.set_ylim((-1, 1)) 
    for i in range(1, num_chords+1):
    
        x, y = bertrand_methods[method_number]()
    
        chord_length = np.sqrt(abs((x[0]-x[1])**2) + (abs(y[0]-y[1]))**2)
        triangle_side_length = np.sqrt(3)
        
        if chord_length > triangle_side_length:
            count += 1
        
        probability = count / i
        mean+=probability
        ct+=1
        print(probability, end='\n')
        
        if(i<1000):
            if chord_length > triangle_side_length:
                ax.plot(x, y, color='r', alpha=0.1) 
            else: 
                ax.plot(x, y, color='b', alpha=0.1)

    draw_circle_and_triangle(plt.gca())
    plt.show()
    print(f'Probabilitatea este: {mean/ct}') 
    
def bertrand1():
    theta1 = np.random.rand() *2* np.pi 
    theta2 = np.random.rand() *2* np.pi
    x=[np.cos(theta1), np.cos(theta2)]
    y=[np.sin(theta1), np.sin(theta2)]
    return x, y

def bertrand2():
    theta = np.random.rand() * 2 * np.pi
    r = np.random.rand()
    theta1 = np.arccos(r)
    theta2 = theta - np.arccos(r)
    OA = 1
    OB = r
    AB = 1-r**2
    x=[np.cos(theta - np.arccos(r)), np.cos(theta + np.arccos(r))]
    y=[np.sin(theta - np.arccos (r)), np.sin(theta + np.arccos(r))]
    
    return x, y

def bertrand3():
    while(1):
        x=np.rand()
        y=np.rand()
        if(x**2+y**2<1):
            return x, y #trebuie convertite din coordonate polare in carteziene
bertrand_methods = {1: bertrand1, 2:bertrand2, 3:bertrand3}

method_choice = int(input('Choose method to simulate: '))
bertrand_simulation(method_choice)
