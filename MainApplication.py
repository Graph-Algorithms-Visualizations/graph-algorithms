from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QTransform
from PyQt5.QtCore import QSize

from graphic_items import *


class GraphContainer(QGraphicsScene):

    def __init__(self):
        super().__init__()
        self.nodes = []
        self.edges = []
        self.pressed = False
        self.drawing_edge = None

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.pressed = True

        mousePos = event.scenePos()
        item = self.itemAt(mousePos.x(), mousePos.y(), QTransform())
        if item:

            # Remove node if right-button clicked
            if event.button() == Qt.RightButton:
                self.removeItem(item)

        else:

            # Add Node
            node = Node(mousePos.x(), mousePos.y())
            self.nodes.append(node)
            self.addItem(node)

        self.update()

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        if self.pressed:
            # Captures Drag events

            mousePos = event.scenePos()
            item = self.itemAt(mousePos.x(), mousePos.y(), QTransform())
            if item and item.type == 'node':

                if self.drawing_edge:
                    # This is the end node
                    self.drawing_edge.setEnd(item.center.x(), item.center.y())
                else:
                    # This is the start node
                    self.drawing_edge = Edge(item, None)
                    self.addItem(self.drawing_edge)

                self.update()

            elif self.drawing_edge:
                self.drawing_edge.setEnd(mousePos.x(), mousePos.y())
                self.update()

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        self.pressed = False

        mousePos = event.scenePos()
        item = self.itemAt(mousePos.x(), mousePos.y(), QTransform())
        if item and item.type == 'node':

            # If we are drawing edge and mouse is released at a node, then add that edge
            if self.drawing_edge and item is not self.drawing_edge.fromNode:
                self.edges.append(self.drawing_edge)
                self.drawing_edge = None

        elif self.drawing_edge:
            self.removeItem(self.drawing_edge)
            self.drawing_edge = None

        self.update()


if __name__ == '__main__':
    app = QApplication([])
    scene = GraphContainer()

    view = QGraphicsView()
    view.setScene(scene)
    view.resize(QSize(500, 500))
    view.show()

    app.exec_()