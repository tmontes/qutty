"""
QuTTY's entry point and single module.
"""

import sys

import importlib_metadata as ilm

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        meta = ilm.metadata(__package__)
        name = meta['name']
        version = meta['version']
        self.setWindowTitle(f'{name} {version}')

        self.resize(320, 240)
        self.setMinimumWidth(240)
        self.setMinimumHeight(160)

        layout = QVBoxLayout()
        layout.addStretch()

        button = QPushButton('Quit')
        button.clicked.connect(lambda: QApplication.quit())
        layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


def main():

    app = QApplication(sys.argv)

    win = MainWindow()
    win.show()

    app.exec_()


if __name__ == '__main__':

    main()
