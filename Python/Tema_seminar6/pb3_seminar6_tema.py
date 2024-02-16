def hanoi(n, sursa, destinatie, aux): 
    if n == 0: 
        return
    hanoi(n-1, sursa, aux, destinatie) 
    print("Discul", n, "se muta de pe", sursa, "pe", destinatie) 
    hanoi(n-1, aux, destinatie, sursa) 
    
hanoi(4, 'A', 'C', 'B') 