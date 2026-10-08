import sys

from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QFont, QFontMetrics
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSplitter,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("UI Test")
        self.setMinimumSize(800, 600)

        self.edit_buttons: list[QPushButton] = []
        self.tool_buttons: list[QPushButton] = []

        self.vertical_splitter = QSplitter(Qt.Orientation.Vertical)
        self.vertical_splitter.setHandleWidth(6)
        self.vertical_splitter.setStyleSheet(
            "QSplitter::handle { background-color: #ffff00 ; }"
        )

        self.window_frame = QWidget()
        self.window_frame.setStyleSheet("background-color: #b00000;")
        frame_layout = QVBoxLayout(self.window_frame)
        frame_layout.setContentsMargins(35, 35, 35, 35)
        frame_layout.setSpacing(0)

        self.top_bar = QWidget()
        self.top_bar.setMinimumHeight(40)
        self.top_bar.setStyleSheet("background-color: #ff6800;")
        top_layout = QHBoxLayout(self.top_bar)
        top_layout.setContentsMargins(0, 0, 0, 0)
        top_layout.setSpacing(0)

        top_labels = ("File", "Edit", "View")
        top_colors = (("#004500", "#00c8df"), ("#000055", "#ff6800"))
        top_layout.addStretch(1)
        for index, text in enumerate(top_labels):
            background, foreground = top_colors[index % len(top_colors)]
            button = QPushButton(text)
            button.setSizePolicy(
                QSizePolicy.Policy.Expanding,
                QSizePolicy.Policy.Expanding,
            )
            button.setStyleSheet(
                "QPushButton { background-color: "
                f"{background}; color: {foreground}; "
                "border: 0; padding: 0; }"
            )
            top_layout.addWidget(button, 1)
            self.edit_buttons.append(button)
        top_layout.addStretch(1)

        self.horizontal_splitter = QSplitter(Qt.Orientation.Horizontal)
        self.horizontal_splitter.setHandleWidth(6)
        self.horizontal_splitter.setStyleSheet(
            "QSplitter::handle { background-color: #ffff00 ; }"
        )

        self.side_bar = QWidget()
        self.side_bar.setMinimumWidth(40)
        self.side_bar.setStyleSheet(
            "background-color: #000055; border: 1px solid #ffff00;"
        )
        self.tool_layout = QGridLayout(self.side_bar)
        self.tool_layout.setContentsMargins(0, 0, 0, 0)
        self.tool_layout.setSpacing(0)
        self.tool_layout.setAlignment(
            Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft
        )

        for _ in range(8):
            button = QPushButton("Tool")
            button.setSizePolicy(
                QSizePolicy.Policy.Fixed,
                QSizePolicy.Policy.Fixed,
            )
            color = "#FF6500" if len(self.tool_buttons) % 2 == 0 else "#008000"
            button.setStyleSheet(
                "QPushButton { background-color: "
                f"{color}; color: #000000; border: 0; padding: 0; }}"
            )
            self.tool_buttons.append(button)

        self.main_area = QWidget()
        self.main_area.setStyleSheet("background-color: #120012;")
        main_layout = QVBoxLayout(self.main_area)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        label = QLabel("UI Layout Test Area")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("color: #FFFFFF;")
        self.main_area_labels = [label]
        self.top_bar_size_label = QLabel()
        self.top_bar_size_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top_bar_size_label.setStyleSheet("color: #FFFFFF;")
        self.main_area_labels.append(self.top_bar_size_label)
        self.side_bar_size_label = QLabel()
        self.side_bar_size_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.side_bar_size_label.setStyleSheet("color: #FFFFFF;")
        self.main_area_labels.append(self.side_bar_size_label)
        main_layout.addStretch(1)
        main_layout.addWidget(label)
        main_layout.addWidget(self.top_bar_size_label)
        main_layout.addWidget(self.side_bar_size_label)
        main_layout.addStretch(1)

        self.horizontal_splitter.addWidget(self.side_bar)
        self.horizontal_splitter.addWidget(self.main_area)
        self.horizontal_splitter.setCollapsible(0, False)
        self.horizontal_splitter.setCollapsible(1, False)
        self.horizontal_splitter.setStretchFactor(0, 0)
        self.horizontal_splitter.setStretchFactor(1, 1)

        self.vertical_splitter.addWidget(self.top_bar)
        self.vertical_splitter.addWidget(self.horizontal_splitter)
        self.vertical_splitter.setCollapsible(0, False)
        self.vertical_splitter.setCollapsible(1, False)
        self.vertical_splitter.setStretchFactor(0, 0)
        self.vertical_splitter.setStretchFactor(1, 1)
        frame_layout.addWidget(self.vertical_splitter)
        self.setCentralWidget(self.window_frame)

        self.vertical_splitter.splitterMoved.connect(self._update_layout)
        self.horizontal_splitter.splitterMoved.connect(self._update_layout)
        QTimer.singleShot(0, self._set_initial_sizes)

    def _set_initial_sizes(self) -> None:
        self.vertical_splitter.setSizes(
            [100, max(1, self.vertical_splitter.height() - 106)]
        )
        self.horizontal_splitter.setSizes(
            [80, max(1, self.horizontal_splitter.width() - 86)]
        )
        self._update_layout()

    def _update_layout(self, *_args: int) -> None:
        self.top_bar_size_label.setText(
            f"Yläpalkin korkeus: {self.top_bar.height()} px"
        )
        self.side_bar_size_label.setText(
            f"Sivupalkin leveys: {self.side_bar.width()} px"
        )

        available = self.side_bar.contentsRect().size()
        width = available.width()
        height = available.height()
        if width > 0 and height > 0:
            columns = max(
                range(1, len(self.tool_buttons) + 1),
                key=lambda count: min(
                    width // count,
                    height // ((len(self.tool_buttons) + count - 1) // count),
                ),
            )
            rows = (len(self.tool_buttons) + columns - 1) // columns
            button_size = max(1, min(width // columns, height // rows))

            while self.tool_layout.count():
                self.tool_layout.takeAt(0)

            for index, button in enumerate(self.tool_buttons):
                button.setFixedSize(button_size, button_size)
                self.tool_layout.addWidget(
                    button,
                    index // columns,
                    index % columns,
                )

            self.tool_layout.activate()
        self._update_fonts()

    def _update_fonts(self, *_args: int) -> None:
        for buttons, minimum, maximum in (
            (self.edit_buttons, 12, 72),
            (self.tool_buttons, 10, 48),
        ):
            font_size = minimum
            for candidate in range(maximum, minimum - 1, -1):
                fits = True
                for button in buttons:
                    font = QFont(button.font())
                    font.setPixelSize(candidate)
                    metrics = QFontMetrics(font, button)
                    contents = button.contentsRect()
                    if (
                        metrics.horizontalAdvance(button.text()) > contents.width() - 16
                        or metrics.height() > contents.height() - 8
                    ):
                        fits = False
                        break
                if fits:
                    font_size = candidate
                    break

            for button in buttons:
                font = QFont(button.font())
                font.setPixelSize(font_size)
                button.setFont(font)

        top_bar_font = self.edit_buttons[0].font()
        for label in self.main_area_labels:
            label.setFont(top_bar_font)

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self._update_layout()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())
