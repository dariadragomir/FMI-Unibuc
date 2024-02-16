import queue

pq_spectacole = queue.PriorityQueue()
n = int(input())

spectacole = [input().split('-') for i in range(n)]
spectacole = [(int(start), int(end)) for start, end in spectacole]

for x in spectacole:
    pq_spectacole.put(x)

rez = [pq_spectacole.get()]

while not pq_spectacole.empty():
    urmator = pq_spectacole.get()
    curent = rez[-1]
    
    if urmator[0] >= curent[1]:
        rez.append(urmator)

print(rez)
