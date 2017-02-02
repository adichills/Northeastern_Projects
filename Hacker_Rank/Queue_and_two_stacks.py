'''
A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.

A basic queue has the following operations:

Enqueue: add a new element to the end of the queue.
Dequeue: remove the element from the front of the queue and return it.
In this challenge, you must first implement a queue using two stacks. Then process  queries, where each query is one of the following  types:

1 x: Enqueue element  into the end of the queue.
2: Dequeue the element at the front of the queue.
3: Print the element at the front of the queue.


'''


class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []

    def peek(self):
        if (len(self.first) == 0):
            while (len(self.second) != 0):
                self.first.append(self.second.pop())
            if (len(self.first) != 0):
                return self.first[len(self.first) - 1]
        else:
            return self.first[len(self.first) - 1]

    def pop(self):
        if (len(self.first) == 0):
            while (len(self.second) != 0):
                self.first.append(self.second.pop())
            if (len(self.first) != 0):
                return self.first.pop()
        else:
            return self.first.pop()

    def put(self, value):
        self.second.append(value)


queue = MyQueue()

t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())

    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()

