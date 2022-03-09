import sys
import inspect
import textwrap
from collections import OrderedDict, UserString
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class Expander(QWidget):

    def __init__(self, parent=None, title=None, animationDuration=200):
        super().__init__(parent=parent)
        self.animationDuration = animationDuration
        self.toggleAnimation = QtCore.QParallelAnimationGroup()
        self.contentArea = QScrollArea()
        self.headerLine = QFrame()
        self.toggleButton = QToolButton()
        self.mainLayout = QGridLayout()
        toggleButton = self.toggleButton
        toggleButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        toggleButton.setArrowType(QtCore.Qt.RightArrow)
        toggleButton.setText(title or '')
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
            arrow_type = QtCore.Qt.DownArrow if checked else QtCore.Qt.RightArrow
            direction = QtCore.QAbstractAnimation.Forward if checked else QtCore.QAbstractAnimation.Backward
            toggleButton.setArrowType(arrow_type)
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

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        contents_vbox = QVBoxLayout()
        label_box = QHBoxLayout()
        for text in ('hello', 'goodbye', 'adios'):
            lbl = QLabel(text)
            lbl.setAlignment(Qt.AlignCenter)
            label_box.addWidget(lbl)
        button_group = QButtonGroup()
        button_group.setExclusive(True)
        self.button_group = button_group 
        button_hbox = QHBoxLayout()
        for _id, text in enumerate(('small', 'medium', 'large')):
            btn = QPushButton(text)
            btn.setCheckable(True)
            button_group.addButton(btn)
            button_group.setId(btn, _id)
            button_hbox.addWidget(btn)
        button_group.buttons()[0].toggle()
        text_area = QTextEdit()
        text_area.setPlaceholderText('Type a greeting here')
        contents_vbox.addLayout(label_box)
        contents_vbox.addLayout(button_hbox)
        contents_vbox.addWidget(text_area)
        collapsible = Expander(self, 'Expander')
        collapsible.setLayout(contents_vbox)
        vbox = QVBoxLayout()
        vbox.addWidget(collapsible)
        vbox.setAlignment(Qt.AlignTop)
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.setGeometry(200, 200, 500, 400)
        self.setWindowTitle('Expander')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())