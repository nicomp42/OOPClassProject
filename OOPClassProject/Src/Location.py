'''
Created on Mar 5, 2020

@author: carmiccc
'''
class Location:
    def __init__(self, region, city):
        self.region = region
        self.city = city
        
    def toString(self):
        return "Location of Team " + self.city + ", region: " + self.region
    