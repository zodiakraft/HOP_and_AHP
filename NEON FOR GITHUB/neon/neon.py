#!/usr/bin/python3
# -*- coding: utf-8 -*-

#if '#' in all_code:
        #	all_code = all_code.split('#')
        #	#print(all_code)

        #fr0m = all_code[1].find('output') + 8
        #to = all_code[1].find('\')')

        #if 'output' in all_code[1]:
        #        if '=' in all_code[1]:
        #                print(all_code[1][fr0m:to])
        #        else:
        #                print(all_code[1][fr0m:to])


        #files = os.listdir(directory)

        #for i in range(len(files)):
        #        if 'txt' in files[i]:
        #                files[i] = files[i].replace('txt', 'npf')
        #                codes.append(files[i])


    #def get_folder(self):
    #
    #    folder = QFileDialog.getExistingDirectory(
    #        self, 'Project Data', '')
    #    if folder:
    #        print(folder)

    #def eventFilter(self, obj, event):
    #    if event.type() == QtCore.QEvent.KeyPress and obj is self.text:
    #        if event.key() == QtCore.Qt.Key_Return and self.text.hasFocus():
    #            print(str(self.cursor_position + 2) + ' - is cursor_position')
    #            self.count_lines_code(stroke = self.cursor_position + 2)
    #            #print(len(self.text.toPlainText().splitlines()) + 1, self.text.textCursor().blockNumber() + 2)
    #    return super().eventFilter(obj, event)


        #process = QtCore.QProcess(self)
        #self.text.setText([file])
        #process.start('notepad', [file])

        #self.setEnabled(False)
        #process.finished.connect(lambda: self.setEnabled(True))


        #filename = QFileDialog.getOpenFileName(self)


import os
import time
from os.path import abspath
import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon, QFont,  QWindow,  QKeySequence
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import (QWidget, QMenuBar, QTextBrowser, QTextEdit,
QMessageBox, QApplication, QAction, QMainWindow, QPushButton, QDesktopWidget,
QGridLayout, QFileDialog, QListWidget, QSpacerItem, QSizePolicy, QTableWidget,
QLineEdit, QLabel, QDoubleSpinBox, QAbstractItemView, QStatusBar, qApp, QMenu,
QMessageBox)
from PyQt5.QtCore import QCoreApplication, Qt, QSize, right

HTML_LINE_HEAD = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN"' \
+ ' "http://www.w3.org/TR/REC-html40/strict.dtd">' \
+ '<html><head><meta name="qrichtext" content="1" /><style type="text/css">' \
+ 'p, li {white-space: pre-wrap; user-select: none;}' \
+ '</style></head><body style=" font-family:\'MS Shell Dlg 2\';' \
+ ' font-size:8.25pt; font-weight:400; font-style:normal;">'
HTML_LINE_FOOT = '</body></html>'

directory = abspath(__file__)
file_name = 'first_program.nep'

codes = []
number_lines_of_code = 0

shell_text_const = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Courier New\'; font-size:10pt;">Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Courier New\'; font-size:10pt;">Type "help", "copyright", "credits" or "license()" for more information.</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Courier New\'; font-size:10pt;">>>> </span></p>'''

shell_plain_text = '''Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> '''

shell_text = shell_plain_text

def center_the_window(class_name):

    qr = class_name.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    class_name.move(qr.topLeft())

def process_click(class_name, info = None):
    cursor = class_name.text.textCursor()
    class_name.cursor_position = cursor.blockNumber()
    class_name.count_lines_code(stroke = cursor.blockNumber())
    if info == 'ln':
        return cursor.blockNumber()
    if info == 'col':
        return cursor.positionInBlock()
    #print(f'Стр {cursor.blockNumber()}, стлб {cursor.positionInBlock()}')

