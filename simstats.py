# CMPT 120 Intro to Programming
# Lab #10 – Working with Objects and Simulation
# Author: Nicholas Siconolfi
# Created: 2018-11-15
# simstats.py

class SimStats:
   def __init__(self):
      self.winsA = 0
      self.winsB = 0
      self.shutsA = 0
      self.shutsB = 0

   def update(self, aGame):
      a, b = aGame.Scores()
      if a > b:
         self.winsA = self.winsA + 1
         if b == 0:
            self.shutsA = self.shutsA + 1
         else:
            self.winsB = self.winsB + 1
         if a == 0:
            self.shutsB = self.shutsB + 1
                
   def __printHeading(self):
      print("Summary of", self.winsA + self.winsB, "games:\n")
      print("          wins (% total)    shutouts  (% wins) ")
      print("-----------------------------------------------")

   def printReport(self):
      self.__printHeading()
      n = self.winsA + self.winsB 
      self.printLine("A", self.winsA, self.shutsA, n);
      self.printLine("B", self.winsB, self.shutsB, n);

   def printLine(self, label, wins, shuts, n):
      template = "Player {0}:{1:5}  ({2:5.1%}) {3:11}     ({4})"
      if wins == 0:
         shutStr = "----- "
      else:
         shutStr = "{0:4.1%}".format(float(shuts)/wins)
         print (template.format(label, wins, float(wins)/n,\
         shuts, shutStr))
        
