queue = [None] * 10
front = 0
back = 0
empty = []

def enqueue(new):
    global back
    empty = [i for i in range(len(queue)) if queue[i] == None]
    queue[min(empty)] = new
    print(empty)
    back = min(empty)
    
def dequeue():
    global queue
    global back
    empty = [i for i in range(len(queue)) if queue[i] == None]
    queue = [queue[i] for i in range(1,len(queue)-1)] + [None]
    print(empty)
    back  = min(empty)
    
    
    
enqueue(3)
enqueue(9)
enqueue(132)
enqueue(2)

print(queue)
print(front,back)

    

