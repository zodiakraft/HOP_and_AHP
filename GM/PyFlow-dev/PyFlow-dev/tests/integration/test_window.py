# Pyflow an open-source tool for modular visual programing in python
# Copyright (C) 2021-2022 Bycelium <https://www.gnu.org/licenses/>

"""
Integration tests for the Window.
"""

import os
import pytest

from pytest_mock import MockerFixture
from pyflow.graphics.window import Window


class TestWindow:
    @pytest.fixture(autouse=True)
    def setup(self, mocker: MockerFixture):
        """Setup reused variables."""
        self.window = Window()

    def test_open_file(self, qtbot):
        """loads files."""
        wnd = Window()
        file_example_path = "./tests/assets/example_graph1.ipyg"
        subwnd = wnd.createNewMdiChild(os.path.abspath(file_example_path))
        subwnd.show()
        wnd.close()

    def test_window_close(self, qtbot):
        """closes."""
        self.window.close()
