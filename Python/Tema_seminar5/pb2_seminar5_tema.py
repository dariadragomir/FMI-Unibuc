proiecte = input().split()
proiecte = [int(x) for x in proiecte]
proiecte = [proiecte[i:i+2] for i in range(0, len(proiecte), 2)]
proiecte.sort(key=lambda x: (-x[0], -x[1]))

profit = 0
mx = max([proiect[0] for proiect in proiecte])
plan = {i: 0 for i in range(1, mx+2)}

for proiect in proiecte:
    for i in range(proiect[0], 0, -1):
        if plan[i] == 0:
            plan[i]=proiect[1]
            profit+=proiect[1]
            break
i = 1
while i<mx:
    if plan[i]==0:
        plan[i]=plan[i+1]
        while (plan[i+1] != 0) & (i+1<=mx):
            plan[i+1]=plan[i+2]
            i+=1
    i+=1

print(plan)
print(profit)