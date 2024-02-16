prop = "Langa o cabana stand pe o banca un bacan a spus un banc bun".split()
x = "bacan"

ans = [y for y in prop if set(x) == set(y)]

print(ans)