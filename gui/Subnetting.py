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
from tools.IpTools import make_net_mask, split_address


class Subnetting(QWidget):
    def __init__(self):
        super(Subnetting, self).__init__()

        self.title = QLabel("Subnetting")
        self.title.setStyleSheet("font: 18pt Times New Roman")

        self.ip_label = QLabel("Ip address")
        self.ip_input = QLineEdit()
        self.ip_input.setPlaceholderText("Enter ip address...")

        self.net_mask_label = QLabel("Netmask")
        self.net_mask_output = QLineEdit()
        self.net_mask_output.setReadOnly(True)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(2)
        self.slider.setMaximum(30)
        self.slider.setValue(24)
        self.slider.setTickInterval(1)
        self.slider.setTickPosition(QSlider.TicksBelow)

        self.split_btn = QPushButton("Split")
        self.clear_btn = QPushButton("Clear")

        self.mask_size_label = QLabel("Mask size")
        self.mask_size = QLabel()

        self.first_network_label = QLabel("First network")

        self.first_net_id = QLineEdit()
        self.first_net_id.setReadOnly(True)
        self.first_net_id_label = QLabel("Network id")
        self.first_net_id_label.setFixedSize(91, 20)

        self.first_first_address = QLineEdit()
        self.first_first_address.setReadOnly(True)
        self.first_first_address_label = QLabel("First address")
        self.first_first_address_label.setFixedSize(91, 20)

        self.first_last_address = QLineEdit()
        self.first_last_address.setReadOnly(True)
        self.first_last_address_label = QLabel("Last address")
        self.first_last_address_label.setFixedWidth(91)

        self.first_broadcast = QLineEdit()
        self.first_broadcast.setReadOnly(True)
        self.first_broadcast_label = QLabel("Broadcast")
        self.first_broadcast_label.setFixedSize(91, 20)

        self.first_max_hosts = QLineEdit()
        self.first_max_hosts.setReadOnly(True)
        self.first_max_hosts_label = QLabel("Max hosts")
        self.first_max_hosts_label.setFixedSize(91, 20)

        self.second_network_label = QLabel("\nSecond network")

        self.second_net_id = QLineEdit()
        self.second_net_id.setReadOnly(True)
        self.second_net_id_label = QLabel("Network id")
        self.second_net_id_label.setFixedSize(91, 20)

        self.second_first_address = QLineEdit()
        self.second_first_address.setReadOnly(True)
        self.second_first_address_label = QLabel("First address")
        self.second_first_address_label.setFixedSize(91, 20)

        self.second_last_address = QLineEdit()
        self.second_last_address.setReadOnly(True)
        self.second_last_address_label = QLabel("Last address")
        self.second_last_address_label.setFixedWidth(91)

        self.second_broadcast = QLineEdit()
        self.second_broadcast.setReadOnly(True)
        self.second_broadcast_label = QLabel("Broadcast")
        self.second_broadcast_label.setFixedSize(91, 20)

        self.second_max_hosts = QLineEdit()
        self.second_max_hosts.setReadOnly(True)
        self.second_max_hosts_label = QLabel("Max hosts")
        self.second_max_hosts_label.setFixedSize(91, 20)

        h1 = QHBoxLayout()
        h1.addWidget(self.ip_label)
        h1.addWidget(self.net_mask_label)

        h2 = QHBoxLayout()
        h2.addWidget(self.ip_input)
        h2.addWidget(self.net_mask_output)

        h3 = QHBoxLayout()
        h3.addWidget(self.first_net_id_label)
        h3.addWidget(self.first_net_id)

        h4 = QHBoxLayout()
        h4.addWidget(self.first_first_address_label)
        h4.addWidget(self.first_first_address)

        h5 = QHBoxLayout()
        h5.addWidget(self.first_last_address_label)
        h5.addWidget(self.first_last_address)

        h6 = QHBoxLayout()
        h6.addWidget(self.first_broadcast_label)
        h6.addWidget(self.first_broadcast)

        h7 = QHBoxLayout()
        h7.addWidget(self.first_max_hosts_label)
        h7.addWidget(self.first_max_hosts)

        h8 = QHBoxLayout()
        h8.addWidget(self.second_net_id_label)
        h8.addWidget(self.second_net_id)

        h9 = QHBoxLayout()
        h9.addWidget(self.second_first_address_label)
        h9.addWidget(self.second_first_address)

        h10 = QHBoxLayout()
        h10.addWidget(self.second_last_address_label)
        h10.addWidget(self.second_last_address)

        h11 = QHBoxLayout()
        h11.addWidget(self.second_broadcast_label)
        h11.addWidget(self.second_broadcast)

        h12 = QHBoxLayout()
        h12.addWidget(self.second_max_hosts_label)
        h12.addWidget(self.second_max_hosts)

        hh = QHBoxLayout()
        hh.addStretch()
        hh.addWidget(self.first_network_label)
        hh.addStretch()

        hh3 = QHBoxLayout()
        hh3.addStretch()
        hh3.addWidget(self.second_network_label)
        hh3.addStretch()

        hh2 = QHBoxLayout()
        hh2.addStretch()
        hh2.addWidget(self.title)
        hh2.addStretch()

        self.mask_size.setText(str(self.slider.value()))
        self.update_mask()
        hh4 = QHBoxLayout()
        hh4.addWidget(self.mask_size_label)
        hh4.addWidget(self.mask_size)

        hh5 = QHBoxLayout()
        hh5.addWidget(self.split_btn)
        hh5.addWidget(self.clear_btn)

        v = QVBoxLayout()
        v.addLayout(hh2)
        v.addLayout(h1)
        v.addLayout(h2)
        v.addWidget(self.slider)
        v.addLayout(hh4)
        v.addLayout(hh5)
        v.addSpacing(10)
        v.addLayout(hh)
        v.addLayout(h3)
        v.addLayout(h4)
        v.addLayout(h5)
        v.addLayout(h6)
        v.addLayout(h7)
        v.addLayout(hh3)
        v.addLayout(h8)
        v.addLayout(h9)
        v.addLayout(h10)
        v.addLayout(h11)
        v.addLayout(h12)

        self.setLayout(v)
        self.setStyleSheet("font: 12pt Times New Roman")
        self.setFixedWidth(400)

        self.slider.valueChanged.connect(self.update_mask)
        self.split_btn.clicked.connect(self.split_network)
        self.clear_btn.clicked.connect(self.clear_all)

    def update_mask(self):
        ones = self.slider.value()
        mask = make_net_mask(ones)
        self.net_mask_output.setText(str(mask))
        self.mask_size.setText(str(ones))

    def split_network(self):
        if self.check_if_all_is_valid():
            ones = self.slider.value()
            parameters1, parameters2 = split_address(self.ip_input.text(), ones)

            self.first_net_id.setText(parameters1[0] + "/" + str(ones + 1))
            self.first_first_address.setText(parameters1[1])
            self.first_last_address.setText(parameters1[2])
            self.first_broadcast.setText(parameters1[3])
            self.first_max_hosts.setText(str(parameters1[4]))

            self.second_net_id.setText(parameters2[0] + "/" + str(ones + 1))
            self.second_first_address.setText(parameters2[1])
            self.second_last_address.setText(parameters2[2])
            self.second_broadcast.setText(parameters2[3])
            self.second_max_hosts.setText(str(parameters2[4]))

    def clear_all(self):
        self.ip_input.clear()
        self.first_net_id.clear()
        self.first_first_address.clear()
        self.first_last_address.clear()
        self.first_broadcast.clear()
        self.first_max_hosts.clear()

        self.second_net_id.clear()
        self.second_first_address.clear()
        self.second_last_address.clear()
        self.second_broadcast.clear()
        self.second_max_hosts.clear()

        self.slider.setValue(24)
        self.net_mask_output.setText("255.255.255.0")

    def check_if_all_is_valid(self):
        text = self.ip_input.text()
        if text == "":
            QMessageBox.about(self, "Warning!", "Ip address field cannot be left empty!")
            return False
        list = text.split(".")
        for elem in list:
            if len(list) != 4:
                QMessageBox.about(self, "Warning!", "Ip address contains four parts!")
                return False
            if not elem.isdigit():
                QMessageBox.about(self, "Warning!", "Ip address contains only numbers!")
                return False
            if int(elem) > 255:
                QMessageBox.about(self, "Warning!", "Each part of an ip address must be lower than 256!")
                return False
        return True
