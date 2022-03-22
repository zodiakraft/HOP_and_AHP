# Pyflow an open-source tool for modular visual programing in python
# Copyright (C) 2021-2022 Bycelium <https://www.gnu.org/licenses/>

""" Module for the SliderBlock.

A block that can allows dynamic value modification using a slider.

"""

from typing import OrderedDict
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QSlider, QVBoxLayout
from pyflow.blocks.executableblock import ExecutableBlock


class SliderBlock(ExecutableBlock):
    """
    Features a slider ranging from 0 to 1 and an area to choose what value to assign the slider to.
    """

    def __init__(self, **kwargs):
        super().__init__(block_type="SliderBlock", **kwargs)

        self.layout = QVBoxLayout(self.root)

        self.slider = QSlider(Qt.Horizontal)

        self.variable_layout = QHBoxLayout()
        self.variable_text = QLineEdit("slider_value")
        self.variable_value = QLabel(f"{self.slider.value()/100}")

        self.variable_text.setFixedWidth(int(self.root.width() / 2))

        self.variable_layout.addWidget(self.variable_text)
        self.variable_layout.addWidget(self.variable_value)

        self.layout.setContentsMargins(
            int(self.edge_size * 2),
            int(self.title_widget.height() + self.edge_size * 2),
            int(self.edge_size * 2),
            int(self.edge_size * 2),
        )
        self.layout.addWidget(self.slider)
        self.layout.addLayout(self.variable_layout)

        self.slider.valueChanged.connect(self.valueChanged)

        self.holder.setWidget(self.root)

    def valueChanged(self):
        """This is called when the value of the slider changes."""
        self.variable_value.setText(f"{self.value}")
        # Make sure that the slider is initialized before trying to run it.
        if self.scene() is not None:
            self.run_right()

    @property
    def source(self):
        """The "source code" of the slider i.e an assignement to the value of the slider."""
        python_code = f"{self.var_name} = {self.value}"
        return python_code

    @source.setter
    def source(self, value: str):
        raise RuntimeError("The source of a sliderblock is read-only.")

    @property
    def value(self):
        """The value of the slider."""
        return str(self.slider.value() / 100)

    @value.setter
    def value(self, value: str):
        self.slider.setValue(int(float(value) * 100))

    @property
    def var_name(self):
        """The name of the python variable associated with the slider."""
        return self.variable_text.text()

    @var_name.setter
    def var_name(self, value: str):
        self.variable_text.setText(value)

    def serialize(self):
        """Return a serialized version of this widget."""
        base_dict = super().serialize()
        base_dict["value"] = self.value
        base_dict["var_name"] = self.var_name

        return base_dict

    def deserialize(
        self, data: OrderedDict, hashmap: dict = None, restore_id: bool = True
    ):
        """Restore a slider block from it's serialized state."""
        for dataname in ["value", "var_name"]:
            if dataname in data:
                setattr(self, dataname, data[dataname])

        super().deserialize(data, hashmap, restore_id)
