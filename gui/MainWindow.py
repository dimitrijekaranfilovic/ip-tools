"""
    Operations based around ip.
    Copyright (C) 2020  Dimitrije Karanfilović
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>
"""
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QScrollArea, QApplication
from gui.Ip import Ip
from gui.Subnetting import Subnetting
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.tab_widget = QTabWidget()
        self.tab_widget.addTab(Ip(), "Address calculator")
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(Subnetting())
        self.tab_widget.addTab(self.scroll_area, "Subnetting")

        self.setCentralWidget(self.tab_widget)
        self.setWindowTitle("IP address tools")
        self.setFixedSize(420, 400)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
