from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QTransform
from PyQt5.QtCore import QSize

from graphic_items import *
from graph_managers import GraphManager

from dummy_data import get_processed_data


class GraphContainer(QGraphicsScene):

    def __init__(self):
        super().__init__()
        self.nodes = []
        self.edges = []
        self.pressed = False
        self.drawing_edge = None
        node_objs, edge_matrix = get_processed_data()
        self.GraphManager = GraphManager(self, node_objs, edge_matrix)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.pressed = True

        mousePos = event.scenePos()
        item = self.itemAt(mousePos.x(), mousePos.y(), QTransform())
        self.GraphManager.mousePressEvent(event, item)
        self.update()

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        if self.pressed:
            # Captures Drag events

            mousePos = event.scenePos()
            item = self.itemAt(mousePos.x(), mousePos.y(), QTransform())
            self.GraphManager.mouseMoveEvent(event, item)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        self.pressed = False

        mousePos = event.scenePos()
        item = self.itemAt(mousePos.x(), mousePos.y(), QTransform())
        self.GraphManager.mouseReleaseEvent(event, item)


if __name__ == '__main__':
    app = QApplication([])
    scene = GraphContainer()

    view = QGraphicsView()
    view.setScene(scene)
    view.resize(QSize(500, 500))
    view.show()

    app.exec_()