'''
Created on Mar 5, 2020
Class project to collaborate on a GitHub repo
@author: nicomp
'''
class Team:
    def __init__(self, teamName, activity):
        self.teamName = teamName
        self.activity = activity
        
    def toString(self):
        return "Team name = " + self.teamName + ", activity = " + self.activity
      