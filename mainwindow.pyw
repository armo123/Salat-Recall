#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from clockwidget import ClockWidget
# import configparser
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout,\
        QHBoxLayout, QGridLayout, QWidget, QGroupBox, QSystemTrayIcon, QMenu,\
        QAction, qApp, QCalendarWidget, QAction, QGridLayout, QGridLayout,\
        QMessageBox 
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTimer, QUrl, QTimer, QThreadPool
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QSound
from worker import Worker
from settingswindow import SettingsWindow
from getprayertimes import GetPrayerTimes
from datetime import datetime
from aboutwindow import AboutDialog
import ressources 
from PyQt5 import QtCore
from configparser import ConfigParser



class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)
        


        PT = GetPrayerTimes()
        self.times = PT.times

        # Imsak labels
        labelImsak = QLabel("Imsak:")
        labelImsakTime = QLabel(self.times['imsak'])

        # Horizontal layout holding imsak labels
        layoutLabelImsak = QHBoxLayout()
        layoutLabelImsak.addWidget(labelImsak)
        # layoutLabelImsak.addStretch(1);
        layoutLabelImsak.addWidget(labelImsakTime)

        # Fajr label
        labelFajr = QLabel("Fajr:")
        labelFajrTime = QLabel(self.times['fajr'])

        # Horizontal layout holding fajr labels
        layoutLabelFajr = QHBoxLayout()
        layoutLabelFajr.addWidget(labelFajr)
        layoutLabelFajr.addWidget(labelFajrTime)

        # Sunrise label
        labelSunrise = QLabel("Sunrise:")
        labelSunriseTime = QLabel(self.times["sunrise"])

        # Horizontal layout holding sunrise labels
        layoutLabelSunrise = QHBoxLayout()
        layoutLabelSunrise.addWidget(labelSunrise)
        layoutLabelSunrise.addWidget(labelSunriseTime)

        # Dhuhr labels
        labelDhuhr = QLabel("Dhuhr:")
        labelDhuhrTime = QLabel(self.times["dhuhr"])

        # Horizontal layout holding dhuhr labels
        layoutLabelDhuhr = QHBoxLayout()
        layoutLabelDhuhr.addWidget(labelDhuhr)
        layoutLabelDhuhr.addWidget(labelDhuhrTime)

        # Asr labels
        labelAsr = QLabel("Asr:")
        labelAsrTime = QLabel(self.times["asr"])

        # Horizontal layout holding asr labels
        layoutLabelAsr = QHBoxLayout()
        layoutLabelAsr.addWidget(labelAsr)
        layoutLabelAsr.addWidget(labelAsrTime)

        # maghrib labels
        labelMaghrib = QLabel("Maghrib:")
        labelMaghribTime = QLabel(self.times["maghrib"])

        # Horizontal layout holding maghrib labels
        layoutLabelMaghrib = QHBoxLayout()
        layoutLabelMaghrib.addWidget(labelMaghrib)
        layoutLabelMaghrib.addWidget(labelMaghribTime)

        # Isha labels
        labelIsha = QLabel("Isha:")
        labelIshaTime = QLabel(self.times["isha"])

        # Horizontal layout holding maghrib labels
        layoutLabelIsha = QHBoxLayout()
        layoutLabelIsha.addWidget(labelIsha)
        layoutLabelIsha.addWidget(labelIshaTime)

        # Current Prayer Label
        self.labelCurrentPrayer = QLabel("Current Prayer:")
        self.labelCurrentPrayer.setStyleSheet("font-weight: bold")
        self.labelCurrentPrayerTime = QLabel("")
        self.labelCurrentPrayerTime.setStyleSheet("color: green; font-weight: bold")
        layoutCurrentPrayer = QHBoxLayout()


        # Layout for CurrentPrayer labels
        layoutCurentPrayer = QHBoxLayout
        layoutCurrentPrayer.addWidget(self.labelCurrentPrayer)
        layoutCurrentPrayer.addWidget(self.labelCurrentPrayerTime)
        
        # Next Prayer Label
        self.labelNextPrayer = QLabel("Next Prayer:")
        self.labelNextPrayer.setStyleSheet("font: bold")
        self.labelNextPrayerTime = QLabel("")
        self.labelNextPrayerTime.setStyleSheet("color: #a100ff; font: bold")
        layoutNextPrayer = QHBoxLayout()

        # Layout for Next Prayer labels
        layoutNextPrayer.addWidget(self.labelNextPrayer)
        layoutNextPrayer.addWidget(self.labelNextPrayerTime)

        # Prayer self.times layout
        prayerTimesLayout = QVBoxLayout()
        prayerTimesLayout.addLayout(layoutLabelImsak)
        prayerTimesLayout.addLayout(layoutLabelFajr)
        prayerTimesLayout.addLayout(layoutLabelSunrise)
        prayerTimesLayout.addLayout(layoutLabelDhuhr)
        prayerTimesLayout.addLayout(layoutLabelAsr)
        prayerTimesLayout.addLayout(layoutLabelMaghrib)
        prayerTimesLayout.addLayout(layoutLabelIsha)
        prayerTimesLayout.addStretch(1)
        prayerTimesLayout.addLayout(layoutCurrentPrayer)
        prayerTimesLayout.addLayout(layoutNextPrayer)

        prayerTimesGroup = QGroupBox()
        prayerTimesGroup.setTitle("Today prayers time:")
        prayerTimesGroup.size
        prayerTimesGroup.setLayout(prayerTimesLayout)

        self.setStyleSheet('QGroupBox{'
                           'font: bold;}')
        self.setFixedSize(420, 280)
        self.setWindowTitle("Salat Recall")

        # Clock Widget
        clockGroup = QGroupBox()
        clockGroup.setTitle("Clock / Next Prayer:")
        clockLayout = QVBoxLayout()
        clock = ClockWidget()
        clockLayout.addWidget(clock)
        clockGroup.setLayout(clockLayout)



        # Main layout the containtainer of all layouts
        mainLayout = QGridLayout()
        mainLayout.addWidget(prayerTimesGroup, 1, 1)
        mainLayout.addWidget(clockGroup, 1, 2)
        mainWidget = QWidget()
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)

        self.player = QMediaPlayer(self)
        self.settingsWindow = SettingsWindow()
        self.aboutWindow = AboutDialog()




        # Tray icon 
        self.icon = QIcon(":icon.png")
        self.setWindowIcon(self.icon)
        self.tray = QSystemTrayIcon(self)
        self.tray.setIcon(self.icon)        # Tray icon 
        # tray.setVisible(True)

        # Tray Menu
        trayMenu = QMenu()
        showAction = QAction(QIcon(":eye.png"),"Show main window", self)
        hideAction = QAction(QIcon(":eye-close.png"), "Hide main window", self)
        stopAdhanTrayAction = QAction(QIcon(":control-stop-square.png"), "Stop Adhan", self)
        exitAction = QAction(QIcon(":door-open-out.png"), "Exit", self)

        trayMenu.addAction(showAction)
        trayMenu.addAction(hideAction)
        trayMenu.addAction(stopAdhanTrayAction)
        trayMenu.addAction(exitAction)

        showAction.triggered.connect(self.show)
        hideAction.triggered.connect(self.hideWindows)
        exitAction.triggered.connect(qApp.quit)
        stopAdhanTrayAction.triggered.connect(self.stopAdhan)

        self.tray.setContextMenu(trayMenu)
        self.tray.setVisible(True)
        
        # Menu 
        quitAction = QAction(QIcon(":door-open-out.png"), "&Quit", self)
        quitAction.setShortcut("Ctrl+Q")
        quitAction.setToolTip("Quit the application")
        quitAction.triggered.connect(self.quit)

        settingsAction = QAction(QIcon(":wrench.png"), "&Settings", self)
        settingsAction.setToolTip("Open settings window")
        settingsAction.setShortcut("Ctrl+S")
        settingsAction.triggered.connect(self.showSettings)

        stopAdhanAction = QAction(QIcon(":control-stop-square.png"), "S&top Adhan", self)
        settingsAction.setToolTip("Stop adhan")
        stopAdhanAction.setShortcut("Ctrl+T")
        stopAdhanAction.triggered.connect(self.stopAdhan)

        aboutAction = QAction(QIcon(":information.png"), "&About", self)
        aboutAction.setToolTip("About the application")
        aboutAction.setShortcut("Ctrl+A")
        aboutAction.triggered.connect(self.showAbout)


        menu = self.menuBar()
        fileMenu = menu.addMenu('&File')
        fileMenu.addAction(quitAction)

        toolsMenu = menu.addMenu("&Tools")
        toolsMenu.addAction(stopAdhanAction)
        toolsMenu.addAction(settingsAction)

        helpMenu = menu.addMenu('&?')
        helpMenu.addAction(aboutAction)
        timer = QTimer(self)
        timer.timeout.connect(self.timeLoop)
        timer.start(1000)


    def showSettings(self):
        self.settingsWindow.exec()
    

    def showAbout(self):
        self.aboutWindow.exec()

    def hideWindows(self):
        self.hide()
        self.settingsWindow.hide()
        self.about.hide()


    def splitedTime():
        formatedTime = str(datetime.now().strftime("%H:%M:%S"))
        st = splitedTime = formatedTime.split(":")
        return st

    def now(self):
        formatedTime = str(datetime.now().strftime("%H:%M:%S"))
        return formatedTime

   
    def threadedLoop(self):
        threadpool = QThreadPool(self)
        worker = Worker(self.timeLoop)
        threadpool.start(worker)

    def showTrayMessage(self, message):

        self.tray.showMessage("Salat Recall" , "Its time for " + message + " prayer !", self.icon, 5000)

    def playAdhan(self):
        config = ConfigParser()
        config.read('config.ini')
        adhanconfig = str(config["Settings"]["Adhan"])
        try:
            if(adhanconfig == "True"):
                url = QUrl.fromLocalFile("adhan.wav")
                adhan = QMediaContent(url)
                self.player.setMedia(adhan)
                try:
                    self.player.setVolume(int(config["Settings"]["Vol"]))
                except KeyError:
                    pass
                self.player.play()
            else:
                    pass
        except KeyError:
            pass

    def stopAdhan(self):
        self.player.stop()

    def quit(self):
        message = QMessageBox.question(self, "Quit ?", 
        "do you want to quit ?", QMessageBox.No | QMessageBox.Yes, QMessageBox.No)
        if (message == QMessageBox.Yes):
            qApp.quit()
            sys.exit()
       
    def timeLoop(self):
        imsakAdhan   =   str(self.times["imsak"])   + ":00"
        fajrAdhan    =   str(self.times["fajr"])    + ":00"
        dhuhrAdhan   =   str(self.times["dhuhr"])   + ":00"
        asrAdhan     =   str(self.times["asr"])     + ":00"
        maghribAdhan =   str(self.times["maghrib"]) + ":00"
        ishaAdhan    =   str(self.times["isha"])    + ":00"
        config = ConfigParser()
        config.read("config.ini")



        try:
            notifconfig = str(config["Settings"]["Notification"])
        except KeyError:
            notifconfig = "True"

        if(self.now() == imsakAdhan):
            try:
                if(notifconfig == "True"):
                    self.showTrayMessage("Imsak")
            except KeyError:
                pass
            #self.playAdhan()

        if(str(self.now()) == fajrAdhan):
            try:
                if(notifconfig == "True"):
                    self.showTrayMessage("Fajr")
            except KeyError:
                pass
            #self.playAdhan()

        if(str(self.now()) == dhuhrAdhan):
            try:
                if(notifconfig == "True"):
                    self.showTrayMessage("Dhuhr")
                pass
            except KeyError:
                pass
            self.playAdhan()

        if(str(self.now()) == asrAdhan):
            try:
                if(notifconfig == "True"):
                    self.showTrayMessage("Asr")
            except KeyError:
                pass

            #self.playAdhan()

        if(str(self.now()) == maghribAdhan):
            try:
                if(notifconfig == "True"):
                    self.showTrayMessage("Maghrib")
            except KeyError:
                pass
            #self.playAdhan()

        if(self.now() == ishaAdhan):
            try:
                if(notifconfig == "True"):
                    self.showTrayMessage("Isha")
            except KeyError:
                pass
            #self.playAdhan()

        print("Now:" + self.now())
        # Displaying Current Prayer
        if(str(self.now()) >= imsakAdhan):
            self.labelCurrentPrayerTime.setText("Imsak")
            self.labelNextPrayerTime.setText("Fajr")

        if(str(self.now()) >= fajrAdhan):
            self.labelCurrentPrayerTime.setText("Fajr")
            self.labelNextPrayerTime.setText("Dhuhr")

        if(str(self.now()) >= dhuhrAdhan):
            self.labelCurrentPrayerTime.setText("Dhuhr")
            self.labelNextPrayerTime.setText("Asr")

        if(str(self.now()) >= asrAdhan):
            self.labelCurrentPrayerTime.setText("Asr")
            self.labelNextPrayerTime.setText("Maghrib")
            
        if(str(self.now()) >= maghribAdhan):
            self.labelCurrentPrayerTime.setText("Maghrib")
            self.labelNextPrayerTime.setText("Isha")

        if(str(self.now()) >= ishaAdhan or str(self.now()) < fajrAdhan):
            self.labelCurrentPrayerTime.setText("Isha")
            self.labelNextPrayerTime.setText("Fajr")
        





    def closeEvent(self, event):
        message = QMessageBox.question(self, "Quit ?",
        "the application will no longer stay in the tray area do you want to quit ?",
        QMessageBox.No | QMessageBox.Yes, QMessageBox.No)
        if(message == QMessageBox.Yes):
            qApp.quit()
            sys.exit()
        event.ignore()
        



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.hide()
    # window.show()
    app.exec()

if __name__=='__main__':
    main()