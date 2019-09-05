from PyQt5.QtCore import Qt

from graphic_items import Node, Edge

class GraphManager:

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

    def addEdge(self, edge, temp=False):
        self.container.addItem(edge)
        if not temp:
            self.edges[edge.fromNode.key][edge.toNode.key] = edge

    def removeEdge(self, edge, temp=False):
        self.container.removeItem(edge)  
        if not temp:
            self.edges[edge.fromNode.key][edge.toNode.key] = None
            # print(self.edges)   
            # self.edges.remove(edge)
            # self.printEdgeMatrix()

    def addNode(self, key, node):
        self.container.addItem(node)
        self.nodes[key] = node
        self.edges.append([None]*key)
        for row in self.edges:
            row.append(None)

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
        # self.printEdgeMatrix()
        # self.nodes.remove(node.key)


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
            if event.button() == Qt.RightButton:
                self.removeNode(item)

        else:

            # Add Node
            node = Node(mousePos.x(), mousePos.y(), self.currentKey)
            self.addNode(self.currentKey, node)
            self.currentKey += 1

    def printEdgeMatrix(self):
        for row in self.edges:
            for edge in row:
                if edge:
                    print("1", end=' ')
                else:
                    print("0", end=' ')
            print()
        print()