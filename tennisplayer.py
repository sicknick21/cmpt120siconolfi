# CMPT 120 Intro to Programming
# Lab #10 – Working with Objects and Simulation
# Author: Nicholas Siconolfi
# Created: 2018-11-15
# tennisplayer.py
from random import *

class TennisPlayer:
    def __init__(self, prob):
        self.prob = prob
        self.score = 0

    def winsServe(self):
        
        return random() <= self.prob

    def incScore(self):
        
        if self.score == 0:
            self.score = self.score + 15
        elif self.score == 15:
            self.score = self.score + 15
        elif self.score == 30:
            self.score = self.score + 10
        elif self.score == 40:
            self.score = self.score + 10

    def Score(self):
        
        return self.score
        
