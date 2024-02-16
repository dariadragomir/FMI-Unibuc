matrice = []
n=3
m=4
for i in range(n):
    list = []
    for j in range(m):
        list.append(i + j)
    matrice.append(list)

x=6

def met1():
    for i in matrice:
        for j in i:
            if matrice[i][j] == x:
                return i, j
    return 0

def met2():
    for i in range(len(matrice)):
        st = 0
        dr = len(matrice[i])
        while st < dr:
            mij = (st+dr)//2
            if matrice[i][mij] == x:
                return i, mij
            elif matrice[i][mij] < x:
                st = mij+1
            else:
                dr = mij-1


def met3():
    lin = len(matrice) - 1
    col = 0
    while (lin >= 0)&(col < len(matrice[0])):
        if matrice[lin][col] == x:
            return lin, col
        elif matrice[lin][col] < x:
            col+=1
        else:
            lin-=1
    return 0

met3()