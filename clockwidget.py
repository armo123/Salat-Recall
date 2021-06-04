#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from datetime import datetime
from PyQt5.QtWidgets import QWidget, QLabel, QApplication,\
        QGraphicsScene, QGraphicsView, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QTransform, QPainter
from PyQt5.QtCore import Qt, QPoint, QTimer 
from configparser import ConfigParser
from praytimes import PrayTimes
from getprayertimes import GetPrayerTimes



class ClockWidget(QWidget):
    def __init__(self, *args, **kwargs):

        super(ClockWidget, self).__init__(*args, **kwargs)

        self.pt = GetPrayerTimes()

        # Loading Images
        self.setFixedSize(210, 210)
        imgBg = QPixmap(':clock-bg.png')
        imgHandleHoure = QPixmap(':houres-handle.png')
        imgHandleMin = QPixmap(':minutes-handle.png')
        imgHandleSec = QPixmap(':seconds-handle.png')
        imgSalatHandleHoure = QPixmap(":salatHouresHandle.png")
        imgSalatHandleMin = QPixmap(":salatMinHandle.png")

        # Converting resouces into QGraphicsItems
        self.imgHHandle = QGraphicsPixmapItem(imgHandleHoure)
        self.imgHHandle.setTransformationMode(Qt.SmoothTransformation)
        self.imgMHandle = QGraphicsPixmapItem(imgHandleMin)
        self.imgMHandle.setTransformationMode(Qt.SmoothTransformation)
        self.imgSHandle = QGraphicsPixmapItem(imgHandleSec)
        self.imgSHandle.setTransformationMode(Qt.SmoothTransformation)
        self.imgSHandleHoure = QGraphicsPixmapItem(imgSalatHandleHoure)
        self.imgSHandleHoure.setTransformationMode(Qt.SmoothTransformation)
        self.imgSHandleMin = QGraphicsPixmapItem(imgSalatHandleMin)
        self.imgSHandleMin.setTransformationMode(Qt.SmoothTransformation)

        scene = QGraphicsScene(self)
        view = QGraphicsView(scene, self)
        view.setGeometry(0,0, 210, 210)
        view.setSceneRect(0, 0, 202, 202)



        #view.fitInView(0, 0, 202, 202, Qt.KeepAspectRatio)

        view.setStyleSheet("background: transparent")
        view.setStyleSheet("background: transparent; border: none;")


        scene.addPixmap(imgBg)
        scene.addItem(self.imgSHandleHoure)
        scene.addItem(self.imgSHandleMin)
        scene.addItem(self.imgHHandle)
        scene.addItem(self.imgMHandle)
        scene.addItem(self.imgSHandle)
        
        midSecW = imgHandleSec.width() / 2
        midSecH = imgHandleSec.height() / 2
        self.imgSHandle.setTransformOriginPoint(QPoint(midSecW, midSecH))

        midMinW = imgHandleMin.width() / 2
        midMinH = imgHandleMin.height() / 2
        self.imgMHandle.setTransformOriginPoint(QPoint(midMinW, midMinH))

        midHoureW = imgHandleHoure.width() / 2
        midHoureH = imgHandleHoure.height() / 2
        self.imgHHandle.setTransformOriginPoint(QPoint(midHoureW, midHoureH))

        midSHoureW = imgSalatHandleHoure.width() / 2
        midSHoureH = imgSalatHandleHoure.height() / 2
        self.imgSHandleHoure.setTransformOriginPoint(QPoint(midSHoureW, midSHoureH))

        midSMinW = imgSalatHandleMin.width() / 2
        midSMinH = imgSalatHandleMin.height() / 2
        self.imgSHandleMin.setTransformOriginPoint(QPoint(midSMinW, midSMinH))


            


        # Initiate handles position
        s = int(self.getTime()[2])
        m = int(self.getTime()[1])
        h = int(self.getTime()[0])

        self.imgSHandle.setRotation(s * 6)
        self.imgMHandle.setRotation(m * 6)
        self.imgHHandle.setRotation(h * 30 + m / 2)
        


        timer = QTimer(self)
        timer.timeout.connect(self.rotateHandles)
        timer.start(1000)


    def rotateHandles(self):
        s = int(self.getTime()[2])
        m = int(self.getTime()[1])
        h = int(self.getTime()[0])
        self.imgSHandle.setRotation(s * 6)
        self.imgMHandle.setRotation(m * 6)
        self.imgHHandle.setRotation(h * 30  + m  / 2)

        imsakAdhan   =   str(self.pt.times["imsak"])   + ":00"
        fajrAdhan    =   str(self.pt.times["fajr"])    + ":00"
        dhuhrAdhan   =   str(self.pt.times["dhuhr"])   + ":00"
        asrAdhan     =   str(self.pt.times["asr"])     + ":00"
        maghribAdhan =   str(self.pt.times["maghrib"]) + ":00"
        ishaAdhan    =   str(self.pt.times["isha"])    + ":00"


        if(str(self.now()) >= imsakAdhan):
            spFajr = str(self.pt.times["fajr"]).split(":")
            fajrM = int(spFajr[1])
            fajrH = int (spFajr[0])
            self.imgSHandleMin.setRotation(fajrM * 6)
            self.imgSHandleHoure.setRotation(fajrH * 30 + fajrH / 2)

        if(str(self.now()) >= fajrAdhan):
            spDhuhr = str(self.pt.times["dhuhr"]).split(":")
            dhuhrM = int(spDhuhr[1])
            dhuhrH = int (spDhuhr[0])
            self.imgSHandleMin.setRotation(dhuhrM * 6)
            self.imgSHandleHoure.setRotation(dhuhrH * 30 + dhuhrM / 2)

        if(str(self.now()) >= dhuhrAdhan):
            spAsr = str(self.pt.times["asr"]).split(":")
            asrM = int(spAsr[1])
            asrH = int (spAsr[0])
            self.imgSHandleMin.setRotation(asrM * 6)
            self.imgSHandleHoure.setRotation(asrH * 30 + asrM / 2)

        if(str(self.now()) >= asrAdhan):
            spMaghrib = str(self.pt.times["maghrib"]).split(":")
            maghribM = int(spMaghrib[1])
            maghribH = int (spMaghrib[0])
            self.imgSHandleMin.setRotation(maghribM * 6)
            self.imgSHandleHoure.setRotation(maghribH * 30 + maghribM / 2)

        if(str(self.now()) >= maghribAdhan):
            spIsha = str(self.pt.times["isha"]).split(":")
            ishaM = int(spIsha[1])
            ishaH = int (spIsha[0])
            self.imgSHandleMin.setRotation(ishaM * 6)
            self.imgSHandleHoure.setRotation(ishaH * 30 + ishaM / 2)

        if(str(self.now()) >= ishaAdhan or self.now() < imsakAdhan):
            spImsak = str(self.pt.times["imsak"]).split(":")
            imsakM = int(spImsak[1])
            imsakH = int (spImsak[0])
            self.imgSHandleMin.setRotation(imsakM * 6)
            self.imgSHandleHoure.setRotation(imsakH * 30 + imsakM / 2)

    def getTime(self):
        formatedTime = str(datetime.now().strftime("%H:%M:%S"))
        st =  formatedTime.split(":")
        return st

    def now(self):
        formatedTime = str(datetime.now().strftime("%H:%M:%S"))
        return formatedTime