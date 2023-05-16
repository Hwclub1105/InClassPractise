class Node:
    def __init__(self,value,nextOne):
        self.nextOne = nextOne
        self.value = value
    
    def pointToNext(self):
        global pointer
        pointer = self.nextOne

memory = [Node(16,7),Node(8,12),Node(7,None),Node(5,8),Node(12,16)]
pointer = 0

def showList(head):
    global pointer
    linked = []
    pointer = head
    while True:
        if pointer == None:
            break
        i = 0
        while pointer != memory[i].value and i < len(memory):
            i+=1
        linked.append(memory[i].value)
        memory[i].pointToNext()
    return linked

def addNode(node):
    global memory
    memory.append(node)
    x = 0
    while memory[x].nextOne != node.nextOne:
        x += 1 
    memory[x].nextOne = node.value
        
        
        
        
addNode(Node(25,12))
print(showList(5))
