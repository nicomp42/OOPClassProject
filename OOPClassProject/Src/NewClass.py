'''
Created on Mar 5, 2020

@author: bayneslc
'''
class Division:
    def __init__(self, conference, divisionLocation):
        self.divisionLocation = divisionLocation
        self.conference = conference
        
    def toString(self):
        return "Location =  " + self.divisionLocation + " , Division Conference = " + self.conference