def create_StatusBar(class_name = None, widget = None):
    class_name.statusbar = class_name.statusBar()
    # Adding a temporary message
    class_name.statusbar.showMessage("Ready", 3000)
    # Adding a permanent message
    class_name.wcLabel = QLabel(f"{self.process_click(widget)} Words")
    class_name.statusbar.addPermanentWidget(self.wcLabel)

def open_file(class_name):

    file, _ = QtWidgets.QFileDialog.getOpenFileName(class_name,
                    'Открыть файл',
                    './',
                    'Neon Programs Files (*.nep)')
    if not file:
        return

    #filename = QFileDialog.getOpenFileName(self)
    print_code(file)

    #process = QtCore.QProcess(self)
    #self.text.setText([file])
    #process.start('notepad', [file])

    #self.setEnabled(False)
    #process.finished.connect(lambda: self.setEnabled(True))

def print_code(direct):
    file_name = 'first_program.nep'

    code = open(direct,'r')
    lines_code = code.readlines()
    all_code = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;">'''

    for i in lines_code:
            if i == '\n':
                all_code = all_code + '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Courier New\'; font-size:10pt;"> </span></p>'
            else:
                all_code = all_code + '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Courier New\'; font-size:10pt;">' + i + '</span></p>'
    all_code += '</body></html>'
    edit = MainWindowCompile()
    edit.show()
    edit.main_widget.text.setText(all_code)

    code.close()


#################################################################################################################################
#███╗░░░███╗░█████╗░██╗███╗░░██╗░██╗░░░░░░░██╗██╗███╗░░██╗██████╗░░█████╗░░██╗░░░░░░░██╗░██████╗██╗░░██╗███████╗██╗░░░░░██╗░░░░░#
#████╗░████║██╔══██╗██║████╗░██║░██║░░██╗░░██║██║████╗░██║██╔══██╗██╔══██╗░██║░░██╗░░██║██╔════╝██║░░██║██╔════╝██║░░░░░██║░░░░░#
#██╔████╔██║███████║██║██╔██╗██║░╚██╗████╗██╔╝██║██╔██╗██║██║░░██║██║░░██║░╚██╗████╗██╔╝╚█████╗░███████║█████╗░░██║░░░░░██║░░░░░#
#██║╚██╔╝██║██╔══██║██║██║╚████║░░████╔═████║░██║██║╚████║██║░░██║██║░░██║░░████╔═████║░░╚═══██╗██╔══██║██╔══╝░░██║░░░░░██║░░░░░#
#██║░╚═╝░██║██║░░██║██║██║░╚███║░░╚██╔╝░╚██╔╝░██║██║░╚███║██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██████╔╝██║░░██║███████╗███████╗███████╗#
#╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝#
#################################################################################################################################


class MainWindowShell(QMainWindow):

    def __init__(self, parent=None):
        super().__init__()
        self.main_widget = Shell(self)
        self.setCentralWidget(self.main_widget)
        self.init_UI()

    def init_UI(self):
        self.resize(670, 680)
        center_the_window(self)
        self.setWindowTitle('Neon 1.0.0 Shell')
        self.setWindowIcon(QIcon(directory.replace('neon.py', 'icon_Neon_IDE.png')))
        #self.text.cursorPositionChanged.connect(self.process_click)


##########################################
#░██████╗██╗░░██╗███████╗██╗░░░░░██╗░░░░░#
#██╔════╝██║░░██║██╔════╝██║░░░░░██║░░░░░#
#╚█████╗░███████║█████╗░░██║░░░░░██║░░░░░#
#░╚═══██╗██╔══██║██╔══╝░░██║░░░░░██║░░░░░#
#██████╔╝██║░░██║███████╗███████╗███████╗#
#╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝#
##########################################


