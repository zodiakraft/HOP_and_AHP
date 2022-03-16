import os
import time
from os.path import abspath
import sys
import math
from random import randint

import pygame
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon, QFont,  QWindow,  QKeySequence, QImage, QPainter, QCursor
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import (QWidget, QMenuBar, QTextBrowser, QTextEdit,
QMessageBox, QApplication, QAction, QMainWindow, QPushButton, QDesktopWidget,
QGridLayout, QFileDialog, QListWidget, QSpacerItem, QSizePolicy, QTableWidget,
QLineEdit, QLabel, QDoubleSpinBox, QAbstractItemView, QStatusBar, QMenu,
QMessageBox, QTabWidget, QTreeWidget, QTreeWidgetItem, QFrame, QScrollArea,
QToolButton, QVBoxLayout)
from PyQt5.QtCore import QCoreApplication, QSize, QTimer, QPoint


class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((1,1)) #хак
        self.screen = pygame.Surface((400, 400))
        self.r = 50
        self.y = 300
        self.x = 400
        self.scale = 1
        self.scaling = False
        self.moving = False
        self.scene_1 = 0
 
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
        
        self.scene()
        
    def scene(self):
        if self.scene_1 == 1:
            pygame.draw.circle(self.screen, (150, 150, 150), (100, 100), 100)
            
    def drawing(self):
        if self.scale > 1:
            pygame.draw.circle(self.screen, (150, 150, 150), (200 + ((self.x - 200) * self.scale), 200 + ((self.y - 200) * self.scale)), self.r * self.scale)
        elif self.scale < 1:
            pygame.draw.circle(self.screen, (150, 150, 150), (200 + ((self.x - 200) * self.scale), 200 + ((self.y - 200) * self.scale)), self.r * self.scale)
        else:
            pygame.draw.circle(self.screen, (150, 150, 150), (self.x, self.y), self.r*0.75)


class Expander(QWidget):

    def __init__(self, parent=None, title=None, animationDuration = 250):
        super().__init__(parent=parent)
        self.animationDuration = animationDuration
        self.toggleAnimation = QtCore.QParallelAnimationGroup()
        self.contentArea = QScrollArea()
        self.headerLine = QFrame()
        self.toggleButton = QToolButton()
        self.mainLayout = QGridLayout()
        toggleButton = self.toggleButton
        toggleButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        #toggleButton.setArrowType(QtCore.Qt.RightArrow)
        toggleButton.setText('ᐅ ' + title or '')
        toggleButton.setCheckable(True)
        toggleButton.setChecked(False)
        toggleButton.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        headerLine = self.headerLine
        headerLine.setFrameShape(QFrame.NoFrame)
        headerLine.setFrameShadow(QFrame.Plain)
        headerLine.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.contentArea.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.contentArea.setMaximumHeight(0)
        self.contentArea.setMinimumHeight(0)
        toggleAnimation = self.toggleAnimation
        toggleAnimation.addAnimation(QtCore.QPropertyAnimation(self, b"minimumHeight"))
        toggleAnimation.addAnimation(QtCore.QPropertyAnimation(self, b"maximumHeight"))
        toggleAnimation.addAnimation(QtCore.QPropertyAnimation(self.contentArea, b"maximumHeight"))
        mainLayout = self.mainLayout
        mainLayout.setVerticalSpacing(0)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        row = 0
        mainLayout.addWidget(self.toggleButton, row, 0, 1, 1, QtCore.Qt.AlignLeft)
        mainLayout.addWidget(self.headerLine, row, 2, 1, 1)
        row += 1
        mainLayout.addWidget(self.contentArea, row, 0, 1, 3)
        super().setLayout(self.mainLayout)

        def start_animation(checked):
            arrow_type = 'ᐁ ' + title if checked else 'ᐅ ' + title   
            direction = QtCore.QAbstractAnimation.Forward if checked else QtCore.QAbstractAnimation.Backward
            toggleButton.setText(arrow_type)
            self.toggleAnimation.setDirection(direction)
            self.toggleAnimation.start()
        self.toggleButton.clicked.connect(start_animation)

    def setLayout(self, contentLayout):
        self.contentArea.destroy()
        self.contentArea.setLayout(contentLayout)
        collapsedHeight = self.toggleButton.sizeHint().height()
        contentHeight = contentLayout.sizeHint().height()
        for i in range(self.toggleAnimation.animationCount()-1):
            spoilerAnimation = self.toggleAnimation.animationAt(i)
            spoilerAnimation.setDuration(self.animationDuration)
            spoilerAnimation.setStartValue(collapsedHeight)
            spoilerAnimation.setEndValue(collapsedHeight + contentHeight)
        contentAnimation = self.toggleAnimation.animationAt(self.toggleAnimation.animationCount() - 1)
        contentAnimation.setDuration(self.animationDuration)
        contentAnimation.setStartValue(0)
        contentAnimation.setEndValue(contentHeight)


