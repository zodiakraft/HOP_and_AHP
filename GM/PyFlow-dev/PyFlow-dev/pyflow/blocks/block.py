# Pyflow an open-source tool for modular visual programing in python
# Copyright (C) 2021-2022 Bycelium <https://www.gnu.org/licenses/>
# pylint:disable=unused-argument

""" Module for the base Block."""

from typing import TYPE_CHECKING, List, Optional, OrderedDict, Tuple, Union

from PyQt5.QtCore import QPointF, QRectF, Qt
from PyQt5.QtGui import QBrush, QPen, QColor, QPainter, QPainterPath
from PyQt5.QtWidgets import (
    QGraphicsItem,
    QGraphicsProxyWidget,
    QGraphicsSceneMouseEvent,
    QStyleOptionGraphicsItem,
    QWidget,
)

from pyflow.core.serializable import Serializable
from pyflow.core.socket import Socket
from pyflow.blocks.widgets import Splitter, SizeGrip, Title

if TYPE_CHECKING:
    from pyflow.scene.scene import Scene

BACKGROUND_COLOR = QColor("#E3212121")


class Block(QGraphicsItem, Serializable):

    """Base class for blocks in Pyflow."""

    DEFAULT_DATA = {
        "title": "New block",
        "splitter_pos": [0, 0],
        "width": 618,
        "height": 184,
        "metadata": {
            "title_metadata": {"color": "white", "font": "Ubuntu", "size": 10}
        },
        "sockets": [],
    }
    MANDATORY_FIELDS = {"block_type", "position"}

    def __init__(
        self,
        block_type: str = "Block",
        position: tuple = (0, 0),
        width: int = DEFAULT_DATA["width"],
        height: int = DEFAULT_DATA["height"],
        edge_size: float = 10.0,
        title: Union[Title, str] = DEFAULT_DATA["title"],
        parent: Optional["QGraphicsItem"] = None,
    ):
        """Base class for blocks in Pyflow.

        Args:
            block_type: Block type.
            position: Block position in the scene.
            width: Block width.
            height: Block height.
            edge_size: Block edges size.
            title: Block title.
            parent: Parent of the block.

        """
        QGraphicsItem.__init__(self, parent=parent)
        Serializable.__init__(self)

        self.block_type = block_type
        self.setPos(QPointF(*position))
        self.sockets_in: List[Socket] = []
        self.sockets_out: List[Socket] = []

        self.pen_width = 3
        self._pen_outline = QPen(QColor("#00000000"))
        self._pen_outline.setWidth(self.pen_width)
        self._pen_outline_selected = QPen(QColor("#FFFFA637"))
        self._pen_outline_selected.setWidth(self.pen_width)
        self._brush_background = QBrush(BACKGROUND_COLOR)

        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)

        self.setAcceptHoverEvents(True)

        self.holder = QGraphicsProxyWidget(self)
        self.root = QWidget()
        self.root.setAttribute(Qt.WA_TranslucentBackground)
        self.root.setGeometry(0, 0, int(width), int(height))

        self.title_widget = Title(title, parent_widget=self.root, parent_block=super())
        self.title_widget.setAttribute(Qt.WA_TranslucentBackground)

        self.splitter = Splitter(self, Qt.Vertical, self.root)

        self.size_grip = SizeGrip(self, self.root)

        if type(self) == Block:
            # This has to be called at the end of the constructor of
            # every class inheriting this.
            self.holder.setWidget(self.root)

        self.edge_size = edge_size
        self.min_width = 300
        self.min_height = 100
        self.width = width
        self.height = height

        self.moved = False
        self.metadata = {}

    def scene(self) -> "Scene":
        """Get the current Scene containing the block."""
        return super().scene()

    def boundingRect(self) -> QRectF:
        """Get the the block bounding box."""
        return QRectF(0, 0, self.width, self.height).normalized()

    def paint(
        self,
        painter: QPainter,
        option: QStyleOptionGraphicsItem,
        widget: Optional[QWidget] = None,
    ):
        """Paint the block."""

        # content
        path_content = QPainterPath()
        path_content.setFillRule(Qt.FillRule.WindingFill)
        path_content.addRoundedRect(
            0, 0, self.width, self.height, self.edge_size, self.edge_size
        )
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(self._brush_background)
        painter.drawPath(path_content.simplified())

        # outline
        path_outline = QPainterPath()
        path_outline.addRoundedRect(
            0, 0, self.width, self.height, self.edge_size, self.edge_size
        )
        painter.setPen(self.pen_outline)
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawPath(path_outline.simplified())

        # selection inner outline
        if self.isSelected():
            path_in_outline = QPainterPath()
            outline_width = self.pen_outline.widthF()
            path_in_outline.addRoundedRect(
                -2 * outline_width,
                -2 * outline_width,
                self.width + 4 * outline_width,
                self.height + 4 * outline_width,
                self.edge_size + 2 * outline_width,
                self.edge_size + 2 * outline_width,
            )
            painter.setPen(self._pen_outline_selected)
            painter.setBrush(Qt.BrushStyle.NoBrush)
            painter.drawPath(path_in_outline.simplified())

    def add_socket(self, socket: Socket):
        """Add a socket to the block."""
        if socket.socket_type == "input":
            self.sockets_in.append(socket)
        else:
            self.sockets_out.append(socket)
        self.update_sockets()

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent):
        """Block reaction to a mouseReleaseEvent."""
        if self.moved:
            self.moved = False
            self.scene().history.checkpoint("Moved block", set_modified=True)
        super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent):
        """Block reaction to a mouseMoveEvent."""
        super().mouseMoveEvent(event)
        self.moved = True

        # Update the position of the sockets of this block
        # and the block it is connected to
        self.update_sockets()
        self.update_neighbors_sockets()

    def remove(self):
        """Remove the block from the scene containing it."""
        scene = self.scene()
        for socket in self.sockets_in + self.sockets_out:
            socket.remove()
        if scene is not None:
            scene.removeItem(self)

    def update_splitter(self):
        """Change the geometry of the splitter to match the block."""
        # We make the resizing of splitter only affect
        # the last element of the split view
        self.splitter.setGeometry(
            int(self.edge_size),
            int(self.edge_size + self.title_widget.height()),
            int(self.width - self.edge_size * 2),
            int(self.height - self.edge_size * 2 - self.title_widget.height()),
        )

    def update_title(self):
        """Change the geometry of the title to match the block."""
        self.title_widget.setGeometry(
            int(self.edge_size),
            int(self.edge_size / 2),
            int(self.width - self.edge_size * 3),
            int(self.title_widget.height()),
        )

    def update_size_grip(self):
        """Change the geometry of the size grip to match the block."""
        self.size_grip.setGeometry(
            int(self.width - self.edge_size * 2),
            int(self.height - self.edge_size * 2),
            int(self.edge_size * 1.7),
            int(self.edge_size * 1.7),
        )

    def get_socket_pos(self, socket: Socket) -> Tuple[float]:
        """Get a socket position to place them on the block sides."""
        if socket.socket_type == "input":
            y = 0
            sockets = self.sockets_in
        else:
            y = self.height
            sockets = self.sockets_out

        # Sockets are evenly spaced out on the whole block width
        space_between_sockets = self.width / (len(sockets) + 1)
        x = space_between_sockets * (sockets.index(socket) + 1)

        return x, y

    def update_sockets(self):
        """Update the sockets positions."""

        def x_end_position(socket: Socket) -> float:
            """x-coordinate of the end point of the first edge."""
            if not socket.edges:
                return 0
            return socket.edges[0].destination.x()

        def x_start_position(socket: Socket) -> float:
            """x-coordinate of the start point of the first edge."""
            if not socket.edges:
                return 0
            return socket.edges[0].source.x()

        self.sockets_in.sort(key=x_start_position)
        self.sockets_out.sort(key=x_end_position)

        for socket in self.sockets_in + self.sockets_out:
            socket.setPos(*self.get_socket_pos(socket))

    def update_neighbors_sockets(self):
        """Update the sockets positions of all neighboring blocks."""
        for socket in self.sockets_in:
            for edge in socket.edges:
                if edge.source_socket is not None:
                    edge.source_socket.block.update_sockets()
        for socket in self.sockets_out:
            for edge in socket.edges:
                if edge.destination_socket is not None:
                    edge.destination_socket.block.update_sockets()

    def update_all(self):
        """Update sockets and title."""
        self.update_sockets()
        self.update_splitter()
        self.update_title()
        self.update_size_grip()

    @property
    def title(self):
        """Block title."""
        return self.title_widget.text()

    @title.setter
    def title(self, value: str):
        if hasattr(self, "title_widget"):
            self.title_widget.setText(value)

    @property
    def width(self):
        """Block width."""
        return self.root.width()

    @width.setter
    def width(self, value: float):
        self.root.setGeometry(0, 0, int(value), self.root.height())

    @property
    def height(self):
        """Block height."""
        return self.root.height()

    @height.setter
    def height(self, value: float):
        self.root.setGeometry(0, 0, self.root.width(), int(value))

    @property
    def pen_outline(self) -> QPen:
        """The current pen used to draw the outline of the Block."""
        return self._pen_outline

    def serialize(self) -> OrderedDict:
        """Return a serialized version of this widget."""
        self.metadata.update({"title_metadata": self.title_widget.serialize()})
        metadata = OrderedDict(sorted(self.metadata.items()))
        return OrderedDict(
            [
                ("id", self.id),
                ("title", self.title),
                ("block_type", self.block_type),
                ("splitter_pos", self.splitter.sizes()),
                ("position", [self.pos().x(), self.pos().y()]),
                ("width", self.width),
                ("height", self.height),
                ("metadata", metadata),
                (
                    "sockets",
                    [
                        socket.serialize()
                        for socket in self.sockets_in + self.sockets_out
                    ],
                ),
            ]
        )

    def deserialize(self, data: dict, hashmap: dict = None, restore_id=True) -> None:
        """Restore the block from serialized data."""
        if restore_id and "id" in data:
            self.id = data["id"]

        self.complete_with_default(data)

        for dataname in ("title", "block_type", "width", "height"):
            setattr(self, dataname, data[dataname])

        self.setPos(QPointF(*data["position"]))
        self.metadata = dict(data["metadata"])
        self.title_widget.deserialize(
            self.metadata["title_metadata"], hashmap, restore_id
        )

        if "splitter_pos" in data:
            self.splitter.setSizes(data["splitter_pos"])

        if len(data["sockets"]) > 0:
            # Remove old sockets
            for socket in self.sockets_in + self.sockets_out:
                socket.remove()

            # Deserialize new sockets
            for socket_data in data["sockets"]:
                socket = Socket(block=self)
                socket.deserialize(socket_data, hashmap, restore_id)

                self.add_socket(socket)

                if hashmap is not None:
                    hashmap.update({socket_data["id"]: socket})

        self.update_all()
