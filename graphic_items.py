from PyQt5.QtWidgets import QGraphicsItem, QGraphicsLineItem
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtCore import Qt, QRectF, QPoint


class Node(QGraphicsItem):

    def __init__(self, x, y, key):
        super().__init__()
        self.setAcceptHoverEvents(True)
        self.center = QPoint(x, y)
        self.onFocus = False
        self.radius = 10
        self.type = 'node'
        self.key = key

    def paint(self, painter, styleoptions, widget=None):
        if self.onFocus:
            painter.setBrush(QBrush(Qt.yellow))
        else:
            painter.setBrush(QBrush(Qt.red))
        painter.drawEllipse(self.center, self.radius, self.radius)

    def boundingRect(self):
        return QRectF(self.center.x() - self.radius, self.center.y() - self.radius, 2 * self.radius, 2 * self.radius)

    def hoverEnterEvent(self, event):
        self.onFocus = True
        self.update()

    def hoverLeaveEvent(self, event):
        self.onFocus = False
        self.update()


class Edge(QGraphicsLineItem):

    def __init__(self, fromNode, toNode):
        self.fromNode = fromNode
        self.toNode = toNode
        if toNode:
            self.endx = toNode.center.x()
            self.endy = toNode.center.y()
        else:
            self.endx = fromNode.center.x()
            self.endy = fromNode.center.y()

        super().__init__(fromNode.center.x(), fromNode.center.y(), self.endx, self.endy)
        self.setPen(QPen(Qt.black, 3))
        self.setZValue(-1)

    def setEnd(self, x, y):
        self.setLine(self.fromNode.center.x(), self.fromNode.center.y(), x, y)
