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
        times = PT.times

        # Imsak labels
        labelImsak = QLabel("Imsak:")
        labelImsakTime = QLabel(times['imsak'])

        # Horizontal layout holding imsak labels
        layoutLabelImsak = QHBoxLayout()
        layoutLabelImsak.addWidget(labelImsak)
        # layoutLabelImsak.addStretch(1);
        layoutLabelImsak.addWidget(labelImsakTime)

        # Fajr labels
        labelFajr = QLabel("Fajr:")
        labelFajrTime = QLabel(times['fajr'])

        # Horizontal layout holding fajr labels
        layoutLabelFajr = QHBoxLayout()
        layoutLabelFajr.addWidget(labelFajr)
        layoutLabelFajr.addWidget(labelFajrTime)

        # Sunrise labels
        labelSunrise = QLabel("Sunrise:")
        labelSunriseTime = QLabel(times["sunrise"])

        # Horizontal layout holding sunrise labels
        layoutLabelSunrise = QHBoxLayout()
        layoutLabelSunrise.addWidget(labelSunrise)
        layoutLabelSunrise.addWidget(labelSunriseTime)

        # Dhuhr labels
        labelDhuhr = QLabel("Dhuhr:")
        labelDhuhrTime = QLabel(times["dhuhr"])

        # Horizontal layout holding dhuhr labels
        layoutLabelDhuhr = QHBoxLayout()
        layoutLabelDhuhr.addWidget(labelDhuhr)
        layoutLabelDhuhr.addWidget(labelDhuhrTime)

        # Asr labels
        labelAsr = QLabel("Asr:")
        labelAsrTime = QLabel(times["asr"])

        # Horizontal layout holding asr labels
        layoutLabelAsr = QHBoxLayout()
        layoutLabelAsr.addWidget(labelAsr)
        layoutLabelAsr.addWidget(labelAsrTime)

        # maghrib labels
        labelMaghrib = QLabel("Maghrib:")
        labelMaghribTime = QLabel(times["maghrib"])

        # Horizontal layout holding maghrib labels
        layoutLabelMaghrib = QHBoxLayout()
        layoutLabelMaghrib.addWidget(labelMaghrib)
        layoutLabelMaghrib.addWidget(labelMaghribTime)

        # Isha labels
        labelIsha = QLabel("Isha:")
        labelIshaTime = QLabel(times["isha"])

        # Horizontal layout holding maghrib labels
        layoutLabelIsha = QHBoxLayout()
        layoutLabelIsha.addWidget(labelIsha)
        layoutLabelIsha.addWidget(labelIshaTime)

        # Current Prayer Label
        labelCurrentPrayer = QLabel("Current Prayer:")
        labelCurrentPrayer.setStyleSheet("font-weight: bold")
        labelCurrentPrayerTime = QLabel("")
        labelCurrentPrayerTime.setStyleSheet("color: green; font-weight: bold")
        layoutCurrentPrayer = QHBoxLayout()


        # Layout for CurrentPrayer labels
        layoutCurentPrayer = QHBoxLayout
        layoutCurrentPrayer.addWidget(labelCurrentPrayer)
        layoutCurrentPrayer.addWidget(labelCurrentPrayerTime)
        
        # Next Prayer Label
        labelNextPrayer = QLabel("Next Prayer:")
        labelNextPrayer.setStyleSheet("font: bold")
        labelNextPrayerTime = QLabel("")
        labelNextPrayerTime.setStyleSheet("color: #a100ff; font: bold")
        layoutNextPrayer = QHBoxLayout()

        # Layout for Next Prayer labels
        layoutNextPrayer.addWidget(labelNextPrayer)
        layoutNextPrayer.addWidget(labelNextPrayerTime)

        # Prayer times layout
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

        # Reading the config File 

    

        player = QMediaPlayer(self)
        def playAdhan():
            config = ConfigParser()
            config.read('config.ini')
            adhanconfig = str(config["Settings"]["Adhan"])
            try:
                if(adhanconfig == "True"):
                    url = QUrl.fromLocalFile("adhan.wav")
                    adhan = QMediaContent(url)
                    player.setMedia(adhan)
                    try:
                      player.setVolume(int(config["Settings"]["Vol"]))
                    except KeyError:
                        pass
                    player.play()
                else:
                    pass
            except KeyError:
                pass

        # Tray icon 
        icon = QIcon(":icon.png")
        self.setWindowIcon(icon)
        tray = QSystemTrayIcon(self)
        tray.setIcon(icon)
        # tray.setVisible(True)

        # Tray Menu

        about = AboutDialog(self)
        settingsWindow = SettingsWindow(self)

        def hide():
            self.hide()
            settingsWindow.hide()
            about.hide()

        def show():
            self.show()

        def stopAdhan():
            player.stop()

        trayMenu = QMenu()
        showAction = QAction(QIcon(":eye.png"),"Show main window", self)
        hideAction = QAction(QIcon(":eye-close.png"), "Hide main window", self)
        stopAdhanTrayAction = QAction(QIcon(":control-stop-square.png"), "Stop Adhan", self)
        exitAction = QAction(QIcon(":door-open-out.png"), "Exit", self)

        trayMenu.addAction(showAction)
        trayMenu.addAction(hideAction)
        trayMenu.addAction(stopAdhanTrayAction)
        trayMenu.addAction(exitAction)

        showAction.triggered.connect(show)
        hideAction.triggered.connect(hide)
        exitAction.triggered.connect(qApp.quit)
        stopAdhanTrayAction.triggered.connect(stopAdhan)

        tray.setContextMenu(trayMenu)
        tray.setVisible(True)
        
        # Menu 

        def quit():
            message = QMessageBox.question(self, "Quit ?", 
            "do you want to quit ?", QMessageBox.No | QMessageBox.Yes, QMessageBox.No)
            if (message == QMessageBox.Yes):
                qApp.quit()
                sys.exit()

        def showSettings():
            settingsWindow.exec()
        

        def showAbout():
            about.exec()



        quitAction = QAction(QIcon(":door-open-out.png"), "&Quit", self)
        quitAction.setShortcut("Ctrl+Q")
        quitAction.setToolTip("Quit the appplication")
        quitAction.triggered.connect(quit)

        settingsAction = QAction(QIcon(":wrench.png"), "&Settings", self)
        settingsAction.setToolTip("Open settings window")
        settingsAction.setShortcut("Ctrl+S")
        settingsAction.triggered.connect(showSettings)

        stopAdhanAction = QAction(QIcon(":control-stop-square.png"), "S&top Adhan", self)
        settingsAction.setToolTip("Stop adhan")
        stopAdhanAction.setShortcut("Ctrl+T")
        stopAdhanAction.triggered.connect(stopAdhan)

        aboutAction = QAction(QIcon(":information.png"), "&About", self)
        aboutAction.setToolTip("About the application")
        aboutAction.setShortcut("Ctrl+A")
        aboutAction.triggered.connect(showAbout)


        menu = self.menuBar()
        fileMenu = menu.addMenu('&File')
        fileMenu.addAction(quitAction)

        toolsMenu = menu.addMenu("&Tools")
        toolsMenu.addAction(stopAdhanAction)
        toolsMenu.addAction(settingsAction)

        helpMenu = menu.addMenu('&?')
        helpMenu.addAction(aboutAction)


        def splitedTime():
            formatedTime = str(datetime.now().strftime("%H:%M:%S"))
            st = formatedTime.split(":")
        def splitedTime():
            formatedTime = str(datetime.now().strftime("%H:%M:%S"))
            st = splitedTime = formatedTime.split(":")
            return st

        def now():
            formatedTime = str(datetime.now().strftime("%H:%M:%S"))
            return formatedTime




    
       
        threadpool = QThreadPool()
        def timeLoop():
            s = int(splitedTime()[2])
            m = int(splitedTime()[1])
            h = int(splitedTime()[0])
            sDeg = s * 6
            mDeg = m * 6
            hDeg = h * 30 + m / 2


            imsakAdhan   =   str(times["imsak"])   + ":00"
            fajrAdhan    =   str(times["fajr"])    + ":00"
            dhuhrAdhan   =   str(times["dhuhr"])   + ":00"
            asrAdhan     =   str(times["asr"])     + ":00"
            maghribAdhan =   str(times["maghrib"]) + ":00"
            ishaAdhan    =   str(times["isha"])    + ":00"
            config = ConfigParser()
            config.read("config.ini")
            try:
                notifconfig = str(config["Settings"]["Notification"])
            except KeyError:
                notifconfig = "True"

            if(str(now()) == imsakAdhan):
                print(notifconfig)
                try:
                    if(notifconfig == "True"):
                        tray.showMessage("Salat Recall" , "Its time for Imsak !", icon, 5000)
                except KeyError:
                    pass
                playAdhan()

            if(str(now()) == fajrAdhan):
                try:
                    if(notifconfig == "True"):
                        tray.showMessage("Salat Recall" , "Its time for Fajr prayer !", icon, 5000)
                except KeyError:
                    pass
                playAdhan()

            if(str(now()) == dhuhrAdhan):
                try:
                    if(notifconfig == "True"):
                        tray.showMessage("Salat Recall" , "Its time for Dhuhr prayer !", icon, 5000)
                except KeyError:
                    pass
                playAdhan()

            if(str(now()) == asrAdhan):
                try:
                    if(notifconfig == "True"):
                        tray.showMessage("Salat Recall" , "Its time for Asr prayer !", icon, 5000)
                except KeyError:
                    pass

                playAdhan()

            if(str(now()) == maghribAdhan):
                try:
                    if(notifconfig == "True"):
                        tray.showMessage("Salat Recall" , "Its time for Maghrib prayer !", icon, 5000)
                except KeyError:
                    pass
                playAdhan()

            if(str(now()) == ishaAdhan):
                try:
                    if(notifconfig == "True"):
                        tray.showMessage("Salat Recall" , "Its time for Isha prayer !", icon, 5000)
                except KeyError:
                    pass
                playAdhan()

            # Displaying Current Prayer
            if(str(now()) >= imsakAdhan):
                labelCurrentPrayerTime.setText("Imsak")
                labelNextPrayerTime.setText("Fajr")

            if(str(now()) >= fajrAdhan):
                labelCurrentPrayerTime.setText("Fajr")
                labelNextPrayerTime.setText("Dhuhr")

            if(str(now()) >= dhuhrAdhan):
                labelCurrentPrayerTime.setText("Dhuhr")
                labelNextPrayerTime.setText("Asr")

            if(str(now()) >= asrAdhan):
                labelCurrentPrayerTime.setText("Asr")
                labelNextPrayerTime.setText("Maghrib")
                
            if(str(now()) >= maghribAdhan):
                labelCurrentPrayerTime.setText("Maghrib")
                labelNextPrayerTime.setText("Isha")

            if(str(now()) >= ishaAdhan or str(now()) < fajrAdhan):
                labelCurrentPrayerTime.setText("Isha")
                labelNextPrayerTime.setText("Fajr")

        def threadedLoop():
            worker = Worker(timeLoop)
            threadpool.start(worker)




        timer = QTimer(self)
        timer.timeout.connect(threadedLoop)

        timer.start(1000)
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