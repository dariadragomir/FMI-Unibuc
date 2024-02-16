carti=[("Ion", "Liviu Rebreanu", 1920, 25),
       ("Engigma Otiliei", "George Calinescu", 1938, 30),
       ("Baltagul", "Mihail Sadoveanu", 1930, 20),
       ("Maitreyi", "Mircea Eliade", 1933, 18)
       #(" Frumoasele adormite", "Stephen King", "Owen King", 2001, 70)
]

def reducere20():
    for i in carti:
        if i[2]<2000:
            i[2]=i[2]*0.8

L=reducere20()
print(x for x in L)