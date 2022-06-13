"""
QuTTY's entry point and single module.
"""

import sys

import importlib_metadata as ilm
import importlib_resources as ilr

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        meta = ilm.metadata(__package__)
        name = meta['name']
        version = meta['version']
        self.setWindowTitle(f'{name} {version}')

        self.resize(360, 400)
        self.setMinimumWidth(280)
        self.setMinimumHeight(320)

        layout = QVBoxLayout()

        logo_filename = ilr.files(__package__) / 'logo.png'
        logo = QPixmap(str(logo_filename))
        label = QLabel()
        label.setPixmap(logo)
        layout.addWidget(label, alignment=Qt.AlignCenter)

        button = QPushButton('Quit')
        button.clicked.connect(QApplication.quit)
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
