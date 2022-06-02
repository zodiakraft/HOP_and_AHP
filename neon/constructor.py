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
QToolButton, QVBoxLayout, QPlainTextEdit)
from PyQt5.QtCore import QCoreApplication, QSize, QTimer, QPoint


class Constructor(QWidget):

    def __init__(self):
        super(Constructor, self).__init__()
        # super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(800, 600)
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)
        self.layout = QGridLayout(self)

        self.text = QtWidgets.QPlainTextEdit()
        self.layout.addWidget(self.text)
        
        self.view = QtWidgets.QTextBrowser()
        self.layout.addWidget(self.view)
        
        self.text.textChanged(self.chang)
        
    def chang(self):
        self.view.setText(self.text.toPlainText())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Constructor()
    main_window.show()
    sys.exit(app.exec_())