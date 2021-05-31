#!/usr/bin/env python
# -*- coding: utf-8 -*


from PyQt5.QtWidgets import QDialog, QHBoxLayout, QLabel, QVBoxLayout,QApplication
from PyQt5.QtGui import QPixmap, QIcon
import sys
import ressources


class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog,self).__init__(*args, **kwargs)
        labelName = QLabel("Salat Call version 1.0.0")
        labelName.setStyleSheet("text-align: center; font: 15px ")
        appIcon = QPixmap()
        appIcon.load(":aboutIcon")
        labelIcon = QLabel()
        labelIcon.setPixmap(appIcon)
        labelsLayout = QHBoxLayout()
        nameLayout = QHBoxLayout()
        labelInfo = QLabel("""    Author: armo
    Email: armo23@protonmail.com
    License: This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details """)
        labelsLayout.addStretch()
        labelsLayout.addWidget(labelIcon)
        labelsLayout.addStretch()
        nameLayout.addStretch() 
        nameLayout.addWidget(labelName)
        nameLayout.addStretch() 
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(labelsLayout)
        mainLayout.addLayout(nameLayout)
        mainLayout.addWidget(labelInfo)

        self.setLayout(mainLayout)
        self.setWindowIcon(QIcon(":information"))
        self.setFixedSize(420,300)
