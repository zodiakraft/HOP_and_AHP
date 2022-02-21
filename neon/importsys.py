import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, \
    QLabel, QAction, QMainWindow, QStatusBar, QMenu, QMessageBox, qApp
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QFont,  QWindow,  QKeySequence


class Game(QMainWindow):
    def __init__(self):
        super().__init__()

        self._createActions()                                               # +++
        self._createMenuBar()                                               # +++

        self.initUI()

        self._createStatusBar()                                              # +++


    def _createActions(self):
        self.exitAction = QAction(QIcon("img/exit.png"), "&Quit", self)
        self.exitAction.triggered.connect(self.close)
        self.helpContentAction = QAction(QIcon("img/readMe.png"), "&Help Content", self)
        self.helpContentAction.setStatusTip("Show the application's About box")
        self.helpContentAction.triggered.connect(self.about)
        self.aboutAction = QAction("&About Qt", self)
        self.aboutAction.setStatusTip("Show the Qt library's About box")
        self.aboutAction.triggered.connect(qApp.aboutQt)

    def _createMenuBar(self):
        menuBar = self.menuBar()
        fileMenu = QMenu("&File", self)
        fileMenu.addAction(self.exitAction)
        menuBar.addMenu(fileMenu)
        # Используя icon and a title
        helpMenu = menuBar.addMenu(QIcon("img/qtlogo.png"), "&Help")
        helpMenu.addAction(self.helpContentAction)
        helpMenu.addAction(self.aboutAction)

    def _createStatusBar(self):
        self.statusbar = self.statusBar()
        # Adding a temporary message
        self.statusbar.showMessage("Hello StatusBar", 3000)
        # Добавление постоянного сообщения
        self.text_1 = "<h3 style='color: red;'>Hello World</h3>"
        self.wcLabel = QLabel(f"{self.text_1}")
        self.statusbar.addPermanentWidget(self.wcLabel)

    def about(self):
        QMessageBox.about(self, "About Dock Widgets",
               "The <b>Dock Widgets</b> example demonstrates how to "
               "use Qt's dock widgets. You can enter your own text, "
               "click a customer to add a customer name and "
               "address, and click standard paragraphs to add them.")

    def initUI(self):
        # Window
        self.setWindowTitle('Game')
#?        self.setFixedSize(460, 210)

        # Buttons
        self.enter = QPushButton('Enter', self)
        self.enter.setFixedSize(70, 30)
        self.enter.move(100, 25)
        self.enter.setEnabled(False)

        self.enter_range = QPushButton('Enter range', self)
        self.enter_range.setFixedSize(80, 35)
        self.enter_range.move(150, 77)

        # LineEdit
        self.number = QLineEdit(self)
        self.number.setPlaceholderText('Num')
        self.number.setFixedSize(50, 25)
        self.number.move(20, 28)
        self.number.setFont(QFont('Times New Roman', 12))
        self.num_int = self.number.text()

        self.froms = QLineEdit(self)
        self.froms.setPlaceholderText('From')
        self.froms.setFixedSize(45, 30)
        self.froms.move(10, 80)
        self.froms.setFont(QFont('Times New Roman', 12))

        self.tos = QLineEdit(self)
        self.tos.setPlaceholderText('To')
        self.tos.setFixedSize(45, 30)
        self.tos.move(80, 80)
        self.tos.setFont(QFont('Times New Roman', 12))

        # Label answer
        self.answer = QLabel('', self)
        self.answer.setStyleSheet('border: 2px solid black')
        self.answer.setFixedSize(270, 60)
        self.answer.move(10, 140)

        # count
        self.sum_text = QLabel('Количество попыток:', self)
        self.sum = QLabel('', self)
        self.sum_text.setFixedSize(140, 20)
        self.sum_text.setStyleSheet('border: 2px solid black')
        self.sum.setFont(QFont('Times New Roman', 15))
        self.sum_text.setFont(QFont('Times New Roman', 11))
        self.sum_text.move(300, 140)

        self.sum.setFixedSize(50, 30)
        self.sum.setStyleSheet('border: 2px solid black')
        self.sum.move(340, 170)
        self.enter_range.clicked.connect(self.enter_ranges)
        self.total = 0
#?    total = 0

    def enter_ranges(self):
        Froms = int(self.froms.text())
        To = int(self.tos.text())
        self.rand_num = random.randrange(Froms, To)
        self.answer.setText('Ok! Number is ready!')
        self.answer.setFont(QFont('Times New Roman', 15))
        self.enter.clicked.connect(self.trying)
        self.enter.setEnabled(True)
        self.enter_range.setEnabled(False)

    def trying(self):
        self.total += 1
        self.sum.setText(str(self.total))
        Enter_num = int(self.number.text())
        Rand_num = self.rand_num
        print(Rand_num)
        if Enter_num == Rand_num:
            self.answer.setText("True! You're using {0} try".format(self.total))
            del self.total
            self.enter.setEnabled(False)
            self.enter_range.setEnabled(True)
        if Enter_num > int(self.tos.text()):
            self.answer.setText('Number is bigger that "To"')
        elif Enter_num < int(self.froms.text()):
            self.answer.setText('Number is lower that "From"')

        else:
            self.answer.setText('False!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gm = Game()
    gm.resize(500, 400)
    gm.show()
    app.exec_()
