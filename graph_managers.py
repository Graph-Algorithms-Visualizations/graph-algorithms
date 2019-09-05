from PyQt5.QtCore import Qt

from graphic_items import Node, Edge


class GraphManager:
    # Parameters as container nodes and edge_matrix
    # edge matrix stores the connections check dummy data for example
    # nodes is a dictionary of cordinates as values mapped to its indices as keys
    # converted nodes to self.nodes which is dictionary of nodes class object mapped to indices as keys
    # converted edge_matrix to self.edges which is 2d matrix of edge class objects
    
    def __init__(self, container, nodes, edge_matrix):
        self.container = container
        self.nodes = {}
        self.edges = []
        for key, val in nodes.items():
            self.addNode(key, val)
        self.currentKey = len(nodes)

        for row in edge_matrix:
            for edge in row:
                if edge:
                    self.addEdge(edge)

        self.temp_edge = None
        self.selectedItem = None

    # adds edge in gui and in stored matrix
    # any doubt contact arib

    def addEdge(self, edge, temp=False):
        self.container.addItem(edge)
        if not temp:
            self.edges[edge.fromNode.key][edge.toNode.key] = edge

    # removes edge in gui and stored matrix
    # any doubt contact sid

    def removeEdge(self, edge, temp=False):
        self.container.removeItem(edge)  
        if not temp:
            self.edges[edge.fromNode.key][edge.toNode.key] = None
            # print(self.edges)   
            # self.edges.remove(edge)
            # self.printEdgeMatrix()

    # adds edge in gui and in stored matrix
    # any doubt contact arib

    def addNode(self, key, node):
        self.container.addItem(node)
        self.nodes[key] = node
        self.edges.append([None]*key)
        for row in self.edges:
            row.append(None)

    # removes node in gui and stored matrix and 
    # any doubt contact sid

    def removeNode(self, node):
        self.container.removeItem(node)
        self.nodes.pop(node.key)
        for i in range(len(self.edges)):
            if(self.edges[node.key][i] != None):
                self.container.removeItem(self.edges[node.key][i])
                self.edges[node.key][i] = None
                # print(self.edges)
        for i in range(len(self.edges)):
            if(self.edges[i][node.key] != None):
                self.container.removeItem(self.edges[i][node.key])
                self.edges[i][node.key] = None


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
            node = Node(mousePos.x(), mousePos.y(), self.currentKey)
            self.addNode(self.currentKey, node)
            self.currentKey += 1

            self.toggleItem(node)
            self.selectedItem.clicked = False
            self.selectedItem = None
