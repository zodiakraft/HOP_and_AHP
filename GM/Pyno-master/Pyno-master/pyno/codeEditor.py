import pyglet
import pyperclip
import keyword
import tokenize
import io
import os

from pyno.utils import x_y_pan_scale, font
from pyno.draw import quad_aligned


highlight = set(list(__builtins__.keys()) +
                list(keyword.__dict__.keys()) +
                keyword.kwlist + 
                ['call', 'cleanup'])

x_shift = 40
y_shift = 20
layout_padding = 5
resize_button = 10
nline_width = 30
nline_padding = 2
help_offset = 5


class CodeEditor():
    '''
    Code editor is the window you define nodes function
    '''

    def __init__(self, node, highlighting=1):
        self.node = node  # node-owner of this codeEditor
        self.document = pyglet.text.document.FormattedDocument(node.code)

        self.highlighting = highlighting  # 0: off, 1: python (node), 2: file (sub)

        @self.document.event
        def on_insert_text(start, end):
            self.update_highlighting()

        @self.document.event
        def on_delete_text(start, end):
            self.update_highlighting()

        self.document.set_style(0, len(node.code),
                                dict(font_name=font,
                                font_size=11, color=(255, 255, 255, 230)))

        self.layout = pyglet.text.layout.IncrementalTextLayout(
                                self.document,
                                *node.editor_size,
                                multiline=True, wrap_lines=False)

        self.update_label = pyglet.text.Label('CTRL+ENTER to save and execute',
                                              font_name=font,
                                              anchor_y='top',
                                              font_size=9)

        self.line_numbering = pyglet.text.Label('',
                                                font_name=font,
                                                font_size=11,
                                                color=(255, 255, 255, 127),
                                                align='right',
                                                anchor_y='top',
                                                width=nline_width,
                                                multiline=True)

        self.autocomplete = pyglet.text.Label('',
                                              font_name=font,
                                              font_size=9,
                                              color=(125, 255, 125, 127))

        self.caret = pyglet.text.caret.Caret(self.layout)
        self.caret.color = (255, 255, 255)
        self.caret.visible = False
        self.hover = False
        self.hovered = True
        self.resize = False

        self.change = False

        self.pan_scale = [[0.0, 0.0], 1]
        self.screen_size = (800, 600)

    def update_node(self):
        # Push code to node
        self.node.new_code(self.document.text)
        self.node.need_update = True
        self.change = False

    def intersect_point(self, point):
        # Intersection with whole codeEditor
        l = self.layout
        if 0 < point[0] - l.x + 20 < l.width + 20 and \
           0 < point[1] - l.y < l.height + 10:
            self.node.hover = True
            return True
        return False

    def intersect_corner(self, point):
        # Intersection with bottom right corner to resize
        l = self.layout
        return (0 < point[0] - (l.x + l.width - resize_button) < resize_button and
                0 < point[1] - l.y < resize_button)

    def render(self):
        self.node.make_child_active()

        l = self.layout
        l.x = self.node.x + self.node.cw + x_shift
        l.y = self.node.y - l.height + self.node.ch + y_shift

        if self.change:
            self.update_label.x = l.x
            self.update_label.y = l.y - help_offset
            self.update_label.draw()

        if self.hover:
            if self.document.text and not self.hovered:
                self.hovered = True
                self.update_highlighting()

            color = self.node.color if not self.change else (255, 100, 10)

            #  codeEditor background
            quad_aligned(l.x - layout_padding, l.y,
                         l.width + layout_padding, l.height,
                         ((0, 0, 0) if not self.change
                                    else (20, 10, 5)) + (230,))

            if self.resize:
                quad_aligned(l.x - layout_padding, l.y + l.height,
                             self.node.editor_size[0] + layout_padding,
                             -self.node.editor_size[1],
                             color + (100,))

            #  codeEditor resize corner
            quad_aligned(l.x + l.width - resize_button, l.y,
                         resize_button, resize_button, color + (255,))

            #  codeEditor left line
            quad_aligned(l.x - layout_padding - nline_width, l.y,
                         nline_width, l.height, color + (255,))

            #  codeEditor left line numbering
            font_height = self.layout.content_height / self.layout.get_line_count()
            line_offset = (-self.layout.view_y) % font_height
            first_line = int(-self.layout.view_y / font_height)
            count_line = min(int((self.layout.height + line_offset) / font_height), self.layout.get_line_count())
            self.line_numbering.x = l.x - layout_padding - nline_width - nline_padding
            self.line_numbering.y = l.y + l.height + line_offset
            self.line_numbering.text = '\n'.join(['%02i'%i for i in range(first_line + 1, first_line + count_line + 1)])
            self.line_numbering.draw()

            #  codeEditor autocomplete hint
            self.autocomplete.x = l.x
            self.autocomplete.y = l.y + l.height + help_offset
            self.autocomplete.draw()
        else:
            if self.document.text and self.hovered:
                self.hovered = False
                self.document.set_style(0, len(self.node.code),
                                        dict(color=(255, 255, 255, 50)))

        self.layout.draw()

    def update_highlighting(self):
        if len(self.document.text) == 0:
            return

        # reset highlighting and hint
        self.document.set_style(0, len(self.document.text),
                                dict(color=(255, 255, 255, 255)))
        self.autocomplete.text = ""

        if self.highlighting == 0:    # 0: off
            return
        elif self.highlighting == 1:  # 1: python
            # rudimentary syntax highlighting and autocomplete hint
            newline_offset = ([-1] +
                              [i for i, ch in enumerate(self.document.text) if ch == '\n'] +
                              [len(self.document.text)])
            try:
                obj_string = ""
                for item in tokenize.tokenize(io.BytesIO(self.document.text.encode('utf-8')).readline):
                    start = newline_offset[item.start[0] - 1] + item.start[1] + 1
                    stopp = newline_offset[item.end[0] - 1] + item.end[1] + 1

                    # rudimentary autocomplete hint
                    if (item.type == tokenize.NAME) or (item.string == "."):
                        obj_string += item.string
                    else:
                        obj_string = ""
                    if (start <= self.caret.position <= stopp):
                        if not obj_string:
                            obj_string = item.string
                        try:
                            obj = eval(obj_string.strip(), self.node.env)
                            #print("Code hint:\n", obj.__doc__)
                            self.autocomplete.text = obj.__doc__.split("\n")[0]
                        except:
                            pass

                    # syntax highlighting
                    if (item.type == tokenize.NAME) and (item.string in highlight):
                        pass
                    elif (item.type in [tokenize.COMMENT, tokenize.OP, tokenize.NUMBER, tokenize.STRING]):
                        pass  # (we could e.g. set another color here...)
                    else:
                        continue  # do not highlight this token
                    self.document.set_style(start, stopp,
                                            dict(color=(255, 200, 100, 255)))
            except tokenize.TokenError:
                pass
        elif self.highlighting == 2:  # 2: file
            if os.path.exists(self.document.text):
                self.document.set_style(0, len(self.node.code),
                                        dict(color=(255, 200, 100, 255)))

    # --- Input events ---

    def on_mouse_press(self, x, y, button, modifiers):
        x, y = x_y_pan_scale(x, y, self.pan_scale, self.screen_size)

        if self.intersect_corner((x, y)):
            self.resize = True
        elif button == 1 and self.hover:
            self.set_focus()
            self.caret.on_mouse_press(x, y, button, modifiers)
            self.update_highlighting()

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        x, y = x_y_pan_scale(x, y, self.pan_scale, self.screen_size)
        dx, dy = int(dx / self.pan_scale[1]), int(dy / self.pan_scale[1])

        if buttons == 1 and self.resize:
            width = max(self.node.editor_size[0] + dx, 300)
            height = max(self.node.editor_size[1] - dy, 150)
            self.node.editor_size = width, height
        elif buttons == 1 and self.hover:
            self.caret.on_mouse_drag(x, y, dx, dy, buttons, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.resize:
            self.layout.width, self.layout.height = self.node.editor_size
            self.resize = False

    def on_text(self, text):
        if self.hover:
            self.change = True
            self.caret.on_text(text)

    def on_text_motion(self, motion):
        if self.hover:
            self.caret.on_text_motion(motion)

    def on_text_motion_select(self, motion):
        if self.hover:
            self.caret.on_text_motion_select(motion)

    def on_key_press(self, symbol, modifiers):
        key = pyglet.window.key

        if symbol == key.TAB:
            self.change = True
            self.document.insert_text(self.caret.position, '  ')
            self.caret.position += 2

        elif modifiers & key.MOD_CTRL and symbol == key.ENTER:
            print('Reload code')
            self.update_node()

        elif modifiers & key.MOD_CTRL:
            if symbol == key.C and self.caret.mark:
                self.copy_text()
            elif symbol == key.V:
                start = min(self.caret.position, self.caret.mark or self.caret.position)
                end = max(self.caret.position, self.caret.mark or self.caret.position)
                text = pyperclip.paste()
                self.document.delete_text(start, end)
                self.document.insert_text(self.caret.position, text)
                self.caret.position += len(text)
                self.caret.mark = self.caret.position
            elif symbol == key.X and self.caret.mark:
                start, end = self.copy_text()
                self.document.delete_text(start, end)
                self.caret.mark = self.caret.position

        elif symbol == key.BACKSPACE or symbol == key.DELETE:
            self.change = True

    def copy_text(self):
        start = min(self.caret.position, self.caret.mark)
        end = max(self.caret.position, self.caret.mark)
        text = self.document.text[start:end]
        pyperclip.copy(text)
        return (start, end)

    def set_focus(self):
        self.caret.visible = True
        self.caret.mark = 0
        self.caret.position = len(self.document.text)

    def __del__(self):
      self.layout.delete()
      self.update_label.delete()
      self.caret.delete()
