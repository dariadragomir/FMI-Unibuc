import numpy as np
import matplotlib.pyplot as plt
import time 
def ex1():
    def a():
        n_trials = 10000
        heads_count = np.sum(np.random.random(n_trials) < 0.5)
        print(f"Numarul de 'cap' pentru o moneda echilibrata: {heads_count} din {n_trials}")

    def b():
        n_trials = 10000
        trials = list(range(100, n_trials + 1, 100))
        proportions = [np.sum(np.random.random(t) < 0.5) / t for t in trials]
    
        plt.figure(figsize=(10, 6))
        plt.plot(trials, proportions, label='Proporție de "cap"', color='blue')
        plt.axhline(0.5, color='red', linestyle='--', label='50%')
        plt.xlabel('Numarul de aruncari')
        plt.ylabel('Proportie de "cap"')
        plt.title('Tendita proportiei de "cap" pentru moneda echilibrata')
        plt.legend()
        plt.grid(True)
        plt.show()

    def c():
        n_trials = 10000
        trials = np.arange(100, n_trials + 1, 100)
        biased_heads_count = np.sum(np.random.random(n_trials) < 0.75)
        print(f"Numarul de 'cap' pentru o moneda masluita: {biased_heads_count} din {n_trials}")

        biased_proportions = [np.sum(np.random.random(t) < 0.75) / t for t in trials]

        plt.figure(figsize=(10, 6))
        plt.plot(trials, biased_proportions, label='Proporție de "cap" (măsluită)', color='green')
        plt.axhline(0.75, color='red', linestyle='--', label='75%')
        plt.xlabel('Numarul de aruncari')
        plt.ylabel('Proportie de "cap"')
        plt.title('Tendinta proportiei de "cap" pentru moneda masluita')
        plt.legend()
        plt.grid(True)
        plt.show()
    
    return a, b, c

a1, b1, c1 = ex1()
t1=time.time()
a1()
t2=time.time()
print(t2-t1)
b1()
c1()

def ex2():
    def a2():
        n_trials = 10000
        rolls = np.floor(np.random.random(n_trials) * 6) + 1
        six_count = np.sum(rolls == 6)
        print(f"\nex2. Numarul de '6' pentru un zar echilibrat: {six_count} din {n_trials}")

    def b2():
        n_trials = 10000
        trials = np.arange(100, n_trials + 1, 100)
        proportions = {i: [] for i in range(1, 7)}
        
        for t in trials:
            rolls = np.floor(np.random.random(t) * 6) + 1
            for i in range(1, 7):
                proportions[i].append(np.sum(rolls == i) / t)
        
        plt.figure(figsize=(10, 6))
        for i in range(1, 7):
            plt.plot(trials, proportions[i], label=f'Proporție de "{i}"')
        plt.axhline(1/6, color='red', linestyle='--', label='1/6 (16.67%)')
        plt.xlabel('Numărul de aruncări')
        plt.ylabel('Proporție')
        plt.title('Tendința proporției pentru zarul echilibrat')
        plt.legend()
        plt.grid(True)
        plt.show()

    def c2():
        def roll_biased_die():
            r = np.random.random()
            if r < 1/3:
                return 1
            elif r < 1/3 + 2/9:
                return 2
            elif r < 1/3 + 4/9:
                return 5
            else:
                return 6
                
        n_trials = 10000
        counts = {1: 0, 2: 0, 5: 0, 6: 0}
        biased_proportions = {1: [], 2: [], 5: [], 6: []}
        x_values = []

        for i in range(1, n_trials + 1):
            result = roll_biased_die()
            if result in counts:
                counts[result] += 1

            if i % 100 == 0:
                for num in counts:
                    biased_proportions[num].append(counts[num] / i)
                x_values.append(i)

        plt.figure(figsize=(10, 6))
        for i in [1, 2, 5, 6]:
            plt.plot(x_values, biased_proportions[i], label=f'Proporție de "{i}"')
        plt.axhline(1/3, color='blue', linestyle='--', label='33.33% pentru "1"')
        plt.axhline(2/9, color='green', linestyle='--', label='22.2% pentru "2", "5", "6"')
        plt.xlabel('Numărul de aruncări')
        plt.ylabel('Proporție')
        plt.title('Tendința proporției pentru zarul măsluit')
        plt.legend()
        plt.grid(True)
        plt.show()

    return a2, b2, c2

a2, b2, c2 = ex2()
a2()
b2()
c2()

def ex3():
    red_die = [2, 2, 2, 5, 5, 5]
    green_die = [3, 3, 3, 3, 3, 6]
    black_die = [1, 4, 4, 4, 4, 4]

    def win_probability(die1, die2):
        win_count = 0
        total_count = len(die1) * len(die2)
        for face1 in die1:
            for face2 in die2:
                if face1 > face2:
                    win_count += 1
        return win_count / total_count
    
    
    red_vs_green = win_probability(red_die, green_die)
    red_vs_black = win_probability(red_die, black_die)
    green_vs_black = win_probability(green_die, black_die)
    green_vs_red = 1 - red_vs_green
    black_vs_red = 1 - red_vs_black
    black_vs_green = 1 - green_vs_black

    print("\nex3. Probabilități teoretice:")
    print(f"Roșu vs Verde: {red_vs_green:.2f}")
    print(f"Roșu vs Negru: {red_vs_black:.2f}")
    print(f"Verde vs Negru: {green_vs_black:.2f}")
    print(f"Verde vs Roșu: {green_vs_red:.2f}")
    print(f"Negru vs Roșu: {black_vs_red:.2f}")
    print(f"Negru vs Verde: {black_vs_green:.2f}")

    n_simulations=10000
    red_wins = green_wins = black_wins = 0
    
    for _ in range(n_simulations):
        red_roll = np.random.choice(red_die)
        green_roll = np.random.choice(green_die)
        black_roll = np.random.choice(black_die)
        
        if red_roll > green_roll:
            red_wins += 1
        else:
            green_wins += 1
        
        if red_roll > black_roll:
            red_wins += 1
        else:
            black_wins += 1
        
        if green_roll > black_roll:
            green_wins += 1
        else:
            black_wins += 1
    
    print("\nRezultatele simulării:")
    print(f"Roșu câștigă: {red_wins / (2 * n_simulations)}")
    print(f"Verde câștigă: {green_wins / (2 * n_simulations)}")
    print(f"Negru câștigă: {black_wins / (2 * n_simulations)}")
    
ex3()

np.random.seed(0)
print(np.random.random())
print(np.random.random())
