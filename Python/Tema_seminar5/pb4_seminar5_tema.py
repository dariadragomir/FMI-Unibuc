A = input().split()
A = [float(x) for x in A]
elem = float(input())

if elem == 0:
    print(max(A))
elif elem > 0:
    A.sort(reverse=True)
    print(A)
else:
    pozitive = [x for x in A if x > 0]
    pozitive.sort(reverse=True)
    st_poz = 0
    dr_poz = len(pozitive) - 1
    negative = [x for x in A if x <= 0]
    negative.sort()
    st_neg = 0
    dr_neg = len(negative) - 1
    rez = []
    for i in range(len(A)-1, -1, -1):
        if i % 2 == 0:
            if st_poz <= dr_poz:
                rez.append(pozitive[st_poz])
                st_poz += 1
            else:
                rez.append(negative[dr_neg])
                dr_neg -= 1
        else:
            if st_neg <= dr_neg:
                rez.append(negative[st_neg])
                st_neg += 1
            else:
                rez.append(pozitive[dr_poz])
                dr_poz -= 1
    print(rez)