# CMPT 120 Intro to Programming
# Lab #10 – Working with Objects and Simulation
# Author: Nicholas Siconolfi
# Created: 2018-11-15
# tennismatch.py
from random import random
from tennisplayer import *
# class to simulate a tennis match

class TennisMatch:
    def __init__(self, probA, probB):
        self.playerA = Player(probA)
        self.playerB = Player(probB)
        self.server = self.playerA
        self.setsA = 0
        self.setsB = 0
        self.Awins = 0
        self.Bwins = 0

    def match(self):
        while not self.isOver():
            if self.server.winsServe():
                self.server.incScore()
            else:
                self.changeServer()
                self.server.incScore()
                self.changeServer()

            


    def Scores(self):
        return self.playerA.Score(), self.playerB.Score()

    def changetheServer(self):
        if self.server == self.playerA:
            self.server = self.playerB
        else:
            self.server = self.playerA
            



    def set(self):
        a = self.PlayerA.Scores()
        b = self.PlayerB.Scores()
        if a > b + 10:
             self.setsA = self.setsA + 1
        else:
            self.setsB = self.setsB + 1

            
    def isOver(self):
        return self.playerA.Score() == 50 or self.playerB.Score() == 50 \
            or (self.playerA.Score() == 40 and self.playerB.Score() > 60) \
            or (self.playerB.Score() > 60 and self.playerA.Score() == 40)



            
    def thematchisOver(self):
        return self.sets == 3
    
    def Win(self):
        while not thematchIsOver():
            if self.setsA > self.setsB:
                self.Awins = self.Awins + 1
            else:
                self.Bwins = self.Bwins + 1
