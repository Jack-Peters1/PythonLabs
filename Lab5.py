class Time:
    def __init__(self, hours, minutes, seconds,): #construct object
       self.hours = hours
       self.minutes = minutes
       self.seconds = seconds

    def getHours(self):
        return self.hours

    def getMinutes(self):
        return self.minutes

    def getSeconds(self):
        return self.seconds

    def toString(self):
        print(self.hours,":",self.minutes,":",self.seconds)

    def timeInSeconds(self): #convert everything to seconds
        return self.hours*3600 + self.minutes*60 + self.seconds

    def changeTheTime(self, h, m, s): #modify time
        self.hours = h
        self.minutes = m
        self.seconds = s

    def twelveHourClock(self): #set clock to 12 hours
        if self.hours > 12 and self.hours != 24:#check if it is afternoon
            return str(self.hours-12,":",self.minutes,":",self.seconds, " PM")
        elif self.hours< 12: #check if it is morning
            return str(self.hours,":",self.minutes,":",self.seconds, " AM")
        elif self.hours == 24: #check if it is midnight
            return str(self.hours-12,":",self.minutes,":",self.seconds, " AM")
        elif self.hours == 12: #check if it is noon
            return str(self.hours,":",self.minutes,":",self.seconds, " PM")

    def whatTimeIsIt(self): #calculate time of day
        if self.hours > 6 and self.hours <12: # if its morning
            return "morning"
        elif self.hours >=12 and self.hours <17: # if its afternoon
            return "afternoon"
        elif self.hours >=17 and self.hours < 22: #if its evening
            return "evening"
        else: # if its night
           return "nighttime"

    def compareTo(self, Time): # compare times in seconds and return
        return self.timeInSeconds() - Time.timeInSeconds()
