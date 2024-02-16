fin = open("autostrada.in")
fout = open("autostrada.out", "a")
lg_autostrada = int(fin.readline())
intervale=[]
for i in fin:
    intervale.append([int(x) for x in i.split()])


ct=-1
reuniune=[]
intervale.sort(key=lambda x: x[0])
for inf in intervale:
    if len(reuniune)>0:
        if inf[0] <= reuniune[ct][1]:
            reuniune[ct][1] = max(reuniune[ct][1], inf[1])
        else:
            ct+=1
            reuniune.append(inf)
    else:
        ct+=1
        reuniune.append(inf)

for elem in reuniune:
    fout.write(str(elem) + '\n')
fout.write('\n')



interv_deschise = []
st=0
dr=0
for interval in reuniune:
    dr=interval[0]
    interv_deschise.append((st, dr))
    st=interval[1]

interv_deschise.append((st, lg_autostrada))

for elem in interv_deschise:
    fout.write(str(elem) + '\n')
fout.write('\n')



s=0
for interval in reuniune:
    s+=interval[1]-interval[0]
fout.write(f"{int(s/lg_autostrada * 100)}%")