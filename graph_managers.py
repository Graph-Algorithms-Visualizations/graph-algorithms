from PyQt5.QtCore import Qt

from graphic_items import Node, Edge


class NodeManager:

    def __init__(self, container, nodes):
        self.container = container
        self.nodes = {}
        for key, val in nodes.items():
            self.addNode(key, val)
        self.currentKey = len(nodes)

    def addNode(self, key, node):
        self.nodes[key] = node
        self.container.addItem(node)

    def removeNode(self, node):
        self.container.removeItem(node)
        self.nodes.remove(node)

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

    def mouseMoveEvent(self, event):
        pass

    def mouseReleaseEvent(self, event):
        pass


class EdgeManager:
    
    def __init__(self, container, edge_matrix):
        self.container = container
        self.edges = edge_matrix
        for row in edge_matrix:
            for edge in row:
                if edge:
                    self.addEdge(edge)

        self.temp_edge = None

    def addEdge(self, edge, temp=False):
        if not temp:
            self.edges[edge.fromNode.key][edge.toNode.key] = edge
        self.container.addItem(edge)

    def removeEdge(self, edge, temp=False):
        self.container.removeItem(edge)
        if not temp:
            self.edges.remove(edge)

    def mousePressEvent(self, event, item):
        pass

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
