d1 = {
    'A': 1,
    'B': 2
}

d2 = {
    'B': 3,
    'C': 2
}

d = {
    x : d1.get(x, 0) + d2.get(x, 0) for x in d1.keys() | d2.keys()
}

print(d)