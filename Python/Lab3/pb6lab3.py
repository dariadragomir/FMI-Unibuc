l = [1, 2, 3, 4]
ans = [(l[i], l[i + 1]) for i in range(len(l) - 1)]

print(ans)