class Shell(QWidget):

    ''' Documentation of Neon Shell
    pass
    '''

    def __init__(self, parent):
        super().__init__()
        super(Shell, self).__init__(parent)
        self.parent = parent
        self.shell_plain_text = '''Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
        Type "help", "copyright", "credits" or "license()" for more information.
        >>> '''
        self.shell_text_const = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Courier New\'; font-size:10pt;">Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Courier New\'; font-size:10pt;">Type "help", "copyright", "credits" or "license()" for more information.</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Courier New\'; font-size:10pt;">>>> </span></p>'''
        self.shell_text = ''
        self.initUI()

    def initUI(self):
        self.layout = QGridLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setHorizontalSpacing(0)
        self.layout.setVerticalSpacing(0)

        self.newAction = QAction('Новый файл', self)
        self.newAction.setShortcut('Ctrl+N')
        self.newAction.setStatusTip('New file')
        self.newAction.triggered.connect(lambda x: open_file(self)) #Сделать открытие диалогового окна на создание файла

        self.openAction = QAction('Открыть файл', self)
        self.openAction.setShortcut('Ctrl+O')
        self.openAction.setStatusTip('Open file')
        self.openAction.triggered.connect(lambda x: open_file(self))

        self.menu = QMenuBar()
        self.layout.addWidget(self.menu, 1, 0)
        self.file = self.menu.addMenu('Файл')
        self.file.addAction(self.openAction)
        self.file.addAction(self.newAction)
        #self.edit = self.menu.addMenu('Правка')
        #self.edit.addAction(self.exitAction)
        #self.options = self.menu.addMenu('Настройки')
        #self.options.addAction(self.exitAction)
        #self.faq = self.menu.addMenu('Справка')
        #self.faq.addAction(self.exitAction)

        self.lines = QTextEdit()
        self.lines.setText(self.shell_text_const)
        self.lines.textChanged.connect(self.set_text_for_shell)
        self.layout.addWidget(self.lines, 1, 0)
        #self.lines.textChanged.connect(self.compiling)
        self.checking_cursor()

    def set_text_for_shell(self):
        self.shell_text = self.lines.toPlainText()
        if self.shell_plain_text not in self.shell_text:
            self.lines.setText(self.shell_text_const)
            self.checking_cursor()
        if len(self.shell_text) >= 1 and shell_text[-1] == '''
''':
            #pass
            print(self.shell_text[:-1].replace(self.shell_plain_text, ''))
            self.shell_text_const = self.shell_text_const[:-11] + (self.shell_text[:-1].replace(self.shell_plain_text, '')) + '''</span></p>'''
            self.shell_plain_text = self.shell_text
            #self.layout.removeWidget(self.lines)
            #self.lines.deleteLater()
            #self.lines = QTextEdit()
            self.lines.blockSignals(True)
            self.lines.setText(shell_text_const)
            self.lines.blockSignals(False)
            print(self.shell_text_const)
        self.checking_cursor()

    def checking_cursor(self):
        #self.shell_text = self.lines.toPlainText()
        self.cursor = self.lines.textCursor()
        self.cursor.setPosition(len(self.shell_text))
        #self.cursor.setPosition(len(shell_text), QtGui.QTextCursor.KeepAnchor)
        self.lines.setTextCursor(self.cursor)


#    def interpret_the_code(self):
#        pass


###############################################################################################################################################
#███╗░░░███╗░█████╗░██╗███╗░░██╗░██╗░░░░░░░██╗██╗███╗░░██╗██████╗░░█████╗░░██╗░░░░░░░██╗░█████╗░░█████╗░███╗░░░███╗██████╗░██╗██╗░░░░░███████╗#
#████╗░████║██╔══██╗██║████╗░██║░██║░░██╗░░██║██║████╗░██║██╔══██╗██╔══██╗░██║░░██╗░░██║██╔══██╗██╔══██╗████╗░████║██╔══██╗██║██║░░░░░██╔════╝#
#██╔████╔██║███████║██║██╔██╗██║░╚██╗████╗██╔╝██║██╔██╗██║██║░░██║██║░░██║░╚██╗████╗██╔╝██║░░╚═╝██║░░██║██╔████╔██║██████╔╝██║██║░░░░░█████╗░░#
#██║╚██╔╝██║██╔══██║██║██║╚████║░░████╔═████║░██║██║╚████║██║░░██║██║░░██║░░████╔═████║░██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░██║██║░░░░░██╔══╝░░#
#██║░╚═╝░██║██║░░██║██║██║░╚███║░░╚██╔╝░╚██╔╝░██║██║░╚███║██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░██║███████╗███████╗#
#╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚══════╝#
###############################################################################################################################################


