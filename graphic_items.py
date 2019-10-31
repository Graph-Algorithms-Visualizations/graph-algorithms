from PyQt5.QtWidgets import QGraphicsItem, QGraphicsLineItem
from PyQt5.QtGui import QBrush, QPen, QColor
from PyQt5.QtCore import Qt, QRectF, QPoint


class Node(QGraphicsItem):

    def __init__(self, x, y, color=None):
        super().__init__()
        self.setAcceptHoverEvents(True)
        self.center = QPoint(x, y)
        self.onFocus = False
        self.clicked = False
        self.type = 'node'
        self.key = -1

        self.radius = 15
        if color:
            self.color = color
        else:
            self.color = QColor(255, 0, 0)

        self.focusColor = QColor(255, 153, 51)
        self.clickedColor = QColor(255, 255, 0)
        self.outlineColor = QColor(153, 0, 0)

    def paint(self, painter, styleoptions, widget=None):
        if self.clicked:
            painter.setBrush(QBrush(self.clickedColor))
        elif self.onFocus:
            painter.setBrush(QBrush(self.focusColor))
        else:
            painter.setBrush(QBrush(self.color))
        painter.setPen(QPen(self.outlineColor))
        painter.drawEllipse(self.center, self.radius, self.radius)

    def setPenColor(self, color):
        self.color = color

    def addMask(self):
        self.color.setAlpha(50)
        self.focusColor.setAlpha(50)
        self.clickedColor.setAlpha(50)
        self.outlineColor.setAlpha(50)

    def boundingRect(self):
        return QRectF(self.center.x() - self.radius, self.center.y() - self.radius, 2 * self.radius, 2 * self.radius)

    def hoverEnterEvent(self, event):
        self.onFocus = True
        self.update()

    def hoverLeaveEvent(self, event):
        self.onFocus = False
        self.update()


class Edge(QGraphicsLineItem):

    def __init__(self, fromNode, toNode, color=None):
        self.fromNode = fromNode
        self.toNode = toNode
        if toNode:
            self.endx = toNode.center.x()
            self.endy = toNode.center.y()
        else:
            self.endx = fromNode.center.x()
            self.endy = fromNode.center.y()

        super().__init__(fromNode.center.x(), fromNode.center.y(), self.endx, self.endy)
        self.setPen(QPen(Qt.black, 5))
        self.setZValue(-1)
        self.type = 'edge'
        self.clicked = False
        self.setAcceptHoverEvents(True)
        self.onFocus = False

        if color:
            self.color = color
        else:
            self.color = QColor(0, 0, 0)
        self.focusColor = QColor(0, 100, 100)
        self.clickedColor = QColor(0, 204, 204)
        self.width = 6

    def setEnd(self, x, y):
        self.setLine(self.fromNode.center.x(), self.fromNode.center.y(), x, y)

    def setPenColor(self, color):
        self.color = color

    def addMask(self):
        self.color.setAlpha(50)
        self.focusColor.setAlpha(50)
        self.clickedColor.setAlpha(50)
        self.outlineColor.setAlpha(50)

    def paint(self, painter, styleoptions, widget=None):
        if self.clicked:
            pen = QPen(self.clickedColor)
        elif self.onFocus:
            pen = QPen(self.focusColor)
        else:
            pen = QPen(self.color)

        pen.setCapStyle(Qt.RoundCap)
        pen.setWidth(self.width)
        self.setPen(pen)
        super().paint(painter, styleoptions, widget)

    def hoverEnterEvent(self, event):
        self.onFocus = True
        self.update()

    def hoverLeaveEvent(self, event):
        self.onFocus = False
        self.update()