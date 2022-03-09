import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPainter, QPainterPath
from PyQt5.QtCore import QSize
from random import randint

ded = [[(20, 20), (350, 525), (100, 300), (20, 20)]]


from PyQt5 import QtCore, QtGui, QtWidgets

class GraphicsView(QtWidgets.QGraphicsView):                                    # +++
    def __init__(self, parent=None):
        super(GraphicsView, self).__init__(parent)
        self.setScene(QtWidgets.QGraphicsScene(self))
        self.resize(1000, 600)

        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(30, 30, 30)))
        self.setFrameShape(QtWidgets.QFrame.NoFrame)

    def wheelEvent(self, event):
        """ Увеличение или уменьшение масштаба. """
        zoomInFactor = 1.25
        zoomOutFactor = 1 / zoomInFactor

        # Save the scene pos
        oldPos = self.mapToScene(event.pos())

        # Zoom
        if event.angleDelta().y() > 0:
            zoomFactor = zoomInFactor
        else:
            zoomFactor = zoomOutFactor
        self.scale(zoomFactor, zoomFactor)

        # Get the new position
        newPos = self.mapToScene(event.pos())

        # Move scene to old position
        delta = newPos - oldPos
        self.translate(delta.x(), delta.y())


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.w = GraphicsView(self)                                       # +++
        self.drawLine()                                                   # +++

    def initUI(self):
        self.setMinimumSize(QSize(200, 200))
        self.resize(1000, 600)
        self.setWindowTitle('Das')
        
    def drawLine(self, qp=None):                    # + =None
        path = QPainterPath()
        def draw_trajectory(line):
            for i, (x, y) in enumerate(line):
                if i == 0:
                    path.moveTo(x, y)
                else:
                    path.lineTo(x, y)

        for line in ded:
            draw_trajectory(line)

#            qp.drawPath(path)

            self.w.scene().addPath(                                        # +++
                path, 
                QtGui.QPen(QtGui.QColor(230, 230, 230)),
                QtGui.QBrush(QtGui.QColor(*[randint(0, 255) for _ in range(4)]))   
                )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())