class MainWindowCompile(QMainWindow):

    def __init__(self, parent=None):
        super().__init__()
        self.main_widget = Compile(self)
        self.setCentralWidget(self.main_widget)
        self.init_UI()

    def init_UI(self):
        self.resize(670, 680)
        center_the_window(self)
        self.setWindowTitle(file_name + ' - ' + directory + ' (1.0.0)')
        self.setWindowIcon(QIcon(directory.replace('neon.py', 'icon_Neon_IDE.png')))
        #self.text.cursorPositionChanged.connect(self.process_click)
        self.statusbar = self.statusBar()
        # Adding a temporary message
        self.statusbar.showMessage("Ready", 3000)
        # Adding a permself.wcLabel = QLabel(f"{self.main_widget.process_click()} Words")
        self.wcLabel = QLabel('Ln: 1   Col: 0')
        self.statusbar.addPermanentWidget(self.wcLabel)

    def setting(self):
        self.statusbar = self.statusBar()
        self.wcLabel.setText(f"Ln: {self.main_widget.process_click(info = 'ln') + 1}   Col: {self.main_widget.process_click(info = 'col')}")


########################################################
#░█████╗░░█████╗░███╗░░░███╗██████╗░██╗██╗░░░░░███████╗#
#██╔══██╗██╔══██╗████╗░████║██╔══██╗██║██║░░░░░██╔════╝#
#██║░░╚═╝██║░░██║██╔████╔██║██████╔╝██║██║░░░░░█████╗░░#
#██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░██║██║░░░░░██╔══╝░░#
#╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░██║███████╗███████╗#
#░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚══════╝#
########################################################


