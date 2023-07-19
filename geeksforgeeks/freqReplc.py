from queue import Queue

q=Queue()
q.put(4)
q.put(5)
# print(q.queue[-1])
q.get()
q.put(6)
i=0
while not q.empty():
    print(q.queue[i])
    i+=1
