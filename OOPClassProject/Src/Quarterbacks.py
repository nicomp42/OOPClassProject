'''
Created on Mar 5, 2020

@author: muenchmh
'''
class Quarterback:
    def __init__(self,FirstName, LastName, TeamName):
        self.FirstName = FirstName
        self.LastName = LastName
        self.TeamName = TeamName
    def toString(self):
        return "Quarterback for the " + self.TeamName + " is " + self.FirstName + " " + self.LastName + "."

#CinciQB = Quarterback("Andy","Dalton","Bengals")
#PittsburgQB = Quarterback("Ben","Roethlisberger","Steelers")
#print(CinciQB.toString())
#print(PittsburgQB.toString())