class Compile(QWidget):

    def __init__(self, parent):
        super().__init__()
        super(Compile, self).__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.layout = QGridLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setHorizontalSpacing(0)
        self.layout.setVerticalSpacing(0)

        self.runAction = QAction('Запустить отладку', self)
        self.runAction.setShortcut('F5')
        self.runAction.setStatusTip('Run file')
        self.runAction.triggered.connect(self.open_file)

        self.openAction = QAction('Открыть файл', self)
        self.openAction.setShortcut('Ctrl+O')
        self.openAction.setStatusTip('Open file')
        self.openAction.triggered.connect(lambda: open_file(self))

        self.exitAction = QAction('Запустить отладку', self)
        self.exitAction.setShortcut('F5')
        self.exitAction.setStatusTip('Run file')
        self.exitAction.triggered.connect(self.open_file) #compile_code

        self.menu = QMenuBar()
        self.layout.addWidget(self.menu, 0, 0, 1, 2)
        self.file = self.menu.addMenu('Файл')
        self.file.addAction(self.openAction)
        self.edit = self.menu.addMenu('Правка')
        self.edit.addAction(self.exitAction)
        self.correct = self.menu.addMenu('Выделение')
        self.correct.addAction(self.exitAction)
        self.view = self.menu.addMenu('Вид')
        self.view.addAction(self.exitAction)
        self.moving = self.menu.addMenu('Переход')
        self.moving.addAction(self.exitAction)
        self.run = self.menu.addMenu('Выполнить')
        self.run.addAction(self.runAction)
        self.terminal = self.menu.addMenu('Терминал')
        self.terminal.addAction(self.exitAction)
        self.faq = self.menu.addMenu('Справка')
        self.faq.addAction(self.exitAction)

        self.lines = QTextBrowser()
        self.lines.setMaximumWidth(42)
        self.layout.addWidget(self.lines, 1, 0)

        self.text = QTextEdit()
        self.layout.addWidget(self.text, 1, 1)
        self.text.installEventFilter(self)
        self.text.setLineWrapMode(QTextEdit.NoWrap)
        self.text.setFocus()
        lambda: open_file(self)

        self.text.cursorPositionChanged.connect(self.parent.setting)

        self.count_lines_code()
        self.text.textChanged.connect(lambda: self.count_lines_code(self.process_click(info = 'ln')))

        self.list_of_tables = [self.lines,self.text]

        for tbl in self.list_of_tables:
            scrollbar = tbl.verticalScrollBar()
            scrollbar.valueChanged.connect(lambda idx,bar=scrollbar: self.move_other_scrollbars(idx, bar))

        self.lines.setVerticalScrollBarPolicy(True)

    def process_click(self, info = None):
        cursor = self.text.textCursor()
        self.cursor_position = cursor.blockNumber()
        self.count_lines_code(stroke = cursor.blockNumber())
        print(f'Стр {cursor.blockNumber()}, стлб {cursor.positionInBlock()}')
        if info == 'ln':
            return cursor.blockNumber()
        if info == 'col':
            return cursor.positionInBlock()

    def move_other_scrollbars(self, idx, bar):

            scrollbars = {tbl.verticalScrollBar() for tbl in self.list_of_tables}
            scrollbars.remove(bar)
            for bar in scrollbars:
                bar.setValue(idx)

    def closeEvent(self, event):

        box = QMessageBox()
        box.setIcon(QMessageBox.Question)
        box.setWindowTitle('Внимание!')
        box.setText('Вы уверены, что хотите выйти из IDE?')
        box.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        buttonY = box.button(QMessageBox.Yes)
        buttonY.setText('Да')
        buttonN = box.button(QMessageBox.No)
        box.setDefaultButton(QMessageBox.No)
        buttonN.setText('Нет')
        box.exec_()

        if box.clickedButton() == buttonY:
            event.accept()
        else:
            event.ignore()

    def compile_code(self):

        self.create_window = MainWindowShell()
        #self.create_window.compiling(self.text.toPlainText())

    def count_lines_code(self, stroke = 0):
        number_lines_of_code = len(self.text.toPlainText().splitlines())
        try:
            if self.text.toPlainText()[-1] == '''
''':
                number_lines_of_code += 1
        except:
            print('all')
        self.print_numbers_stroke(number_lines_of_code, grey = stroke)

    def print_numbers_stroke(self, number, grey = -1):
        print(number, grey)
        html_body = ''''''
        for i in range(number):
            if i == grey and grey != -1:
                html_body += '<p align="right" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#808080;"><span style=" font-family:\'Courier New\'; font-size:10pt;">' + str(i + 1) + '</span></p>'
            else:
                html_body += '<p align="right" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Courier New\'; font-size:10pt;">' + str(i + 1) + '</span></p>'

        self.lines.setText(HTML_LINE_HEAD + html_body + '<p align="right" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Courier New\'; font-size:10pt;">  </span></p>' + HTML_LINE_FOOT)

    def open_file(self):

        file, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                        'Открыть файл',
                        './',
                        'Neon Programs Files (*.nep)')
        if not file:
            return

        self.print_code(file)

    def print_code(self, direct):
        file_name = 'first_program.nep'

        code = open(direct,'r')
        lines_code = code.readlines()
        self.all_code = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;">'''

        for i in lines_code:
                if i == '\n':
                    self.all_code = self.all_code + '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Courier New\'; font-size:10pt;"> </span></p>'
                else:
                    self.all_code = self.all_code + '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Courier New\'; font-size:10pt;">' + i + '</span></p>'
        self.all_code += '</body></html>'

        code.close()
        #self.edit = MainWindowCompile()
        return self.all_code

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = MainWindowShell()
    main_window.show()
    sys.exit(app.exec_())
