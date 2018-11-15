# CMPT 120 Intro to Programming
# Lab #10 – Working with Objects and Simulation
# Author: Nicholas Siconolfi
# Created: 2018-11-15
# tennissimulation.py

from simstats import *
from tennismatch import *


def Intro():
    print("This program is used as a simulation for a tennis match ")

def getStats():
    probA = float(input("Enter the probability of A winning: "))
    probB = float(input("Enter the probability of B winning: "))
    n = int(input("Enter the amount of games to simulate: "))
    return probA, probB, n
    
def main():
    Intro()
    probA, probB, n = getStats()
    stats = SimStats()
    for i in range(n):
        thesim = tennisMatch(probA, probB)
        thesim.match()
        stats.update(thesim)
    stats.printReport()

main()
