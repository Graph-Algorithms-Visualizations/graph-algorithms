from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QTransform, QPainter
from PyQt5.QtCore import QSize

from graph_managers import GraphManager


class GraphContainer(QGraphicsScene):

    def __init__(self):
        super().__init__()
        self.pressed = False
        self.drawing_edge = None
        node_objs, edge_matrix = {}, []     # Open from a pickle file
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
    view.setRenderHint(QPainter.Antialiasing)
    view.resize(QSize(500, 500))
    view.show()

    app.exec_()