fin = open("test.in", "r")

cuvinte = "".join(fin.readlines()).split()
    
d = {x[-2:] : sorted([y for y in cuvinte if y.endswith(x[-2:])]) for x in cuvinte}
    # for x in cuvinte:
    #     d[x[-2:]] = []

    # for x in cuvinte:
    #     d[x[-2:]].append(x)

    # for x in d.keys():
    #     d[x].sort()
print(d)    