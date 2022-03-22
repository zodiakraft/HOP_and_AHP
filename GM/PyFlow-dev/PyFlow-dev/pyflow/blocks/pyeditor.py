# Pyflow an open-source tool for modular visual programing in python
# Copyright (C) 2021-2022 Bycelium <https://www.gnu.org/licenses/>

""" Module for the PyFlow python editor."""

from typing import TYPE_CHECKING, Optional, OrderedDict, Tuple

from PyQt5.QtCore import Qt
from PyQt5.QtGui import (
    QFocusEvent,
    QFont,
    QFontMetrics,
    QColor,
    QKeyEvent,
    QWheelEvent,
)
from PyQt5.QtWidgets import QApplication
from PyQt5.Qsci import QsciScintilla, QsciLexerPython

from pyflow.core.editor import Editor
from pyflow.core.history import History
from pyflow.graphics.theme_manager import theme_manager


if TYPE_CHECKING:
    from pyflow.blocks.codeblock import CodeBlock

POINT_SIZE = 11


class PythonEditor(Editor):

    """In-block python editor for Pyflow."""

    def __init__(self, block: "CodeBlock"):
        """In-block python editor for Pyflow.
        Args:
            block: Block in which to add the python editor widget.
        """
        super().__init__(block)
        self.block: "CodeBlock" = self.block  # Add typechecking
        self.foreground_color = QColor("#dddddd")
        self.background_color = QColor("#212121")

        self.history = EditorHistory(self)

        self.update_theme()
        theme_manager().themeChanged.connect(self.update_theme)

        self.fontmetrics = QFontMetrics(self.font())

        # Set caret
        self._caret_color = QColor("#D4D4D4")
        self.setCaretForegroundColor(self._caret_color)

        # Indentation
        self.setAutoIndent(True)
        self.setTabWidth(4)
        self.setIndentationGuides(True)
        self.setIndentationsUseTabs(False)
        self.setBackspaceUnindents(True)

        # Disable horizontal scrollbar
        self.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR, 0)

        # # Add folding
        self.setFolding(QsciScintilla.FoldStyle.CircledTreeFoldStyle, 1)
        self.setFoldMarginColors(self.background_color, self.background_color)
        self.setMarkerForegroundColor(self.foreground_color, 1)
        self.setMarkerBackgroundColor(self.background_color, 1)

        # Add background transparency
        self.setStyleSheet("background:transparent")
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

    def update_theme(self):
        """Change the font and colors of the editor to match the current theme"""
        font = QFont()
        font.setFamily(theme_manager().recommended_font_family)
        font.setFixedPitch(True)
        font.setPointSize(POINT_SIZE)
        self.setFont(font)

        # Margin 0 is used for line numbers
        self.fontmetrics = QFontMetrics(self.font())
        self.setMarginsFont(font)
        self.setMarginWidth(0, self.fontmetrics.width("00") + 6)
        self.setMarginLineNumbers(0, True)
        self.setMarginsForegroundColor(self.foreground_color)
        self.setMarginsBackgroundColor(self.background_color)

        lexer = QsciLexerPython()
        theme_manager().current_theme().apply_to_lexer(lexer)
        lexer.setFont(font)
        self.setLexer(lexer)

    def wheelEvent(self, event: QWheelEvent) -> None:
        """How PythonEditor handles wheel events"""
        if self.mode == "EDITING" and event.angleDelta().x() == 0:
            event.accept()
            return super().wheelEvent(event)

    def focusOutEvent(self, event: QFocusEvent) -> None:
        """PythonEditor reaction to PyQt focusOut events."""
        self.block.source = self.text()
        self.block.scene().history.checkpoint(
            "A codeblock source was updated", set_modified=True
        )
        self.history.checkpoint()
        return super().focusOutEvent(event)

    def focusInEvent(self, event: QFocusEvent) -> None:
        text_len = self.SendScintilla(self.SCI_GETLENGTH)
        self.SendScintilla(self.SCI_GOTOPOS, text_len)
        return super().focusInEvent(event)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        """PythonEditor reaction to PyQt keyPressed events."""

        # Disable QsciScintilla undo
        self.SendScintilla(QsciScintilla.SCI_EMPTYUNDOBUFFER, 1)

        # Check if Shift+Return is pressed
        # If so, the cell should be (left) run
        shift_is_pressed: bool = (
            QApplication.keyboardModifiers() == Qt.KeyboardModifier.ShiftModifier
        )
        if shift_is_pressed:
            if event.key() in {Qt.Key.Key_Return, Qt.Key.Key_Enter}:
                self.block.run_left()
                return

        # Manualy check if Ctrl+Z or Ctrl+Y is pressed
        control_is_pressed: bool = (
            QApplication.keyboardModifiers() == Qt.KeyboardModifier.ControlModifier
        )
        if control_is_pressed and event.key() == Qt.Key.Key_Z:
            # The sequence ends and a new one starts when pressing Ctrl+Z
            self.history.end_sequence()
            self.history.start_sequence()
            self.history.undo()
        elif control_is_pressed and event.key() == Qt.Key.Key_Y:
            self.history.redo()
        elif not control_is_pressed:
            self.history.start_sequence()

        if event.key() in {Qt.Key.Key_Return, Qt.Key.Key_Enter}:
            self.history.end_sequence()

        super().keyPressEvent(event)


class EditorHistory(History):
    """
    Helper object to handle undo/redo operations on a PythonEditor.
    Args:
        editor: PythonEditor reference.
        max_stack: Maximum size of the history stack (number of available undo).
    """

    def __init__(self, editor: "PythonEditor", max_stack: int = 50):
        self.editor: "PythonEditor" = editor
        self.is_writing = False
        super().__init__(max_stack)

    def start_sequence(self):
        """
        Start a new writing sequence if it was not already the case, and save the current state.
        """
        if not self.is_writing:
            self.is_writing = True
            self.checkpoint()

    def end_sequence(self):
        """
        End the writing sequence if it was not already the case.
        Do not save at this point because the writing parameters to be saved (cursor pos, etc)
        are the one of the beginning of the next sequence.
        """
        self.is_writing = False

    def checkpoint(self):
        """
        Store a snapshot of the editor's text and parameters in the history stack
        (only if the text has changed).
        """
        text: str = self.editor.text()
        old_data = self.restored_data()
        if old_data is not None and old_data["text"] == text:
            return

        cursor_pos: Tuple[int, int] = self.editor.getCursorPosition()
        scroll_pos: int = self.editor.verticalScrollBar().value()
        self.store(
            {
                "text": text,
                "cursor_pos": cursor_pos,
                "scroll_pos": scroll_pos,
            }
        )

    def restore(self):
        """
        Restore the editor's text and parameters
        using the snapshot pointed by current in the history stack.
        """
        data: Optional[OrderedDict] = self.restored_data()

        if data is not None:
            self.editor.setText(data["text"])
            self.editor.setCursorPosition(*data["cursor_pos"])
            self.editor.verticalScrollBar().setValue(data["scroll_pos"])
