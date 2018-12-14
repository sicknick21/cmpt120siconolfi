# CMPT 120 Intro to Programming
# Project 5
# Author: Nicholas Siconolfi
# Created: 2018-12-10
# calculatorproject5.py
# This program reprsents the graphical interface of the calculator along with the functions to calculate arithmetic sequences.

from graphics import *
from button import Button 
import math

class Calculator:
    def __init__(self):
        win = GraphWin("Calculator Project")
        win.setCoords(0,0,16.5,21)   
        win.setBackground("lightgreen")
        self.win = win
        self.__createButtons()
        self.__createDisplay()
        self.finAnswer()
        self.memstorage()
        self.mem = "0"

#Creates the display for the buttons and the memory.

    def memstorage(self):
        text = Text(Point(12,18.75),"")
        text.draw(self.win)
        text.setFace("courier")
        text.setSize(5)
        self.M = text
        
      
    def __createButtons(self):
        iSpecs = [(3.75,1.5,'0'), (6,1.5,'.'), (1.5,3.75,'1'), (3.75,3.75,'2'), (6,3.75,'3'),
                   (8.25,3.75,'+'), (10.5,3.75,'-'), (1.5,6,'4'), (3.75,6,'5'), (6,6,'6'),
                   (8.25,6,'*'), (10.5,6,'/'), (1.5,8.25,'7'), (3.75,8.25,'8'), (6,8.25,'9'),
                   (8.25,8.25,'Del'),(10.5,8.25,'C'), (12.75,1.5,'1/x'), (12.75,3.75,'%'),
                   (12.75,8.25,'sqrt'), (12.75,6,'x**2'), (3.75,15,'M+'), (6,15,'MS'),
                   (8.25,15,'MR'), (1.5,15,'MC'), (12.75,15,'S')]
        self.buttons = []
        
        for (cx,cy,label) in iSpecs:
            self.buttons.append(Button(self.win,Point(cx,cy),2.27,2.33,label))
        self.buttons.append(Button(self.win,Point(9.3,1.5),4.5,1.9,"="))
        for i in self.buttons:  i.activate()


#Creates new mode for the additional buttons
    def __Scientific(self):
        bSpecs = bSpecs = [(3.75,1.5,'0'), (6,1.5,'.'), (1.5,3.75,'1'), (3.75,3.75,'2'), (6,3.75,'3'),
                   (8.25,3.75,'+'), (10.5,3.75,'-'), (1.5,6,'4'), (3.75,6,'5'), (6,6,'6'),
                   (8.25,6,'*'), (10.5,6,'/'), (1.5,8.25,'7'), (3.75,8.25,'8'), (6,8.25,'9'),
                   (8.25,8.25,'Del'),(10.5,8.25,'C'), (12.75,1.5,'1/x'), (12.75,3.75,'%'),
                   (12.75,8.25,'sqrt'), (12.75,6,'x**2'), (3.75,15,'M+'), (6,15,'MS'),
                   (8.25,15,'MR'), (1.5,15,'MC'), (1.5,10.5,'ln'), (1.5, 12.75,'log'),
                    (3.75,10.5,'x**y'), (15,8.5,'atan'), (15,6.5,'asin'), (15,4.00,'acos'), (6,10.5,'10^x'), (10.5,10.5,'sin'),
                (8.25,10.5 ,'cos'), (12.75,10.5,'tan'), (15,10.5,'('), (15,12.5,')')]
    
  
        self.buttons = []

        for (cx,cy,label) in iSpecs:
            self.buttons.append(Button(self.win,Point(cx,cy),2.350,2.30,label))
        self.buttons.append(Button(self.win,Point(9.3,1.5),4.5,1.9,"="))
        for i in self.buttons:  i.activate()


# Creates the display for the input and output
    def __createDisplay(self):
        bg = Rectangle(Point(.75,18), Point(12.75,20))
        bg.setFill('red')
        bg.draw(self.win)
        text = Text(Point(6.75,18.75), "")
        text.draw(self.win)
        text.setFace("courier")
        text.setStyle("bold")
        text.setSize(10)
        self.display = text

    def finAnswer(self):
        bg = Rectangle(Point(.75,16.5), Point(12.75,18))
        bg.setFill('red')
        bg.draw(self.win)
        text = Text(Point(6.75,17.25), "")
        text.draw(self.win)
        text.setFace("courier")
        text.setStyle("bold")
        text.setSize(10)
        self.finAnswer = text

#Creates the function to click the buttons and how they are used.
    def getButton(self):
        while True:
            b = self.win.getMouse()
            for i in self.buttons:
                if i.clicked(b):
                    return i.getLabel()
 

    def processButton(self, key):

        text = self.display.getText()

        if key == 'C':

            self.display.setText("")
            self.finAnswer.setText("")
        elif key == 'Del':

            self.display.setText(text[:-1])

        elif key == '=':

            try:

                result = eval(text)

            except:

                result = 'Error'

            self.finAnswer.setText(str(result))

        else:

            self.display.setText(text+key)

            
        if key == 'MR':
            self.display.setText(self.mem)
            
        
        elif key == 'MS':
            self.mem = text or '0'
            if self.mem != '0':
                self.M.setText('M')
        elif key == 'M+':
            self.mem = str(eval(text+'+'+str(self.mem)))
            if self.mem != '0':
                self.M.setText('M+')
        elif key == 'MC':
            self.mem = "0"
            self.M.setText('')
        elif key == '1/x':
            try:
                result = 1/(eval(text))
            except:
                result = 'Error'
            self.finAnswer.setText(str(result))
        elif key == 'sqrt':
            result = (eval(text))**0.5
            self.finAnswer.setText(str(result))
            
        elif key == 'x**2':
            result = eval(text)**2
            self.finAnswer.setText(str(result))
        
      
        elif key == 'sqrt':
            result = (eval(text))**0.5
            self.finAnswer.setText(str(result))

        elif key == 'S':
            self.__Scientific()
            self.display.setText(text[-10:])

        elif key  == 'back':
            self.__createButtons()
            self.display.setText(text[-10:])

        elif key == 'ln':

            result = math.log(eval(text))
            self.finAnswer.setText(str(result))

        elif key == '10**x':

            result = (eval(text))
            self.finAnswer.setText(str(result))
            
        elif key == 'cos':
            result = math.cos(eval(text))
            self.finAnswer.setText(str(result))

        elif key == 'tan':
            result = math.tan(eval(text))
            self.finAnswer.setText(str(result))

        elif key == 'sin':
            result = math.sin(eval(text))
            self.finAnswer.setText(str(result))

        elif key == 'acos':
            result = math.acos(eval(text))
            self.displayanswer.setText(str(result))

        elif key == 'asin':
            result = math.asin(eval(text))
            self.finAnswer.setText(str(result))

        elif key == 'atan':
            result = math.atan(eval(text))
            self.finAnswer.setText(str(result))
        
        elif key == 'x**y':

            y = eval(input('Please Enter a Value for y:'))
            result = (eval(text))**y
            self.finAnswer.setText(str(result))
            
        elif key == 'log':
            result = math.log10(eval(text))
            self.finAnswer.setText(str(result))
 
        elif key == '10^x':
            result = 10**(eval(text))
            self.finAnswer.setText(str(result))
            
    def run(self):

        while True:

            key = self.getButton()

            self.processButton(key)

 
if __name__ == '__main__':
    tCalc = Calculator()
    tCalc.run()
Calculator()

   
