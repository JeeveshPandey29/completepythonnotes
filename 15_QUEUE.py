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
print(queue) #deque([20, 30])

# Queue using class
from collections import deque #deque allows fast appends and pops from both ends (O(1) time complexity).

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if self.is_empty():
            return "Queue Empty"

        return self.queue.popleft()

    def front(self):
        if self.is_empty():
            return "Queue Empty"

        return self.queue[0]

    def rear(self):
        if self.is_empty():
            return "Queue Empty"

        return self.queue[-1]

    def is_empty(self):
        return len(self.queue) == 0


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())
print(q.front())
print(q.rear())


'''  

A circular queue is a special type of queue where the last position connects 
back to the first position, forming a circle. Wrap around means that the queue indices reset to the start 
when they reach the end.

move front: front = (front + 1) % size
move rear: rear = (rear + 1) % size

'''

'''

Dequeue is double ended queue. Normal Queue has 
Enqueue  -> Rear
Dequeue  -> Front

Dequeue has
Insert Front  ✅
Insert Rear   ✅

Delete Front  ✅
Delete Rear   ✅

Front <-> 10 20 30 <-> Rear

'''

from collections import deque
d = deque()

d.append(10)
d.append(20)
d.append(30)
print(d)  #deque([10, 20, 30])

d.appendleft(5)
print(d) #deque([5, 10, 20, 30])

d.popleft()
d.pop() # 10 20  


# Python heap
import heapq
heap = []

heapq.heappush(heap, 30)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)

print(heap) 

''' 
internally smallest element stays at top [10, 30, 20] 
Start: heap = []

heappush(heap, 30) → [30]  
(only one element, so heap property holds)

heappush(heap, 10) → [10, 30]  
(10 is smaller, so it becomes the root)

heappush(heap, 20) → [10, 30, 20]  
(heap property: smallest element 10 stays at index 0)

'''
# remove smallest element 
print(heapq.heappop(heap))

