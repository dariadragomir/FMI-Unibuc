prop = "ana bana are pere prune ana pere prune ana ana ana".split()
    
freq = {
    x:prop.count(x) for x in prop
}
    

freq_list = {
    f : [x for x in freq.keys() if freq[x] == f] for f in freq.values()
}

min_freq = min(freq_list.keys())
max_freq = max(freq_list.keys())

print(min(freq_list[min_freq]), min(freq_list[max_freq]))
    