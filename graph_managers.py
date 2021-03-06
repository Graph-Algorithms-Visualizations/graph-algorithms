from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from modify import Graph
from graphic_items import Node, Edge
from NPAlgorithms import AlgorithmManager
import copy

class GraphManager:
    # Parameters as container nodes and edge_matrix
    # edge matrix stores the connections check dummy data for example
    # nodes is a dictionary of cordinates as values mapped to its indices as keys
    # converted nodes to self.nodes which is dictionary of nodes class object mapped to indices as keys
    # converted edge_matrix to self.edges which is 2d matrix of edge class objects

    def __init__(self, container, newGraph):
        self.container = container
        self.temp_edge = None
        self.selectedItem = None
        self.penColor = None
        self.graph = None
        self.vertexMask = []
        self.updateVirtualGraph(newGraph)
        self.AlgorithmManager = AlgorithmManager(self.graph)


    def updateVirtualGraph(self, newGraph):
        if self.graph:
            # Update Graph

            # Remove all nodes first
            for node in self.graph.nodeList:
                self.removeNode(node)

        # Adding nodes in graph

        self.graph = Graph([], [])

        for node in newGraph.nodeList:
            self.addNode(node)

        for edges in newGraph.adjacencyList:
            for edge in edges:
                self.addEdge(edge, False, True)

    # adds edge in gui and in stored matrix

    def addEdge(self, edge, temp=False, directed = False):
        cnt = 0
        if self.penColor:
            edge.setPenColor(self.penColor)
        if edge:
            self.container.addItem(edge)
        if not temp:
            adj = self.graph.adjacencyList
            nodes = self.graph.nodeList

            toNode = edge.toNode
            fromNode = edge.fromNode
            
            adj[fromNode.key].append(edge)
            
            if(directed == False):
                newReverseEdge = Edge(toNode,fromNode, edge.color)
                adj[toNode.key].append(newReverseEdge)
                self.container.addItem(newReverseEdge)


    # removes edge in gui and stored matrix
    def removeEdge(self, edge, temp=False, directed = False):
        self.container.removeItem(edge)
        # self.printAdjList()
        if not temp:
            toNode = edge.toNode
            fromNode = edge.fromNode
            
            self.removeEdgeFromList(fromNode, toNode)
            if directed == False:
                self.removeEdgeFromList(toNode, fromNode)


    #to remove edge from list
    def removeEdgeFromList(self, fromNode, toNode):
        adj = self.graph.adjacencyList[fromNode.key]
        newAdj = []
        for i in range(len(adj)):
            if(adj[i].toNode.key != toNode.key):
                newAdj.append(adj[i])
        self.graph.adjacencyList[fromNode.key] = newAdj

    # adds edge in gui and in stored matrix

    def addNode(self, node):
        if self.penColor:
            node.setPenColor(self.penColor)
        self.container.addItem(node)
        
        adj = self.graph.adjacencyList
        nodes = self.graph.nodeList

        node.key = len(nodes)
        # print(node.key)
        nodes.append(node)

        newList = []
        adj.append(newList)


    # removes node in gui and stored matrix and 

    def printAdjList(self):
        for i in range(len(self.graph.adjacencyList)):
            print('adj - ' + str(i) + ':', end = ' ')
            for j in range(len(self.graph.adjacencyList[i])):
                print(self.graph.adjacencyList[i][j].toNode.key,end = ' ')
            print()
        print()
        print()

    def removeNode(self, node):

        self.container.removeItem(node)


        for edge in self.graph.adjacencyList[node.key]:
            self.container.removeItem(edge)

        self.graph.adjacencyList.pop(node.key)
        for edgelist in self.graph.adjacencyList:
            tempEdge = []
            for edge in edgelist:
                if edge.toNode.key == node.key or edge.fromNode.key == node.key:
                    tempEdge.append(edge)
                    break
            for e in tempEdge:
                self.container.removeItem(e)
                edgelist.remove(e)


        for nde in self.graph.nodeList:
            if nde.key > node.key:
                nde.key = nde.key - 1

        self.graph.nodeList.remove(node)


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

            if self.selectedItem:
                self.selectedItem.clicked = False
                self.selectedItem = None

            self.removeMask()

    def mouseDoubleClickEvent(self, event, item):
        mousePos = event.scenePos()
        if not item:
            # Add Node
            node = Node(mousePos.x(), mousePos.y())
            self.addNode(node)


    def getData(self):
        return self.graph.nodeList, self.graph.adjacencyList

    def callAlgorithms(self, id):
        self.removeMask()
        self.vertexMask = self.AlgorithmManager.runAlgorithm(id)
        self.addMask()

    def addMask(self):

        for i in range(len(self.vertexMask)):
            if not self.vertexMask[i]:
                self.graph.nodeList[i].addMask()

        self.container.update()

    def removeMask(self):

        for i in range(len(self.vertexMask)):
            if not self.vertexMask[i]:
                self.graph.nodeList[i].removeMask()

        self.container.update()

    def printMatrix(self):
        for row in self.edges:
            for edge in row:
                if edge:
                    print("1", end=" ")
                else:
                    print("0", end=" ")
            print()
        print()