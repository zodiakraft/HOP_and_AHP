import sys
from PyQt5 import QtWidgets

import design

class ExampleApp(QtWidgets.QMainWindow, design.Ui_Vilg):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.changer)
        self.pushButton_2.clicked.connect(self.comparison)
        self.pushButton_3.clicked.connect(self.unifier)
        self.pushButton_4.clicked.connect(self.calculator)
            
    def changer(self):
        self.texting = self.lineEdit.text().replace(',', '.').split()
        self.texting_browser = ''
        for i, elem in enumerate(self.texting):
            self.texting[i] = int(elem)
        self.dict = {self.texting.index(max(self.texting)):min(self.texting), self.texting.index(min(self.texting)):max(self.texting)}
        for key, value in self.dict.items():
            self.texting[key] = value
        for i in self.texting:
            self.texting_browser = self.texting_browser + str(i) + ' ' #Замените пробел на любой символ, который будет разделять символы
        self.textBrowser.setText(self.texting_browser.rstrip()) #Тогда rstrip() замените на replace('символ', '')
    def comparison(self):
        self.listing = [int(self.lineEdit_2.text()), int(self.lineEdit_5.text()), int(self.lineEdit_6.text())]
        if self.listing.index(max(self.listing)) == 0:
            self.lineEdit_2.setStyleSheet("QLineEdit {background-color: green;}")
        elif self.listing.index(max(self.listing)) == 1:
            self.lineEdit_5.setStyleSheet("QLineEdit {background-color: green;}")
        elif self.listing.index(max(self.listing)) == 2:
            self.lineEdit_6.setStyleSheet("QLineEdit {background-color: green;}")
            
        self.textBrowser_2.setText(str(max(self.listing)))
        # if self.lineEdit_2.text() == self.lineEdit_5.text() and self.lineEdit_5.text() == self.lineEdit_6.text():
        #     self.textBrowser_2.setText(f'{str(self.lineEdit_2.text())} = {self.lineEdit_5.text()} = {self.lineEdit_6.text()}')
        # elif self.lineEdit_2.text() == self.lineEdit_5.text() and self.lineEdit_5.text() < self.lineEdit_6.text():
        #     self.textBrowser_2.setText(f'{str(self.lineEdit_2.text())} = {self.lineEdit_5.text()} < {self.lineEdit_6.text()}')
        # elif self.lineEdit_2.text() == self.lineEdit_5.text() and self.lineEdit_5.text() > self.lineEdit_6.text():
        #     self.textBrowser_2.setText(f'{str(self.lineEdit_2.text())} = {self.lineEdit_5.text()} > {self.lineEdit_6.text()}')
        # elif self.lineEdit_2.text() < self.lineEdit_5.text() and self.lineEdit_5.text() == self.lineEdit_6.text():
        #     self.textBrowser_2.setText(f'{str(self.lineEdit_2.text())} < {self.lineEdit_5.text()} = {self.lineEdit_6.text()}')
        # elif self.lineEdit_2.text() < self.lineEdit_5.text() and self.lineEdit_5.text() < self.lineEdit_6.text():
        #     self.textBrowser_2.setText(f'{str(self.lineEdit_2.text())} < {self.lineEdit_5.text()} < {self.lineEdit_6.text()}')
        # elif self.lineEdit_2.text() < self.lineEdit_5.text() and self.lineEdit_5.text() > self.lineEdit_6.text():
        #     self.textBrowser_2.setText(f'{str(self.lineEdit_2.text())} < {self.lineEdit_5.text()} > {self.lineEdit_6.text()}')
        # elif self.lineEdit_2.text() > self.lineEdit_5.text() and self.lineEdit_5.text() == self.lineEdit_6.text():
        #     self.textBrowser_2.setText(f'{str(self.lineEdit_2.text())} > {self.lineEdit_5.text()} = {self.lineEdit_6.text()}')
        # elif self.lineEdit_2.text() > self.lineEdit_5.text() and self.lineEdit_5.text() < self.lineEdit_6.text():
        #     self.textBrowser_2.setText(f'{str(self.lineEdit_2.text())} > {self.lineEdit_5.text()} < {self.lineEdit_6.text()}')
        # elif self.lineEdit_2.text() > self.lineEdit_5.text() and self.lineEdit_5.text() > self.lineEdit_6.text():
        #     self.textBrowser_2.setText(f'{str(self.lineEdit_2.text())} > {self.lineEdit_5.text()} > {self.lineEdit_6.text()}')
    def unifier(self):
        pass
    def calculator(self):
        pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.setWindowTitle('Калькулятор')
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()