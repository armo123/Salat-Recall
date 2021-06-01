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

        pt = GetPrayerTimes()

        # Loading Images
        self.setFixedSize(210, 210)
        imgBg = QPixmap(':clock-bg.png')
        imgHandleHoure = QPixmap(':houres-handle.png')
        imgHandleMin = QPixmap(':minutes-handle.png')
        imgHandleSec = QPixmap(':seconds-handle.png')
        imgSalatHandleHoure = QPixmap(":salatHouresHandle.png")
        imgSalatHandleMin = QPixmap(":salatMinHandle.png")

        # Converting resouces into QGraphicsItems
        imgHHandle = QGraphicsPixmapItem(imgHandleHoure)
        imgHHandle.setTransformationMode(Qt.SmoothTransformation)
        imgMHandle = QGraphicsPixmapItem(imgHandleMin)
        imgMHandle.setTransformationMode(Qt.SmoothTransformation)
        imgSHandle = QGraphicsPixmapItem(imgHandleSec)
        imgSHandle.setTransformationMode(Qt.SmoothTransformation)
        imgSHandleHoure = QGraphicsPixmapItem(imgSalatHandleHoure)
        imgSHandleHoure.setTransformationMode(Qt.SmoothTransformation)
        imgSHandleMin = QGraphicsPixmapItem(imgSalatHandleMin)
        imgSHandleMin.setTransformationMode(Qt.SmoothTransformation)

        scene = QGraphicsScene(self)
        view = QGraphicsView(scene, self)
        view.setGeometry(0,0, 210, 210)
        view.setSceneRect(0, 0, 202, 202)



        #view.fitInView(0, 0, 202, 202, Qt.KeepAspectRatio)

        view.setStyleSheet("background: transparent")
        view.setStyleSheet("background: transparent; border: none;")


        scene.addPixmap(imgBg)
        scene.addItem(imgSHandleHoure)
        scene.addItem(imgSHandleMin)
        scene.addItem(imgHHandle)
        scene.addItem(imgMHandle)
        scene.addItem(imgSHandle)
        
        midSecW = imgHandleSec.width() / 2
        midSecH = imgHandleSec.height() / 2
        imgSHandle.setTransformOriginPoint(QPoint(midSecW, midSecH))

        midMinW = imgHandleMin.width() / 2
        midMinH = imgHandleMin.height() / 2
        imgMHandle.setTransformOriginPoint(QPoint(midMinW, midMinH))

        midHoureW = imgHandleHoure.width() / 2
        midHoureH = imgHandleHoure.height() / 2
        imgHHandle.setTransformOriginPoint(QPoint(midHoureW, midHoureH))

        midSHoureW = imgSalatHandleHoure.width() / 2
        midSHoureH = imgSalatHandleHoure.height() / 2
        imgSHandleHoure.setTransformOriginPoint(QPoint(midSHoureW, midSHoureH))

        midSMinW = imgSalatHandleMin.width() / 2
        midSMinH = imgSalatHandleMin.height() / 2
        imgSHandleMin.setTransformOriginPoint(QPoint(midSMinW, midSMinH))

        def getTime():
            formatedTime = str(datetime.now().strftime("%H:%M:%S"))
            st = splitedTime = formatedTime.split(":")
            return st
            


        # Initiate handles position
        s = int(getTime()[2])
        m = int(getTime()[1])
        h = int(getTime()[0])

        imgSHandle.setRotation(s * 6)
        imgMHandle.setRotation(m * 6)
        imgHHandle.setRotation(h * 30 + m / 2)
        
        def now():
            formatedTime = str(datetime.now().strftime("%H:%M:%S"))
            return formatedTime


            

        def rotateHandles():
            s = int(getTime()[2])
            m = int(getTime()[1])
            h = int(getTime()[0])
            imgSHandle.setRotation(s * 6)
            imgMHandle.setRotation(m * 6)
            imgHHandle.setRotation(h * 30  + m  / 2)

            imsakAdhan   =   str(pt.times["imsak"])   + ":00"
            fajrAdhan    =   str(pt.times["fajr"])    + ":00"
            dhuhrAdhan   =   str(pt.times["dhuhr"])   + ":00"
            asrAdhan     =   str(pt.times["asr"])     + ":00"
            maghribAdhan =   str(pt.times["maghrib"]) + ":00"
            ishaAdhan    =   str(pt.times["isha"])    + ":00"


            if(str(now()) >= imsakAdhan):
                spFajr = str(pt.times["fajr"]).split(":")
                fajrM = int(spFajr[1])
                fajrH = int (spFajr[0])
                imgSHandleMin.setRotation(fajrM * 6)
                imgSHandleHoure.setRotation(fajrH * 30 + fajrH / 2)

            if(str(now()) >= fajrAdhan):
                spDhuhr = str(pt.times["dhuhr"]).split(":")
                dhuhrM = int(spDhuhr[1])
                dhuhrH = int (spDhuhr[0])
                imgSHandleMin.setRotation(dhuhrM * 6)
                imgSHandleHoure.setRotation(dhuhrH * 30 + dhuhrM / 2)

            if(str(now()) >= dhuhrAdhan):
                spAsr = str(pt.times["asr"]).split(":")
                asrM = int(spAsr[1])
                asrH = int (spAsr[0])
                imgSHandleMin.setRotation(asrM * 6)
                imgSHandleHoure.setRotation(asrH * 30 + asrM / 2)

            if(str(now()) >= asrAdhan):
                spMaghrib = str(pt.times["maghrib"]).split(":")
                maghribM = int(spMaghrib[1])
                maghribH = int (spMaghrib[0])
                imgSHandleMin.setRotation(maghribM * 6)
                imgSHandleHoure.setRotation(maghribH * 30 + maghribM / 2)

            if(str(now()) >= maghribAdhan):
                spIsha = str(pt.times["isha"]).split(":")
                ishaM = int(spIsha[1])
                ishaH = int (spIsha[0])
                imgSHandleMin.setRotation(ishaM * 6)
                imgSHandleHoure.setRotation(ishaH * 30 + ishaM / 2)

            if(str(now()) >= ishaAdhan or now() < imsakAdhan):
                spImsak = str(pt.times["imsak"]).split(":")
                imsakM = int(spImsak[1])
                imsakH = int (spImsak[0])
                imgSHandleMin.setRotation(imsakM * 6)
                imgSHandleHoure.setRotation(imsakH * 30 + imsakM / 2)

        timer = QTimer(self)
        timer.timeout.connect(rotateHandles)
        timer.start(1000)

