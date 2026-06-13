''' queue is fifo; Front -> 1 2 3 <- Rear 
enqueue: is the operation in which add element a rear

Front -> 10 20 30 <- Rear
Enqueue(40)
Front -> 10 20 30 40 <- Rear

Dequeu: Remove element from Front.

Front -> 10 20 30 40 <- Rear
Dequeue()
Front -> 20 30 40 <- Rear

peek is to look at first element and rear is to look ar last element
'''

#QUEUE using python list
queue = []

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)

print(queue)

# Dequeue
queue.pop(0)

print(queue)

'''
list is bad for queues: suppose queue is queue = [10,20,30,40] and we do queue.pop[0]
python removes 10 and it becomes [20, 30, 40], everything shifts to left time complexity becomes O(n).
for that python provides from collection import deque that is used in bfs, graphs, trees. 
'''

from collections import deque
queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)
print(queue)  #deque([10,20,30])

queue.popleft()
print(queue)
