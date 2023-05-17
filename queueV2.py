
queue = [None] * 10
back = 0
front = 0

def enqueue(new):
    global back
    queue[back] = new
    back = (back+1)%10

def dequeue():
    global front
    front = (front+1)%10
    
enqueue(4)
enqueue(5)
enqueue(6)
enqueue(7)
enqueue(8)
enqueue(9)
enqueue(10)
enqueue(11)
enqueue(12)
enqueue(13)


dequeue()




print(queue)
print(queue[front:back]+ [None]*(10-len(queue[front:back])))