'''
Created on Mar 5, 2020

@author: lamberei
'''
class Building:
    def __init__(self, buildingType, capacity):
        self.buildingType = buildingType
        self.capacity = capacity
        
    def toString(self):
        return "Building Type = " + self.buildingType + ", capacity = " + self.capacity 