import itertools
import numpy as np
import math
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)  # Add to the rear

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)  # Remove from the front

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        return f"Queue: {self.items}"
    

    def reverse_queue(self):
        temp =[]
        while not self.is_empty():
            temp.append(self.dequeue())
        for item in reversed(temp):
            self.enqueue(item)

    def contains(self, item):
        
        temp = []
        # Step 1: Dequeue all items and store in temp
        while not self.is_empty():
            val = self.dequeue()
            temp.append(val)
            print(f"dequeue: '{val}'")
        # Step 2: Check for the item and restore the queue
        found = False
        for val in temp:
            if val == item:
                print(f"val: '{val}'")
                found =  True
            #restore queue
            self.enqueue(val)
        
        return found
    
    def interleave_queues_1(self,q1, q2):
        #list comprehension
        #result = [i for sublist in zip(q1, q2) for i in sublist]
        
        
        #with itertools interleave using itertools.chain()
        #result = list(itertools.chain(*zip(q1, q2)))

        #numpy solution
        result = np.ravel(np.column_stack((q1,q2)))
        return result
        #using queue
        
#def interleave_queues_using_queue(q1,q2):
#    result = Queue()
#    while not q1.is_empty() and q2.is_empty():
#        result.enqueue(q1.dequeue())
##        result.enqueue(q2.dequeue())

    #handle left ove if queue are unequal
#    while not q1.is_empty():
#        result.enqueue(q1.dequeue())
#    while not q2.is_empty():
#        result.enqueue(q2.dequeue())
            
#        return result
    @staticmethod
    def interleave_queues_using_queue(q1,q2):
        result = Queue()
        while not q1.is_empty() and not q2.is_empty():
            i1 = q1.dequeue()
            i2 = q2.dequeue()
            print(f"dequeue1: '{i1}'")
            print(f"dequeue2: '{i2}'")
            result.enqueue(i1)
            result.enqueue(i2)
        #handle leftover if queue not the same size
        while not q1.is_empty():
            i1 = q1.dequeue()
            result.enqueue(i1)
        while not q2.is_empty():
            i2 = q2.dequeue()
            result.enqueue(i2)
        return result
    
    #def reverse_the_first_elements(self, k):
        temp = []
        reversed_fisrt = []
        while not self.is_empty():
            val = self.dequeue()
            temp.append(val)
            print(f"val: '{val}'")
        first = temp[:k]
        for val in reversed(first):
            reversed_fisrt.append(val)
        
        last = temp[k:]
        #for val in first:
        #    self.enqueue(val)
        print(f"first: '{reversed_fisrt}', last: '{last}'")
        return 
    def reverse_first_element(self,q, k):
        temp = []
        #first dequeue until k 
        for i in range(k):
            temp.append(q.dequeue())
        #2. enqueue at the end of queue
        while temp:
            q.enqueue(temp.pop())
        for i in range(q.size() - k):
            q.enqueue(q.dequeue())

    def is_queue_palindrome(self):
        first = []
        last = []
        #check first element in q is same as last element in q
        
        while not self.is_empty():
            val = self.dequeue()
            first.append(val)
            #print(f"val: '{val}'")
        for item in reversed(first):
            last.append(item)
            print(f"item: '{item}'")
        for item in first:
            self.enqueue(item)
        return first == last
        
            
    def sum_queue_keep_queue(self):
        temp = []
        result = 0
        while not self.is_empty():
            val = self.dequeue()
            temp.append(val)
        for i in temp:
            result += i
            self.enqueue(i)
        return result

   
    def interlace_queues_first_second_halves(self):
        result = []
        temp = []
        
        length = int(self.size()/2)
        while not self.is_empty():
            val = self.dequeue()
            temp.append(val)
        first = temp[:length]
        last = temp[length:]

        result = [i for sublist in zip(first, last) for i in sublist]
        for item in result:
            self.enqueue(item)
            
        return self

        
        

        

            
                
        

q = Queue()
q.enqueue(100)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(540)
#for palindrome
q.enqueue(430)
q.enqueue(30)
q.enqueue(20)
q.enqueue(100)
#q.reverse_queue()


#print(q)              # Queue: [10, 20, 30]
#print(q.dequeue())    # 10
#print(q.peek())       # 20
#print(q.size())       # 2
#print(q.is_empty())
#print(q.contains(20))
#q1 = Queue()
#q1.enqueue(1)
#q1.enqueue(2)
#q1.enqueue(3)
#q2 = Queue()
#q2.enqueue(4)
#q2.enqueue(5)
#q2.enqueue(6)
#print(q1, q2)
#q1 = [1,2,3]
#q2 = [3,4,5]
#print(q.interleave_queues_1(q1,q2))
#result = Queue.interleave_queues_using_queue(q1,q2)
#print("result:",result)
#print(q.reverse_first_element(q,3))
#print(q)
#print(q.is_queue_palindrome())
#print(q.sum_queue_keep_queue())
#print(q)
print(q.interlace_queues_first_second_halves())








