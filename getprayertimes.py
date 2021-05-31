#!/usr/bin/env python
# -*- coding: utf-8 -*-


from configparser import ConfigParser
from praytimes import PrayTimes
from datetime import datetime



class GetPrayerTimes():
    # Reading config file
    def __init__(self, *args, **kwargs):
        self.config = ConfigParser()
        self.config.read("config.ini")
        try:
            self.lat = self.config["Settings"]["Latitude"]
            self.long = self.config["Settings"]["longitude"]
        except KeyError:
            self.lat = "00.00"
            self.long = "00.00"
        # self.setWindowFlag(Qt.WindowStaysOnTopHint )

        # Creating PrayerTimes instance
        try:
            self.methodconfig = self.config["Settings"]["Method"]
        except KeyError:
            self.methodconfig = "MWL"

        self.PT = PrayTimes()
        self.PT.setMethod(self.methodconfig)

        # Ajusting time
        # PT.adjust({
            # "maghrib" : "+0.5 min"
            # })

        # Fine tuning necessary prayer times according to the region
        try:
            self.imsakcopnfig = float(self.config["Settings"]["Imsak"])
        except KeyError:
            self.imsakcopnfig = 0 
        
        try:
            self.fajrconfig = float(self.config["Settings"]["Fajr"])
        except KeyError:
            self.fajrconfig = 0

        try:
            self.dhuhrconfig = float(self.config["Settings"]["Dhuhr"])
        except KeyError:
            self.dhuhrconfig = 0

        try:
            self.asrconfig = float(self.config["Settings"]["Asr"])
        except KeyError:
            self.asrconfig = 0

        try:
            self.maghribconfig = float(self.config["Settings"]["Maghrib"])
        except KeyError:
            self.maghribconfig = 0

        try:
            self.ishaconfig = float(self.config["Settings"]["Isha"])
        except KeyError:
            self.ishaconfig = 0
        
        self.PT.tune({
            "imsak"    : self.imsakcopnfig,
            "fajr"     : self.fajrconfig,
            "dhuhr"    : self.dhuhrconfig,
            "asr"      : self.asrconfig,
            "maghrib"  : self.maghribconfig,
            "isha"     : self.ishaconfig
            })

        # Getting the current date
        self.formatedDate = str(datetime.today().strftime("%Y/%m/%d"))


        # Splitting the date so it fits in the list of getTimes method 
        self.splittedDate = self.formatedDate.split("/")
        self.currentYear = int(self.splittedDate[0])
        self.currentMonth = int(self.splittedDate[1])
        self.currentDay = int(self.splittedDate[2])
        self.times = self.PT.getTimes((self.currentYear, self.currentMonth, self.currentDay),\
                (float(self.lat), float(self.long)), +1)