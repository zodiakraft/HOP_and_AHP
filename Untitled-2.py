import sys
import pygame
from random import randint
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QGridLayout
from PyQt5.QtCore import QTimer, QSize, QPoint
from PyQt5.QtGui import QImage, QPainter, QCursor, QPainterPath

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

     
class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((1,1)) #хак
        self.screen = pygame.Surface((400,400))
        self.r = 50
        self.y = 300
        self.x = 400
        self.scale = 1
        self.moving = False
 
    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
        self.screen.fill((0, 0, 0))
        self.drawing()
        pygame.display.update()
    
        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_LEFT]:
            self.x -= 3
        elif keys[pygame.K_RIGHT]:
            self.x += 3

    def drawing(self):
        pygame.draw.circle(self.screen, (150, 150, 150), (self.x, self.y), self.r)
     
class W(QWidget):
    def __init__(self):
        self.w = GraphicsView(self)                                       # +++
        super().__init__()
        self.btn_rev = QPushButton('Reverse',self)
        self.timer = QTimer()
        self.btn_rev.clicked.connect(self.on_rev)
        self.init_pygame()
 
    def init_pygame(self):
        self.game = Game()
        self.timer.timeout.connect(self.pygame_loop)
        self.timer.start(50)
 
    def pygame_loop(self):
        self.game.loop()
        self.update()
            
    def paintEvent(self,e):
        p = QPainter(self)
        img = QImage(self.game.screen.get_buffer(),400,400,QImage.Format_RGB32)
        p.drawImage(200,0,img)
    
    def on_rev(self):
        self.game.x = 100
        
    def keyPressEvent(self, event):
        print(event.key())
        if event.key() in [QtCore.Qt.Key_D, QtCore.Qt.Key_Right]:
            self.game.x += 2
        elif event.key() in [QtCore.Qt.Key_A]:
            self.game.x -= 2
        if event.key() in [QtCore.Qt.Key_W]:
            self.game.y -= 2
        if event.key() in [QtCore.Qt.Key_S]:
            self.game.y += 2
        event.accept()
        
# if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
# if event.type == pygame.MOUSEMOTION:
# if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        
    def mousePressEvent(self, event):
        print(int(str(event.pos()).replace('PyQt5.QtCore.QPoint(', '').split(', ')[0]) - 200, int(str(event.pos()).replace('PyQt5.QtCore.QPoint(', '').replace(')', '').split(', ')[1]))
        print(self.game.x, self.game.y)
        if self.game.x < int(str(event.pos()).replace('PyQt5.QtCore.QPoint(', '').split(', ')[0]) - 200 < self.game.x + 100 and self.game.y < int(str(event.pos()).replace('PyQt5.QtCore.QPoint(', '').replace(')', '').split(', ')[1]) < self.game.y + 100:
            self.game.moving = True
    
    def mouseMoveEvent(self, event):
        if self.game.moving:
            self.game.x = int(str(event.pos()).replace('PyQt5.QtCore.QPoint(', '').split(', ')[0]) - 200
            self.game.y = int(str(event.pos()).replace('PyQt5.QtCore.QPoint(', '').replace(')', '').split(', ')[1])

    def mouseReleaseEvent(self, event):
        self.game.moving = False

    def wheelEvent(self, event):
        print(event.angleDelta().x())
 
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = W()
    w.resize(600,400)
    w.show()
    sys.exit(app.exec_())

# central_widget = QWidget(self)
# grid_layout = QGridLayout(central_widget)
# self.setCentralWidget(central_widget)
# self._label = QLabel('', self)
# grid_layout.addWidget(self._label, 0, 0)