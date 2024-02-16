x=int(input())
y=int(input())
while y:    #pana se citeste 0
    x=x^y
    y=x
    y=int(input())
print(x)
