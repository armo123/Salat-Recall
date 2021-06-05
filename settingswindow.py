#!/usr/bin/env python
# -*- coding: utf-8 -*-



import configparser
import sys
from PyQt5.QtGui import QIcon, QRegExpValidator
from PyQt5.QtWidgets import QAction, QApplication, QDialog, QGroupBox, QHBoxLayout, QMessageBox, QPushButton,\
     QVBoxLayout, QLabel, QLineEdit, QWidget, QComboBox, QCheckBox, QSlider
from PyQt5.QtCore import QLine, QRegExp , Qt
from PyQt5.QtGui import QRegExpValidator, QIcon
from configparser import ConfigParser


    

class SettingsWindow(QDialog):
    def __init__(self, *args, **kwargs):
        super(SettingsWindow, self).__init__(*args, **kwargs)
        # Reding config file to file the text filds
        self.config = ConfigParser()
        self.config.read("config.ini")
        self.state = False
        self.change = False
    
   

        # Creating widgets 

        self.labelLatitude = QLabel("Latitude:")
        self.latitude = QLineEdit()
        self.latitude.setFixedWidth(50)
        self.latitude.setMaxLength(7)
        rx = QRegExp("\-{0,1}[0-9]{0,2}\.[0-9]{2}")
        self.latitude.setValidator(QRegExpValidator(rx))

        try:
            self.configlatitude = self.config["Settings"]["Latitude"]
            self.latitude.setText(self.configlatitude)
        except KeyError :
            self.latitude.setText("00.00")

        layoutLatitude = QHBoxLayout()
        layoutLatitude.addWidget(self.labelLatitude)
        layoutLatitude.addStretch()
        layoutLatitude.addWidget(self.latitude)
        self.longitudeLabel = QLabel("Longitude")
        self.longitude = QLineEdit()
        self.longitude.setFixedWidth(50)
        self.longitude.setMaxLength(7)
        self.longitude.setValidator(QRegExpValidator(rx))

        try:
            configlongitude = self.config["Settings"]["Longitude"]
            self.longitude.setText(configlongitude)
        except KeyError:
            self.longitude.setText("00.00")

        layoutlongitude  = QHBoxLayout()
        layoutlongitude.addWidget(self.longitudeLabel)
        layoutlongitude.addStretch()
        layoutlongitude.addWidget(self.longitude)
        loactionLayout = QVBoxLayout()
        loactionLayout.addLayout(layoutLatitude)
        loactionLayout.addLayout(layoutlongitude)

        self.labelTuneImsak = QLabel("Imsak:")
        self.imsak = QLineEdit()
        self.imsak.setMaxLength(6)
        self.imsak.setMaximumWidth(50)
        rxHours = QRegExp("\-{0,1}[0-9]{0,1}[0-9]{0,1}[0-9]{0,1}\.[0-9]{0,2}")
        self.imsak.setValidator(QRegExpValidator(rxHours))

        try:
            self.configimsak = self.config["Settings"]["Imsak"]
            self.imsak.setText(self.configimsak)
        except KeyError:
            self.imsak.setText("00.00")

        layoutImsak = QHBoxLayout()
        layoutImsak.addWidget(self.labelTuneImsak)
        layoutImsak.addStretch()
        layoutImsak.addWidget(self.imsak)
        self.labelTuneFajr = QLabel("Fajr:")
        self.fajr = QLineEdit()
        self.fajr.setMaxLength(6)
        self.fajr.setMaximumWidth(50)
        self.fajr.setValidator(QRegExpValidator(rxHours))
        try:
            fajrconfig = self.config["Settings"]["Fajr"]
            self.fajr.setText(fajrconfig)
        except KeyError:
            self.fajr.setText("00.00")
        fajrLayout = QHBoxLayout()
        fajrLayout.addWidget(self.labelTuneFajr)
        fajrLayout.addWidget(self.fajr)
        self.dhuhrTuneLabel = QLabel("Dhuhr:")
        self.dhuhr = QLineEdit()
        self.dhuhr.setMaxLength(6)
        self.dhuhr.setMaximumWidth(50)
        self.dhuhr.setValidator(QRegExpValidator(rxHours))
        try:
            dhuhrconfig = self.config["Settings"]["Dhuhr"]
            self.dhuhr.setText(dhuhrconfig)
        except KeyError:
            self.dhuhr.setText("00.00")
        layoutDhuhr = QHBoxLayout()
        layoutDhuhr.addWidget(self.dhuhrTuneLabel)
        layoutDhuhr.addWidget(self.dhuhr)
        labelTuneAsr = QLabel("Asr")
        self.asr = QLineEdit()
        self.asr.setMaxLength(6)
        self.asr.setMaximumWidth(50)
        self.asr.setValidator(QRegExpValidator(rxHours))

        try:
            asrconfig = self.config["Settings"]["Asr"]
            self.asr.setText(asrconfig)
        except KeyError:

            self.asr.setText("00.00")
        layoutAsr = QHBoxLayout()
        layoutAsr.addWidget(labelTuneAsr)
        layoutAsr.addWidget(self.asr)
        self.labelTuneMaghrib = QLabel("Maghrib:")
        self.maghrib = QLineEdit()
        self.maghrib.setMaxLength(6)
        self.maghrib.setMaximumWidth(50)
        self.maghrib.setValidator(QRegExpValidator(rxHours))

        try:
            configmaghrib = self.config["Settings"]["Maghrib"]
            self.maghrib.setText(configmaghrib)
        except KeyError:
            self.maghrib.setText("00.00")

        maghribLayout = QHBoxLayout()
        maghribLayout.addWidget(self.labelTuneMaghrib)
        maghribLayout.addWidget(self.maghrib)
        self.labelTuneIsha = QLabel("Isha:")
        self.isha = QLineEdit()
        self.isha.setMaxLength(6)
        self.isha.setMaximumWidth(50)
        self.isha.setValidator(QRegExpValidator(rxHours))
        try:
            configisha = self.config["Settings"]["Isha"]
            self.isha.setText(configisha)
        except KeyError:
            self.isha.setText("00.00")
        layoutIsha = QHBoxLayout()
        layoutIsha.addWidget(self.labelTuneIsha)
        layoutIsha.addWidget(self.isha)


        tunningLayout = QVBoxLayout()
        tunningLayout.addLayout(layoutImsak)
        tunningLayout.addLayout(fajrLayout)
        tunningLayout.addLayout(layoutDhuhr)
        tunningLayout.addLayout(layoutAsr)
        tunningLayout.addLayout(maghribLayout)
        tunningLayout.addLayout(layoutIsha)
        
        self.adhanLabel = QLabel("No adhan")
        self.adhan = QCheckBox()
        try:
            checked = self.config["Settings"]["Adhan"]
        except:
            checked = "False"

        if(checked == "False"):
            self.adhan.setChecked(True)
        else:
            self.adhan.setChecked(False)
        
        self.notifLabel = QLabel("No notifications")
        self.notification = QCheckBox()
        try:
            checkedNotif = self.config["Settings"]["Notification"]
        except KeyError:
            checkedNotif = "False"

        if(checkedNotif == "False"):
            self.notification.setChecked(True)
        else:
            self.notification.setChecked(False)

        notifLayout = QHBoxLayout()
        notifLayout.addWidget(self.notifLabel)
        notifLayout.addWidget(self.notification)

        layoutAdhan = QHBoxLayout()
        layoutAdhan.addWidget(self.adhanLabel)
        layoutAdhan.addStretch
        layoutAdhan.addWidget(self.adhan)
        layoutGroupAdhan = QVBoxLayout()

        self.volumeAdhan = QSlider(Qt.Horizontal)
        try:
            vol = self.config["Settings"]["Vol"]
        except KeyError:
            vol = "50"
        self.volumeAdhan.setValue(int(vol))
        volumeLayout = QHBoxLayout()
        volumeLayout.addWidget(self.volumeAdhan)
        self.labelVol = QLabel()
        self.labelVol.setText("Volume:" + str(self.volumeAdhan.value()))
        layoutLabelVol = QHBoxLayout()
        layoutLabelVol.addWidget(self.labelVol)
        layoutGroupAdhan.addLayout(layoutAdhan)
        layoutGroupAdhan.addLayout(notifLayout)
        layoutGroupAdhan.addLayout(volumeLayout)
        layoutGroupAdhan.addLayout(layoutLabelVol)


        groupeAdhan = QGroupBox("Adhan:")
        groupeAdhan.setLayout(layoutGroupAdhan)
    


        
        self.saveButton = QPushButton(QIcon(":disk.png"), "Save")
        layoutSave = QHBoxLayout()
        layoutSave.addStretch()
        layoutSave.addWidget(self.saveButton)
        
        locationGroup = QGroupBox("Location:")
        locationGroup.setLayout(loactionLayout)
        tuneGroup = QGroupBox("Prayers time Tunning:")
        tuneGroup.setLayout(tunningLayout)


        self.methodList = QComboBox()
        methods = ["MWL", "ISNA", "Egypt", "Makkah", "Karachi", "Tehran", "Jafari"]
        self.methodList.addItems(methods)

        try: 
            configmethod = self.config["Settings"]["Method"]
            for i in range(len(methods)):
                if (methods[i] == configmethod):
                    self.methodList.setCurrentIndex(i)
        except KeyError:
            pass


        methodLayout = QVBoxLayout()
        methodLayout.addWidget(self.methodList)
        methodsGroup = QGroupBox("Calculation Method:")
        methodsGroup.setLayout(methodLayout)

        settingsLayout = QVBoxLayout()
        settingsLayout.addWidget(locationGroup)
        settingsLayout.addWidget(tuneGroup)
        settingsLayout.addWidget(methodsGroup)
        settingsLayout.addWidget(groupeAdhan)
        settingsLayout.addStretch()
        settingsLayout.addLayout(layoutSave)
        self.setLayout(settingsLayout)
        self.setWindowIcon(QIcon(":wrench.png"))
        self.setWindowTitle("Settings")
        self.setFixedSize(220, 480)
        self.setStyleSheet("QGroupBox{font: bold;}")

        # Saving settings in ini file

        self.latitude.textChanged[str].connect(self.changed)
        self.longitude.textChanged[str].connect(self.changed)
        self.imsak.textChanged[str].connect(self.changed)
        self.fajr.textChanged[str].connect(self.changed)
        self.dhuhr.textChanged[str].connect(self.changed)
        self.asr.textChanged[str].connect(self.changed)
        self.maghrib.textChanged[str].connect(self.changed)
        self.isha.textChanged[str].connect(self.changed)
        self.methodList.currentTextChanged[str].connect(self.changed)
        self.volumeAdhan.valueChanged.connect(self.volumeChanged)
        self.adhan.stateChanged.connect(self.stateCh)
        self.notification.stateChanged.connect(self.stateCh)
        self.saveButton.clicked.connect(self.saveConfig)

    def changed(self):
        self.change = True

    def volumeChanged(self):
        self.labelVol.setText("Volume:" + str(self.volumeAdhan.value()))
        self.state = True

    def stateCh(self):
        self.state = True

    def saveConfig(self):
        if(len(self.latitude.text()) > 0):
            latitudeValue = self.latitude.text()
        else:
            self.latitude.setText("00.00")
            latitudeValue = "00.00"

        if(len(self.longitude.text()) > 0):
            longitudeValue = self.longitude.text()
        else:
            self.longitude.setText("00.00")
            longitudeValue = "00.00"
        
        if(len(self.imsak.text()) > 0):
            imsakValue = self.imsak.text()
        else:
            self.imsak.setText("00.00") 
            imsakValue = "00.00"

        if(len(self.fajr.text()) > 0):
            fajrValue = self.fajr.text()
        else:
            self.fajr.setText("00.00")
            fajrValue = "00.00"

        if(len(self.dhuhr.text()) > 0):
            dhuhrValue = self.dhuhr.text()
        else:
            self.dhuhr.setText("00.00")
            dhuhrValue = "00.00"
        
        if(len(self.asr.text()) > 0):
            asrValue = self.asr.text()
        else:
            self.asr.setText("00.00")
            asrValue = "00.00"
        
        if(len(self.maghrib.text())> 0):
            maghribValue = self.maghrib.text()
        else:
            self.maghrib.setText("00.00")
            maghribValue = "00.00"

        if(len(self.isha.text()) > 0):
            ishaValue = self.isha.text()
        else:
            self.isha.setText("00.00")
            ishaValue = "00.00"

        method = self.methodList.currentText()

        if(self.adhan.isChecked() == True):
            noAdhan = "False"
        else:
            noAdhan = "True"

        if(self.notification.isChecked() == True):
            noNotif = "False"
        else:
            noNotif = "True"

        adhanVol = str(self.volumeAdhan.value())  

        self.config["Settings"]={'Latitude':  latitudeValue,
                            'longitude': longitudeValue,
                            'Imsak':     imsakValue,
                            'Fajr':      fajrValue,
                            'Dhuhr':     dhuhrValue,
                            'Asr':       asrValue,
                            'Maghrib':   maghribValue,
                            'Isha':      ishaValue,
                            'Method':    method,
                            'Adhan':     noAdhan,
                            'Vol':       adhanVol,
                            'Notification': noNotif}                 
                        
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)
        if(self.change == True):
            QMessageBox.information(self, "Restart the App", 
            "Please restart the Application")
        self.change = False
        self.state = False
    
        
    def closeEvent(self, event):
        if (self.change == True or self.state == True):
            message =  QMessageBox.question(self, "Quit without saving", 
            "Do you want to quit without saving ?", 
            QMessageBox.Yes| QMessageBox.No, QMessageBox.No)
            if (message == QMessageBox.No):
                event.ignore()
            else:
                self.chang = False
                return
        self.change = False