class Shell(QWidget):

    resized = QtCore.pyqtSignal()

    def __init__(self):
        super(Shell, self).__init__()
        # super().__init__()
        self.timer = QTimer()
        self.initUI()
        self.init_pygame()

    def initUI(self):
        self.resize(800, 600)
        # self.setMinimumWidth(800)
        self.layout = QGridLayout(self)

        self.gridlayout = QGridLayout(self)
        self.gridlayout.addWidget(QtWidgets.QLabel('1'))

        self.fridconfig = QWidget(self)
        self.fridconfig.layout = QVBoxLayout()
        
        self.directory = QTreeWidget()

        self.directory.setColumnCount(1)
        self.directory.setHeaderLabels(["Linecenture"])

        data = {"Player": ["Player", "Axe", "Shield"],
        "Enemy": ["Enemy", "Sword"],
        "Tree": []}

        items = []
        for key, values in data.items():
            item = QTreeWidgetItem([key])
            for value in values:
                #ext = value.split(".")[-1].upper()
                child = QTreeWidgetItem([value]) #child = QTreeWidgetItem([value, ext])
                item.addChild(child)
            items.append(item)
        
        self.directory.insertTopLevelItems(0, items)
        self.directory.setFrameShape(QtWidgets.QFrame.NoFrame)

        #self.directory.show()

        self.tab = QTabWidget()
        self.tab.addTab(self.directory, 'Директория проекта')
        self.tab.setMinimumWidth(160)
        # self.tab.setMaximumWidth(self.size().width() // 5)
        self.layout.addWidget(self.tab, 1, 0)

        self.tab1 = QTabWidget()
        self.tab1.setDocumentMode(True)
        self.tab1.addTab(QtWidgets.QLabel(), 'Сцена')
        self.tab1.addTab(QtWidgets.QLabel(), 'Игра')
        # self.tab1.setMinimumWidth(420)
        # self.tab1.setMaximumWidth(self.size().width() // 2)
        self.layout.addWidget(self.tab1, 1, 1)

        self.collapsible = Expander(self, 'Геометрия объекта')
        self.collapsible.setLayout(self.gridlayout)
        self.fridconfig.layout.addWidget(self.collapsible)

        self.collapsible1 = Expander(self, 'Спрайт')
        self.collapsible1.setLayout(self.gridlayout)
        self.fridconfig.layout.addWidget(self.collapsible1)

        #self.fridconfig.layout.addSpacing(600)
        self.fridconfig.layout.addSpacerItem(QSpacerItem(0, 0, vPolicy = QSizePolicy.Expanding))

        self.fridconfig.layout.setContentsMargins(0, 0, 0, 0)
        self.fridconfig.setLayout(self.fridconfig.layout)
        
        self.spacer = QSpacerItem(350, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(self.spacer, 1, 2)

        self.tab2 = QTabWidget()
        self.tab2.addTab(self.fridconfig, 'Конфигурация')
        self.tab2.setMinimumWidth(240)
        self.tab2.setMinimumHeight(505)
        # self.tab2.setMaximumWidth(self.size().width() - self.size().width() // 5 - self.size().width() // 2)
        self.layout.addWidget(self.tab2, 1, 3, 2, 1)

        self.tab3 = QTabWidget()
        self.tab3.addTab(QtWidgets.QLabel('1'), 'Проводник')
        self.tab3.setMinimumHeight(250)
        self.tab3.setMinimumWidth(self.width()-self.tab2.width()-33)
        # self.tab2.setMaximumWidth(self.size().width() // 1.5)
        self.layout.addWidget(self.tab3, 2, 0, 1, 3)

        self.resized.connect(self.tabs)
    
    def resizeEvent(self, event):
        self.resized.emit()
        return super(Shell, self).resizeEvent(event)
    
    def tabs(self):
        self.tab.setMaximumWidth(self.size().width() // 5)
        self.tab2.setMaximumWidth(self.size().width()// 10 * 3)
        self.tab3.setMaximumWidth(self.width()-self.tab2.width()-33)
        # self.tab1.setMaximumWidth(self.width()//10)
        
    def init_pygame(self):
        self.game = Game()
        self.timer.timeout.connect(self.pygame_loop)
        self.timer.start(10)
 
    def pygame_loop(self):
        self.game.loop()
        self.update()
            
    def paintEvent(self, event, scene = 0):
        if scene == 0:
            p = QPainter(self)
            print(self.width(), self.tab3.width(), self.tab2.width(), self.tab3.width() + self.tab2.width(), self.width())
            self.transform_x = self.tab1.width() - 3
            self.transform_y = self.tab1.height() - 20
            self.game.screen = pygame.transform.scale(self.game.screen, (self.transform_x, self.transform_y))
            img = QImage(self.game.screen.get_buffer(), self.transform_x, self.transform_y, QImage.Format_RGB32)
            p.drawImage(self.size().width() // 5 + 17, 31, img)
        if scene == 1:
            self.game.scene_1 = 1
    
    def on_rev(self):
        self.paintEvent(event = 0, scene = 1)
        
    def keyPressEvent(self, event):
        # print(event.key())
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
        # print(int(str(event.pos()).replace('PyQt5.QtCore.QPoint(', '').split(', ')[0]) - 200, int(str(event.pos()).replace('PyQt5.QtCore.QPoint(', '').replace(')', '').split(', ')[1]))
        # print(self.game.x, self.game.y)
        if self.game.x < int(str(event.pos()).replace('PyQt5.QtCore.QPoint(', '').split(', ')[0]) - 200 < self.game.x + 100 and self.game.y < int(str(event.pos()).replace('PyQt5.QtCore.QPoint(', '').replace(')', '').split(', ')[1]) < self.game.y + 100:
            self.game.moving = True
    
    def mouseMoveEvent(self, event):
        if self.game.moving:
            self.game.x = int(str(event.pos()).replace('PyQt5.QtCore.QPoint(', '').split(', ')[0]) - 200
            self.game.y = int(str(event.pos()).replace('PyQt5.QtCore.QPoint(', '').replace(')', '').split(', ')[1])

    def mouseReleaseEvent(self, event):
        self.game.moving = False
        
    def wheelEvent(self, event):
        angle = event.angleDelta()
        angleX = angle.x()
        angleY = angle.y()
        if angleY < 0:
            self.game.scale -= 0.1
            # print('LOW')
        elif angleY > 0:
            self.game.scale += 0.25
            # print('HIGH')
        else:
            pass
            # print('ERROR!')
        self.game.scaling = True
        self.game.drawing()


        
if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Shell()
    main_window.show()
    sys.exit(app.exec_())