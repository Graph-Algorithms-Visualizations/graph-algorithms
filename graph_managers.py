from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

from graphic_items import Node, Edge


class GraphManager:
    # Parameters as container nodes and edge_matrix
    # edge matrix stores the connections check dummy data for example
    # nodes is a dictionary of cordinates as values mapped to its indices as keys
    # converted nodes to self.nodes which is dictionary of nodes class object mapped to indices as keys
    # converted edge_matrix to self.edges which is 2d matrix of edge class objects
    
    # def __init__(self, container, nodes, edge_matrix):
    #     self.container = container
    #     self.temp_edge = None
    #     self.selectedItem = None
    #     self.penColor = None

    #     if len(nodes) > 0:
    #         self.currentKey = max([key for key in nodes]) + 1
    #     else:
    #         self.currentKey = 0

    #     self.nodes = {}
    #     self.edges = []
    #     for _ in range(self.currentKey):
    #         self.edges.append([None] * self.currentKey)

    #     for key, val in nodes.items():
    #         self.addNode(key, val)

    #     for row in edge_matrix:
    #         for edge in row:
    #             if edge:
    #                 self.addEdge(edge)

    def __init__(self, container, newGraph):
        self.container = container
        self.temp_edge = None
        self.selectedItem = None
        self.penColor = None
        self.graph = None
        if len(nodes) > 0:
            self.currentKey = max([key for key in nodes]) + 1
        else:
            self.currentKey = 0

        self.updateVirtualGraph(newGraph)

    def updateVirtualGraph(self, newGraph):
        if self.graph:
            # Update Graph

            # Remove all nodes first
            for node in self.graph.nodeList:
                self.removeNode(node)
            # Add new nodes and its edges
        else:
            self.graph = newGraph

        # Adding nodes in graph
        for node in self.graph.nodeList:
            self.addNode(0, node)

        for edges in self.graph.adjacencyList:
            for edge in edges:
                self.addEdge(edge)

    # adds edge in gui and in stored matrix
    # any doubt contact arib

    # def addEdge(self, edge, temp=False):
    #     if self.penColor:
    #         edge.setPenColor(self.penColor)
    #     if edge:
    #         self.container.addItem(edge)
    #     if not temp:
    #         self.edges[edge.fromNode.key][edge.toNode.key] = edge
    
    def addEdge(self, edge, temp=False, directed = False):
        if self.penColor:
            edge.setPenColor(self.penColor)
        if edge:
            self.container.addItem(edge)
        if not temp:
            adj = self.adjacencyList
            nodes = self.nodeList

            toNode = edge.toNode
            fromNode = edge.fromNode
            
            adj[fromNode.key].append(edge)
            
            if(directed == False):
                newReverseEdge = Edge(toNode,fromNode)
                adj[toNode.key].append(newReverseEdge)

    # removes edge in gui and stored matrix
    # any doubt contact sid

    # def removeEdge(self, edge, temp=False):
    #     self.container.removeItem(edge)  
    #     if not temp:
    #         self.edges[edge.fromNode.key][edge.toNode.key] = None
    def removeEdge(self, edge, temp=False, directed = False):
        self.container.removeItem(edge)  
        if not temp:
            toNode = edge.toNode
            fromNode = edge.fromNode
            
            self.removeEdgeFromList(fromNode, toNode)
            if(directed == False):
                self.removeEdgeFromList(toNode, fromNode)


    #to remove edge from list
    def removeEdgeFromList(self, fromNode, toNode):
        adj = self.adjacencyList[fromNode.key]
        newAdj = []
        for i in range(len(adj)):
            if(adj[i].toNode.key != toNode.key):
                newAdj.append(adj[i])
        self.adjacencyList[fromNode.key] = newAdj

    # adds edge in gui and in stored matrix
    # any doubt contact arib

    # def addNode(self, key, node):
    #     if self.penColor:
    #         node.setPenColor(self.penColor)
    #     self.container.addItem(node)
    #     self.nodes[key] = node
    #     if key == self.currentKey:
    #         self.edges.append([None]*key)
    #         for row in self.edges:
    #             row.append(None)

    def addNode(self, key, node):
        if self.penColor:
            node.setPenColor(self.penColor)
        self.container.addItem(node)
        
        adj = self.graph.adjacencyList
        nodes = self.graph.nodeList

        node.key = len(nodes)
        nodes.append(node)

        newList = []
        adj.append(newList)
        


    # removes node in gui and stored matrix and 
    # any doubt contact sid

    # def removeNode(self, node):
    #     self.container.removeItem(node)
    #     self.nodes.pop(node.key)
    #     for edge in self.edges[node.key]:
    #         if edge:
    #             self.removeEdge(edge)
    #     for i in range(len(self.edges)):
    #         if self.edges[i][node.key]:
    #             self.removeEdge(self.edges[i][node.key])

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
        for i in range(len(self.graph.adjacencyList)):
            
            if(i != node.key):
                currentSize = currentSize + 1
                adj.append([])

                for j in range(len(self.graph.adjacencyList[i])):
                    if(self.graph.adjacencyList[i][j].toNode.key != node.key):
                        modifiedEdge = copy.deepcopy(self.graph.adjacencyList[i][j])
                        modifiedEdge.fromNode.key = newIndex[modifiedEdge.fromNode.key]
                        modifiedEdge.toNode.key = newIndex[modifiedEdge.toNode.key]
                        adj[currentSize - 1].append(modifiedEdge) 
        
        #create modified nodeList
        nodes = []
        for i in range(len(self.graph.nodeList)):
            if(self.graph.nodeList[i].key != node.key):
                modifiedNode = self.graph.nodeList[i]
                modifiedNode = newIndex[modifiedNode.key]
                nodes.append(modifiedNode)

        self.graph.adjacencyList = adj
        self.graph.nodeList = nodes

    # any doubt contact arib
    def toggleItem(self, item):

        if self.selectedItem and item is self.selectedItem:
            self.selectedItem.clicked = False
            self.selectedItem = None
        elif self.selectedItem:
            self.selectedItem.clicked = False
            self.selectedItem = item
            self.selectedItem.clicked = True
        else:
            self.selectedItem = item
            self.selectedItem.clicked = True

    def setPenColor(self, penColor):
        self.penColor = penColor

    def mouseMoveEvent(self, event, item):

        mousePos = event.scenePos()
        if item and item.type == 'node':

            if self.temp_edge:
                # This is the end node
                self.temp_edge.setEnd(item.center.x(), item.center.y())
            else:
                # This is the start node
                self.temp_edge = Edge(item, None)
                self.addEdge(self.temp_edge, temp=True)

            self.container.update()

        elif self.temp_edge:
            self.temp_edge.setEnd(mousePos.x(), mousePos.y())
            self.container.update()

    # any doubt contact arib

    def mouseReleaseEvent(self, event, item):
        if item and item.type == 'node':

            # If we are drawing edge and mouse is released at a node, then add that edge
            if self.temp_edge and item is not self.temp_edge.fromNode:
                self.removeEdge(self.temp_edge, temp=True)
                newEdge = Edge(self.temp_edge.fromNode, item)
                self.addEdge(newEdge)
                self.temp_edge = None

        elif self.temp_edge:
            self.removeEdge(self.temp_edge, temp=True)
            self.temp_edge = None

        self.container.update()

    # any doubt contact arib

    def mousePressEvent(self, event, item):
        mousePos = event.scenePos()
        if item and item.type == 'node':

            # Remove node if right-button clicked
            if item is self.selectedItem and event.button() == Qt.RightButton:
                self.removeNode(item)

            if event.button() == Qt.LeftButton:
                self.toggleItem(item)

        elif item and item.type == 'edge':

            if item is self.selectedItem and event.button() == Qt.RightButton:
                self.removeEdge(item)

            if event.button() == Qt.LeftButton:
                self.toggleItem(item)

        else:

            # Add Node
            # node = Node(mousePos.x(), mousePos.y(), self.currentKey)
            # self.addNode(self.currentKey, node)
            # self.currentKey += 1

            # self.toggleItem(node)
            if self.selectedItem:
                self.selectedItem.clicked = False
                self.selectedItem = None

    def mouseDoubleClickEvent(self, event, item):
        mousePos = event.scenePos()
        if not item:
            # Add Node
            node = Node(mousePos.x(), mousePos.y(), self.currentKey)
            self.addNode(self.currentKey, node)
            self.currentKey += 1


    def getData(self):
        return self.nodes, self.edges

    def printMatrix(self):
        for row in self.edges:
            for edge in row:
                if edge:
                    print("1", end=" ")
                else:
                    print("0", end=" ")
            print()
        print()