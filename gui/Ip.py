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

from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QSlider, QMessageBox
from PyQt5.QtCore import Qt
from tools.IpTools import make_net_mask, calculate_all_parameters


class Ip(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("IP Address Calculator")

        self.label.setStyleSheet("font: 18pt Times New Roman")

        self.ip_input = QLineEdit()
        self.ip_input.setPlaceholderText("Enter ip address...")

        self.net_mask_input = QLineEdit()
        self.net_mask_input.setReadOnly(True)

        self.net_id = QLineEdit()
        self.net_id.setReadOnly(True)
        self.net_id_label = QLabel("Network id")
        self.net_id_label.setFixedSize(91, 20)

        self.first_address = QLineEdit()
        self.first_address.setReadOnly(True)
        self.first_address_label = QLabel("First address")
        self.first_address_label.setFixedSize(91, 20)

        self.last_address = QLineEdit()
        self.last_address.setReadOnly(True)
        self.last_address_label = QLabel("Last address")
        self.last_address_label.setFixedWidth(91)

        self.broadcast = QLineEdit()
        self.broadcast.setReadOnly(True)
        self.broadcast_label = QLabel("Broadcast")
        self.broadcast_label.setFixedSize(91, 20)

        self.max_hosts = QLineEdit()
        self.max_hosts.setReadOnly(True)
        self.max_hosts_label = QLabel("Max hosts")
        self.max_hosts_label.setFixedSize(91, 20)

        self.calculate_btn = QPushButton("Calculate")
        self.clear_btn = QPushButton("Clear")

        h1 = QHBoxLayout()
        h1.addStretch()
        h1.addWidget(self.label)
        h1.addStretch()

        labels = QHBoxLayout()
        self.ip_label = QLabel("Ip address")
        self.net_mask_label = QLabel("Netmask")
        labels.addWidget(self.ip_label)
        labels.addWidget(self.net_mask_label)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(2)
        self.slider.setMaximum(30)
        self.slider.setValue(24)
        self.slider.setTickInterval(1)
        self.slider.setTickPosition(QSlider.TicksBelow)

        self.net_mask_size = QLabel(str(self.slider.value()))
        self.update_netmask_size()

        h_box = QHBoxLayout()
        h_box.addWidget(self.ip_input)
        h_box.addWidget(self.net_mask_input)

        hh = QHBoxLayout()
        hh.addWidget(self.calculate_btn)
        hh.addWidget(self.clear_btn)

        h2 = QHBoxLayout()
        h2.addWidget(self.net_id_label)
        h2.addWidget(self.net_id)

        h3 = QHBoxLayout()
        h3.addWidget(self.first_address_label)
        h3.addWidget(self.first_address)

        h4 = QHBoxLayout()
        h4.addWidget(self.last_address_label)
        h4.addWidget(self.last_address)

        h5 = QHBoxLayout()
        h5.addWidget(self.broadcast_label)
        h5.addWidget(self.broadcast)

        h6 = QHBoxLayout()
        h6.addWidget(self.max_hosts_label)
        h6.addWidget(self.max_hosts)

        v_box = QVBoxLayout()
        v_box.addLayout(h1)
        v_box.addLayout(labels)
        v_box.addLayout(h_box)
        v_box.addWidget(self.slider)

        hhh = QHBoxLayout()
        hhh.addWidget(QLabel("Mask size"))
        hhh.addWidget(self.net_mask_size)
        v_box.addLayout(hhh)

        v_box.addLayout(h2)
        v_box.addLayout(h3)
        v_box.addLayout(h4)
        v_box.addLayout(h5)
        v_box.addLayout(h6)
        v_box.addLayout(hh)

        self.calculate_btn.clicked.connect(self.calculate)
        self.clear_btn.clicked.connect(self.clear)
        self.slider.valueChanged.connect(self.update_netmask_size)

        self.setWindowTitle("IP tools")
        self.setLayout(v_box)

        self.setStyleSheet("font: 12pt Times New Roman")
        self.show()

    def update_netmask_size(self):
        ones = self.slider.value()
        dot_decimal = make_net_mask(ones)
        self.net_mask_input.setText(dot_decimal)
        self.net_mask_size.setText(str(ones))

    def calculate(self):
        help_list = []
        if self.check_ip(self.ip_input.text()):
            help_list = calculate_all_parameters(self.ip_input.text(), self.net_mask_input.text())
            first = ""
            last = ""
            if help_list[1] == help_list[0] or help_list[1] == help_list[3]:
                first = "-"
            else:
                first = help_list[1]
            if help_list[2] == help_list[0] or help_list[2] == help_list[3]:
                last = "-"
            else:
                last = help_list[2]
            self.net_id.setText(help_list[0] + "/" + str(self.slider.value()))
            self.first_address.setText(first)
            self.last_address.setText(last)
            self.broadcast.setText(help_list[3])
            self.max_hosts.setText(str(help_list[4]))

    def check_ip(self, text):
        list_of_parts = text.split(".")
        if text == "":
            QMessageBox.about(self, "Warning!", "Ip address field cannot be left empty!")
            return False
        elif len(list_of_parts) != 4:
            QMessageBox.about(self, "Warning!", "Ip address contains four parts!")
            return False
        else:
            for part in list_of_parts:
                if not part.isdigit():
                    QMessageBox.about(self, "Warning!", "Ip address contains only numbers!")
                    return False
                if int(part) > 255:
                    QMessageBox.about(self, "Warning!", "Each part of an ip address must be lower than 256!")
                    return False
        return True

    def clear(self):
        self.net_id.clear()
        self.ip_input.clear()
        self.first_address.clear()
        self.last_address.clear()
        self.broadcast.clear()
        self.max_hosts.clear()
        self.slider.setValue(24)
        self.update_netmask_size()
