import copy

# class Node:
#     def __init__(self,data):
#         self.key = data

# class Edge:
#     def __init__(self,fromNode,toNode):
#         self.fromNode = fromNode
#         self.toNode = toNode

class Graph:
    def __init__(self, nodeList, adjacencyList):
        self.nodeList = nodeList
        self.adjacencyList = adjacencyList

    def addNode(self):
        adj = self.adjacencyList
        nodes = self.nodeList
        
        newNode = Node(len(nodes)) 
        nodes.append(newNode)

        newList = []
        adj.append(newList)
        
        # self.adjacencyList = adj
        # self.nodeList = nodes

    # def addEdge(self, fromNode, toNode, directed = False):
    #     adj = self.adjacencyList
    #     nodes = self.nodeList

    #     newEdge = Edge(fromNode,toNode)
    #     adj[fromNode.key].append(newEdge)

    #     if(directed == False):
    #         newReverseEdge = Edge(toNode,fromNode)
    #         adj[toNode.key].append(newReverseEdge)
    def addEdge(self, edge, directed = False):
        adj = self.adjacencyList
        nodes = self.nodeList

        toNode = edge.toNode
        fromNode = edge.fromNode
        
        adj[fromNode.key].append(edge)

        if(directed == False):
            newReverseEdge = Edge(toNode,fromNode)
            adj[toNode.key].append(newReverseEdge)

    # def removeEdge(self, fromNode, toNode, directed = False):
    #     self.removeEdgeFromList(fromNode, toNode)
    #     if(directed == False):
    #         self.removeEdgeFromList(toNode, fromNode)
    
    def removeEdge(self, edge, directed = False):
        
        toNode = edge.toNode
        fromNode = edge.fromNode
        
        self.removeEdgeFromList(fromNode, toNode)
        if(directed == False):
            self.removeEdgeFromList(toNode, fromNode)

    def removeEdgeFromList(self, fromNode, toNode):
        adj = self.adjacencyList[fromNode.key]
        newAdj = []
        for i in range(len(adj)):
            if(adj[i].toNode.key != toNode.key):
                newAdj.append(adj[i])
        self.adjacencyList[fromNode.key] = newAdj

    def removeNode(self, node):
        newIndex = [-1 for i in range(len(self.nodeList))]
        indexCounter = 0
        for i in range(len(self.nodeList)):
            if(i != node.key):
                newIndex[i] = indexCounter
                indexCounter = indexCounter + 1

        #create modified adjacency list
        adj = [] 
        currentSize = 0
        for i in range(len(self.adjacencyList)):
            
            if(i != node.key):
                currentSize = currentSize + 1
                adj.append([])

                for j in range(len(self.adjacencyList[i])):
                    if(self.adjacencyList[i][j].toNode.key != node.key):
                        modifiedEdge = copy.deepcopy(self.adjacencyList[i][j])
                        modifiedEdge.fromNode.key = newIndex[modifiedEdge.fromNode.key]
                        modifiedEdge.toNode.key = newIndex[modifiedEdge.toNode.key]
                        adj[currentSize - 1].append(modifiedEdge) 
                
                
        #create modified nodeList
        nodes = []
        for i in range(len(self.nodeList)):
            if(self.nodeList[i].key != node.key):
                modifiedNode = self.nodeList[i]
                modifiedNode = newIndex[modifiedNode.key]
                nodes.append(modifiedNode)

        self.adjacencyList = adj
        self.nodeList = nodes

    def printAdjList(self):
        for i in range(len(self.adjacencyList)):
            print('adj - ' + str(i) + ':', end = ' ')
            for j in range(len(self.adjacencyList[i])):
                print(self.adjacencyList[i][j].toNode.key,end = ' ')
            print()

# def test():
#     g = Graph()
#     g.addNode() # 1
#     # print(len(g.adjacencyList[0]))
#     # print(len(g.nodeList))
#     g.addNode() # 2
#     # print(len(g.nodeList))
#     g.addNode() # 3
#     g.addNode() # 4
#     g.addNode() # 5
#     g.addEdge(g.nodeList[0],g.nodeList[1])
#     g.addEdge(g.nodeList[1],g.nodeList[2])
#     g.addEdge(g.nodeList[1],g.nodeList[3])
#     g.addEdge(g.nodeList[4],g.nodeList[2])
#     g.addEdge(g.nodeList[3],g.nodeList[2])
#     # g.addEdge(g.nodeList[2],g.nodeList[1])
#     # print(len(g.nodeList))
#     # for i in range(len(g.nodeList)):
#     #     print(g.nodeList[i].key)

#     g.printAdjList()
#     print() 
#     print() 
#     print()
#     g.removeEdge(g.nodeList[1],g.nodeList[0])
#     g.printAdjList()
#     print() 
#     print() 
#     print()
#     g.removeEdge(g.nodeList[1],g.nodeList[2])
#     g.printAdjList()


# test()
