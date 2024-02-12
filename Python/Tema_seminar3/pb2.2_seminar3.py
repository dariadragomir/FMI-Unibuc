import re
s=input()
list=[]
x=re.findall("[\w]+", s)

for element in x:
    list.append(element)
multime=set(list)
print(len(multime))
