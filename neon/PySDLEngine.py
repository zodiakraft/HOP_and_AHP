import os
import time
from os.path import abspath
import sys
import math

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon, QFont,  QWindow,  QKeySequence
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import (QWidget, QMenuBar, QTextBrowser, QTextEdit,
QMessageBox, QApplication, QAction, QMainWindow, QPushButton, QDesktopWidget,
QGridLayout, QFileDialog, QListWidget, QSpacerItem, QSizePolicy, QTableWidget,
QLineEdit, QLabel, QDoubleSpinBox, QAbstractItemView, QStatusBar, qApp, QMenu,
QMessageBox, QTabWidget, QTreeWidget, QTreeWidgetItem, QFrame, QScrollArea,
QToolButton, QVBoxLayout)
from PyQt5.QtCore import QCoreApplication, Qt, QSize, right


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
        self.initUI()

    def initUI(self):
        self.resize(800, 600)
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
        self.tab.setMinimumWidth(170)
        self.tab.setMaximumWidth(self.size().width() // 5)
        self.layout.addWidget(self.tab, 1, 0)

        self.tab1 = QTabWidget()
        self.tab1.addTab(QtWidgets.QLabel('1'), 'Сцена')
        self.tab1.addTab(QtWidgets.QLabel('1'), 'Игра')
        self.tab1.setMinimumWidth(420)
        self.tab1.setMaximumWidth(self.size().width() // 2)
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
        
        self.tab2 = QTabWidget()
        self.tab2.addTab(self.fridconfig, 'Конфигурация')
        self.tab2.setMinimumWidth(250)
        self.tab2.setMinimumHeight(505)
        self.tab2.setMaximumWidth(self.size().width() - self.size().width() // 5 - self.size().width() // 2)
        self.layout.addWidget(self.tab2, 1, 3, 3, 2)

        self.tab3 = QTabWidget()
        self.tab3.addTab(QtWidgets.QLabel('1'), 'Проводник')
        self.tab3.setMinimumHeight(250)
        self.layout.addWidget(self.tab3, 2, 0, 2, 2)

        self.resized.connect(self.tabs)
    
    def resizeEvent(self, event):
        self.resized.emit()
        return super(Shell, self).resizeEvent(event)
    
    def tabs(self):
        self.tab.setMaximumWidth(self.size().width() // 5)
        self.tab1.setMaximumWidth(self.size().width() // 2)
        self.tab2.setMaximumWidth(self.size().width() - self.size().width() // 5 - self.size().width() // 2)
        print(self.size().height())


        
if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Shell()
    main_window.show()
    sys.exit(app.exec_())