import numpy as np

class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        
    def adjacencyMatrix(self):
        weightsize = [len(str(i.weight)) for i in edges]
        space = max(weightsize)
        length = len(nodes)
        row = [0 for _ in range(length)]
        matrix = np.array([row for _ in range(length)])
        for i in edges:
            matrix[nodes.index(i.source)][nodes.index(i.target)] = i.weight
            
        output = ' '*(space+1)
        for x in nodes:
             output += x.name
             output += ' '*(space)
        output += '\n'
        
        for i in range(length):
            output += nodes[i].name + ' '*(space)
            for element in matrix[i]:
                    output += str(element) + ' '*(space-len(str(element))+1)
            output += '\n'
        print(output)

class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

class Node:
    def __init__(self, name):
        self.name = name
        
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')

edge1 = Edge(A,B,20)
edge2 = Edge(A,C,24)
edge3 = Edge(B,D,423)
edge4 = Edge(C,D,1)
edge5 = Edge(C,E,3)
edge6 = Edge(D,E,6)
edge7 = Edge(E,A,2)

nodes = [A, B, C, D, E]
edges = [edge1,edge2,edge3,edge4,edge5,edge6,edge7]
graph1 = Graph(nodes, edges)

graph1.adjacencyMatrix()