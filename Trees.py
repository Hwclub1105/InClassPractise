class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def pre_order_traversal(self):
        text.append(self.value)
        
        if tree[self.left].value != None:
            tree[self.left].pre_order_traversal()
        
        if tree[self.right].value != None:
            tree[self.right].pre_order_traversal()
                 
    def in_order_traversal(self):
        if tree[self.left].value != None:
            tree[self.left].in_order_traversal()
        
        text.append(self.value)
        
        if tree[self.right].value != None:
            tree[self.right].in_order_traversal()
                 
    def post_order_traversal(self):
        if tree[self.left].value != None:
            tree[self.left].post_order_traversal()
        
        if tree[self.right].value != None:
            tree[self.right].post_order_traversal()
        
        text.append(self.value)
        
        
treeV = [                           '-',
                    '+',                             '/',
         '*',               '+',            '/',                '^',
    '5',     '2',       '7',     '9',    '2',   '1',        '3',    '7',
    None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]

#((5*2)+(7+9))-((2/1)/(3^7))

tree = [Node(treeV[0],1,2), Node(treeV[1],3,4), Node(treeV[2],5,6), Node(treeV[3],7,8), Node(treeV[4],9,10), Node(treeV[5],11,12), Node(treeV[6],13,14)]
tree = [Node(treeV[i], (2*i)+1, (2*i)+2) for i in range(len(treeV))]

text = []
tree[0].in_order_traversal()
print(''.join(text))

text = []
tree[0].in_order_traversal()
print('')

tree[0].post_order_traversal()
print('')



