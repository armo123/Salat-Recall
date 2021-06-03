#!/usr/bin/env python
# -*- coding: utf-8 -*-



import sys
from PyQt5.QtGui import QIcon, QRegExpValidator
from PyQt5.QtWidgets import QAction, QApplication, QDialog, QGroupBox, QHBoxLayout, QMessageBox, QPushButton,\
     QVBoxLayout, QLabel, QLineEdit, QWidget, QComboBox, QCheckBox, QSlider
from PyQt5.QtCore import QLine, QRegExp , Qt
from PyQt5.QtGui import QRegExpValidator, QIcon
from configparser import ConfigParser


    

class SettingsWindow(QDialog):
    state = False
    changed = False
    def __init__(self, *args, **kwargs):
        super(SettingsWindow, self).__init__(*args, **kwargs)
        # Reding config file to file the text filds
        config = ConfigParser()
        config.read("config.ini")
    

        # Creating widgets 

        labelLatitude = QLabel("Latitude:")
        latitude = QLineEdit()
        latitude.setFixedWidth(50)
        latitude.setMaxLength(7)
        rx = QRegExp("\-{0,1}[0-9]{2,3}\.[0-9]{2}")
        latitude.setValidator(QRegExpValidator(rx))

        try:
            configlatitude = config["Settings"]["Latitude"]
            latitude.setText(configlatitude)
        except KeyError :
            latitude.setText("00.00")

        layoutLatitude = QHBoxLayout()
        layoutLatitude.addWidget(labelLatitude)
        layoutLatitude.addStretch()
        layoutLatitude.addWidget(latitude)
        longitudeLabel = QLabel("Longitude")
        longitude = QLineEdit()
        longitude.setFixedWidth(50)
        longitude.setMaxLength(7)
        longitude.setValidator(QRegExpValidator(rx))

        try:
            configlongitude = config["Settings"]["Longitude"]
            longitude.setText(configlongitude)
        except KeyError:
            longitude.setText("00.00")

        layoutLongitude  = QHBoxLayout()
        layoutLongitude.addWidget(longitudeLabel)
        layoutLongitude.addStretch()
        layoutLongitude.addWidget(longitude)
        loactionLayout = QVBoxLayout()
        loactionLayout.addLayout(layoutLatitude)
        loactionLayout.addLayout(layoutLongitude)

        labelTuneImsak = QLabel("Imsak:")
        imsak = QLineEdit()
        imsak.setMaxLength(6)
        imsak.setMaximumWidth(50)
        rxHours = QRegExp("\-{0,1}[0-2][0-9]{0,1}\.[0-9]{0,2}")
        imsak.setValidator(QRegExpValidator(rxHours))

        try:
            configimsak = config["Settings"]["Imsak"]
            imsak.setText(configimsak)
        except KeyError:
            imsak.setText("00.00")

        layoutImsak = QHBoxLayout()
        layoutImsak.addWidget(labelTuneImsak)
        layoutImsak.addStretch()
        layoutImsak.addWidget(imsak)
        labelTuneFajr = QLabel("Fajr:")
        fajr = QLineEdit()
        fajr.setMaxLength(6)
        fajr.setMaximumWidth(50)
        fajr.setValidator(QRegExpValidator(rxHours))
        try:
            fajrconfig = config["Settings"]["Fajr"]
            fajr.setText(fajrconfig)
        except KeyError:
            fajr.setText("00.00")
        fajrLayout = QHBoxLayout()
        fajrLayout.addWidget(labelTuneFajr)
        fajrLayout.addWidget(fajr)
        dhuhrTuneLabel = QLabel("Dhuhr:")
        dhuhr = QLineEdit()
        dhuhr.setMaxLength(6)
        dhuhr.setMaximumWidth(50)
        dhuhr.setValidator(QRegExpValidator(rxHours))
        try:
            dhuhrconfig = config["Settings"]["Dhuhr"]
            dhuhr.setText(dhuhrconfig)
        except KeyError:
            dhuhr.setText("00.00")
        layoutDhuhr = QHBoxLayout()
        layoutDhuhr.addWidget(dhuhrTuneLabel)
        layoutDhuhr.addWidget(dhuhr)
        labelTuneAsr = QLabel("Asr")
        asr = QLineEdit()
        asr.setMaxLength(6)
        asr.setMaximumWidth(50)
        asr.setValidator(QRegExpValidator(rxHours))

        try:
            asrconfig = config["Settings"]["Asr"]
            asr.setText(asrconfig)
        except KeyError:

            asr.setText("00.00")
        layoutAsr = QHBoxLayout()
        layoutAsr.addWidget(labelTuneAsr)
        layoutAsr.addWidget(asr)
        labelTuneMaghrib = QLabel("Maghrib:")
        maghrib = QLineEdit()
        maghrib.setMaxLength(6)
        maghrib.setMaximumWidth(50)
        maghrib.setValidator(QRegExpValidator(rxHours))

        try:
            configmaghrib = config["Settings"]["Maghrib"]
            maghrib.setText(configmaghrib)
        except KeyError:

            maghrib.setText("00.00")
        maghribLayout = QHBoxLayout()
        maghribLayout.addWidget(labelTuneMaghrib)
        maghribLayout.addWidget(maghrib)
        labelTuneIsha = QLabel("Isha:")
        isha = QLineEdit()
        isha.setMaxLength(6)
        isha.setMaximumWidth(50)
        isha.setValidator(QRegExpValidator(rxHours))
        try:
            configisha = config["Settings"]["Isha"]
            isha.setText(configisha)
        except KeyError:
            isha.setText("00.00")
        layoutIsha = QHBoxLayout()
        layoutIsha.addWidget(labelTuneIsha)
        layoutIsha.addWidget(isha)


        tunningLayout = QVBoxLayout()
        tunningLayout.addLayout(layoutImsak)
        tunningLayout.addLayout(fajrLayout)
        tunningLayout.addLayout(layoutDhuhr)
        tunningLayout.addLayout(layoutAsr)
        tunningLayout.addLayout(maghribLayout)
        tunningLayout.addLayout(layoutIsha)
        
        adhanLabel = QLabel("No adhan")
        adhan = QCheckBox()
        try:
            checked = config["Settings"]["Adhan"]
        except:
            checked = "False"

        if(checked == "False"):
            adhan.setChecked(True)
        else:
            adhan.setChecked(False)
        
        notifLabel = QLabel("No notifications")
        notification = QCheckBox()
        try:
            checkedNotif = config["Settings"]["Notification"]
        except KeyError:
            checkedNotif = "False"

        if(checkedNotif == "False"):
            notification.setChecked(True)
        else:
            notification.setChecked(False)

        notifLayout = QHBoxLayout()
        notifLayout.addWidget(notifLabel)
        notifLayout.addWidget(notification)

        layoutAdhan = QHBoxLayout()
        layoutAdhan.addWidget(adhanLabel)
        layoutAdhan.addStretch
        layoutAdhan.addWidget(adhan)
        layoutGroupAdhan = QVBoxLayout()

        volumeAdhan = QSlider(Qt.Horizontal)
        try:
            vol = config["Settings"]["Vol"]
        except KeyError:
            vol = "50"
        volumeAdhan.setValue(int(vol))
        volumeLayout = QHBoxLayout()
        volumeLayout.addWidget(volumeAdhan)
        labelVol = QLabel()
        labelVol.setText("Volume:" + str(volumeAdhan.value()))
        layoutLabelVol = QHBoxLayout()
        layoutLabelVol.addWidget(labelVol)
        layoutGroupAdhan.addLayout(layoutAdhan)
        layoutGroupAdhan.addLayout(notifLayout)
        layoutGroupAdhan.addLayout(volumeLayout)
        layoutGroupAdhan.addLayout(layoutLabelVol)


        groupeAdhan = QGroupBox("Adhan:")
        groupeAdhan.setLayout(layoutGroupAdhan)
    


        
        saveButton = QPushButton(QIcon("images/disk.png"), "Save")
        layoutSave = QHBoxLayout()
        layoutSave.addStretch()
        layoutSave.addWidget(saveButton)
        
        locationGroup = QGroupBox("Location:")
        locationGroup.setLayout(loactionLayout)
        tuneGroup = QGroupBox("Prayers time Tunning:")
        tuneGroup.setLayout(tunningLayout)


        methodList = QComboBox()
        methods = ["MWL", "ISNA", "Egypt", "Makkah", "Karachi", "Tehran", "Jafari"]
        methodList.addItems(methods)

        try: 
            configmethod = config["Settings"]["Method"]
            for i in range(len(methods)):
                if (methods[i] == configmethod):
                    methodList.setCurrentIndex(i)
        except KeyError:
            pass


        methodLayout = QVBoxLayout()
        methodLayout.addWidget(methodList)
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


        def changed():
            self.changed = True

        def volumeChanged():
            labelVol.setText("Volume:" + str(volumeAdhan.value()))

        def stateCh():
            self.state = True

        


        latitude.textChanged[str].connect(changed)
        longitude.textChanged[str].connect(changed)
        imsak.textChanged[str].connect(changed)
        fajr.textChanged[str].connect(changed)
        dhuhr.textChanged[str].connect(changed)
        asr.textChanged[str].connect(changed)
        maghrib.textChanged[str].connect(changed)
        isha.textChanged[str].connect(changed)
        methodList.currentTextChanged[str].connect(changed)
        volumeAdhan.valueChanged.connect(volumeChanged)
        adhan.stateChanged.connect(stateCh)
        notification.stateChanged.connect(stateCh)

        def saveConfig():
            if(len(latitude.text()) > 0):
                latitudeValue = latitude.text()
            else:
                latitude.setText("00.00")
                latitudeValue = "00.00"

            if(len(longitude.text()) > 0):
                longitudeValue = longitude.text()
            else:
                longitude.setText("00.00")
                longitudeValue = "00.00"
            
            if(len(imsak.text()) > 0):
                imsakValue = imsak.text()
            else:
                imsak.setText("00.00") 
                imsakValue = "00.00"

            if(len(fajr.text()) > 0):
                fajrValue = fajr.text()
            else:
                fajr.setText("00.00")
                fajrValue = "00.00"

            fajrValue  = "00.00"

            if(len(dhuhr.text()) > 0):
                dhuhrValue = dhuhr.text()
            else:
                dhuhr.setText("00.00")
                dhuhrValue = "00.00"
            
            if(len(asr.text()) > 0):
                asrValue = asr.text()
            else:
                asr.setText("00.00")
                asrValue = "00.00"
            
            if(len(maghrib.text())> 0):
                maghribValue = maghrib.text()
            else:
                maghrib.setText("00.00")
                maghribValue = "00.00"

            if(len(isha.text()) > 0):
                ishaValue = isha.text()
            else:
                isha.setText("00.00")
                ishaValue = "00.00"

            method = methodList.currentText()

            if(adhan.isChecked() == True):
                noAdhan = "False"
            else:
                noAdhan = "True"

            if(notification.isChecked() == True):
                noNotif = "False"
            else:
                noNotif = "True"

            adhanVol = str(volumeAdhan.value())  


            config["Settings"]={'Latitude':  latitudeValue,
                                'Longitude': longitudeValue,
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
                config.write(configfile)
            if(self.changed == True):
                QMessageBox.information(self, "Restart the App", 
                "Please restart the Application")
            self.changed = False
            self.state = False
        

        saveButton.clicked.connect(saveConfig)
        
    def closeEvent(self, event):
        if (self.changed == True or self.state == True):
            message =  QMessageBox.question(self, "Quit without saving", 
            "Do you want to quit without saving ?", 
            QMessageBox.Yes| QMessageBox.No, QMessageBox.No)
            if (message == QMessageBox.No):
                event.ignore()
            else:
                self.changed = False
                return
        self.changed = False


