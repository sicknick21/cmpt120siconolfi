# CMPT 120 Intro to Programming
# Project 4
# Author: Nicholas Siconolfi
# Created: 2018-11-28
# calculatorclasses.py
# This program reprsents the graphical interface of the calculator along with the functions to calculate arithmetic sequences.

from graphics import *

#Restarted parts of the project to do what we do in class in order to implement the memory and the classes in a easier way 

def main():
    win = drawCalculator()
    getInput(win)


def drawCalculator():
    win = GraphWin("Calculator Project", 325, 440)
    win.setBackground("lightgreen")
    win.setCoords(0, -3, 13, 19)

    # Creating the display on screen
    Rectangle(Point(1, 18), Point(12, 16)).draw(win)
    
    for c in range(-2, 14, 3):
        for r in range(3, 13, 3):
            Rectangle(Point(r - 2, c + 2), Point(r, c)).draw(win)

    # List for buttons
    button = ["Clear", "Quit", "", "=", "+/-", "0", ".", "-", "7", "8", "9", "+",
           "4", "5", "6", "*", "1", "2", "3", "/", "M+", "M-", "MR", "MC"]

    i = 0

    # Creating the buttons with the spacing 
    for c in range(-1, 15, 3):
        for r in range(2, 12, 3):
            Text(Point(r, c), button[i]).draw(win)
            i = i + 1
    return win


def getInput(win):
    click = ""
    i = ""
    equation = []
    printedEquation = Text(Point(0, 0), "")
    printedEquation.undraw()

    mem = 0
    # Creating the equation
    while (i != "="):
        equation.append(click)
        prints = "".join(equation)
        print(prints)
        printedEquation.undraw()
        printedEquation = Text(Point(6.5, 17), prints)
        printedEquation.draw(win)

        # Clicks from the mouse
        p = win.getMouse()
        x = p.getX()
        y = p.getY()

        whereClicked = Buttons(x, y, win, prints, mem, printedEquation, equation)
        click, equation, mem = whereClicked.Click()


class Buttons:
    # This class creates the buttons
    def __init__(self, x, y, win, printed, currentMemory, printedEquation, equation):
        self.x = x
        self.y = y
        self.clicked = ""
        self.win = win
        self.printed = printed
        self.memory = currentMemory
        self.printedEquation = printedEquation
        self.equation = equation

    def Click(self):
        # Creating the memory functions
        if self.y <= 15 and self.y >= 13:
            # Creates the M+
            if self.x <= 3 and self.x >= 1:
                self.clicked = ""
                newMemory = int(self.printed)
                self.memory = (self.memory + newMemory)
            # Creates the M-
            elif (self.x <= 6 and self.x >= 4):
                self.clicked = ""
                newMemory = int(self.printed)
                self.memory = (self.memory - newMemory)
            # Creates the MR
            elif (self.x <= 9 and self.x >= 7):
                self.printed = ""
                self.equation = []
                self.clicked = str(self.memory)
            # Creates the MC
            elif (self.x <= 12 and self.x >= 10):
                self.clicked = ""
                self.memory = 0
            # Creates the numbers to put into the memory
        if (self.y <= 12 and self.y >= 10):
            if (self.x <= 3 and self.x >= 1):
                self.clicked = "1"
            elif (self.x <= 6 and self.x >= 4):
                self.clicked = "2"
            elif (self.x <= 9 and self.x >= 7):
                self.clicked = "3"
            elif (self.x <= 12 and self.x >= 10):
                self.clicked = "/"
        elif (self.y <= 9 and self.y >= 7):
            if (self.x <= 3 and self.x >= 1):
                self.clicked = "4"
            elif (self.x <= 6 and self.x >= 4):
                self.clicked = "5"
            elif (self.x <= 9 and self.x >= 7):
                self.clicked = "6"
            elif (self.x <= 12 and self.x >= 10):
                self.clicked = "*"
        elif (self.y <= 6 and self.y >= 4):
            if (self.x <= 3 and self.x >= 1):
                self.clicked = "7"
            elif (self.x <= 6 and self.x >= 4):
                self.clicked = "8"
            elif (self.x <= 9 and self.x >= 7):
                self.clicked = "9"
            elif (self.x <= 12 and self.x >= 10):
                self.clicked = "+"
        elif (self.y <= 3 and self.y >= 1):
            if (self.x <= 3 and self.x >= 1):
                self.clicked = ""
            elif (self.x <= 6 and self.x >= 4):
                self.clicked = "0"
            elif (self.x <= 9 and self.x >= 7):
                self.clicked = "."
            elif (self.x <= 12 and self.x >= 10):
                self.clicked = "-"
        elif (self.y <= 0 and self.y >= -2):
            # The Enter button function
            if (self.x <= 12 and self.x >= 10):
                PrintedDisplay = Display(self.printed)
                FinAnswer = Calculate(PrintedDisplay.getDisplayNum())
                FinAnswer.concat()
                FinAnswer.calc()

                self.printedEquation.undraw()
                finalAnswer = Text(Point(6.5, 17), FinAnswer.getFinAnswer())
                finalAnswer.draw(self.win)
                # Check to exit the loop
                i = "="
            # The Clear button function
            elif (self.x <= 3 and self.x >= 1):
                self.clicked = ""
                self.printed = ""
                self.equation = []
            # The Quit button function to leave the calculator
            elif (self.x <= 6 and self.x >= 4):
                self.win.close()

        p = self.win.getMouse()
        self.x = p.getX()
        self.y = p.getY()

        if ((self.y <= 0 and self.y >= -2) and (self.x <= 3 and self.x >= 1)):
            finalAnswer.undraw()
            getInput(self.win)
        if ((self.y <= 0 and self.y >= -2) and (self.x <= 6 and self.x >= 4)):
            self.win.close()
        return self.clicked, self.equation, self.memory



class Display:
    # Class to make the display
    def __init__(self, displayNum):
        self.displayNum = displayNum

    def getDisplayNum(self):
        return self.displayNum

    def setDisplayNum(self, newNum):
        self.displayNum = newNum


class Calculate:
    # Class to calculate the math
    def __init__(self, display):
        self.display = display
        self.finAnswer = 0
        self.endOperation = 0

    def getFinAnswer(self):
        return self.finAnswer

    def eq(self, finalNum, i, equation=[]):
        del equation[i - 1:i + 2]
        equation.insert(i - 1, finalNum)
        print(equation)
        self.display = equation

    # How to multiply the input
    def multiply(self, num1, num2):
        self.endOperation = num1 * num2

    # How to divide the input
    def divide(self, num1, num2):
        self.endOperation = num1 / num2

    # How to add the input
    def add(self, num1, num2):
        self.endOperation = num1 + num2

    # How to subtract the input
    def subtract(self, num1, num2):
        self.endOperation = num1 - num2

    def concat(self):
        finEq = []
        i = 0
        number = ""

        for n in range(len(self.display)):
            if self.display[n] == "+" or self.display[n] == "-" or self.display[n] == "*" or self.display[n] == "/":

                number = self.display[n - i: n]
                newNumber = "".join(number)
                finEq.append(newNumber)
                finEq.append(self.display[n])
                i = 0
                number = ""
            elif len(self.display) == n + 1:
                number = self.display[n - i: n + 1]
                newNumber = "".join(number)
                finEq.append(newNumber)
                i = 0
                number = ""
            else:
                i = i + 1

        self.display = finEq

    def calc(self):

        while len(self.display) != 1:

            while ("*" in self.display) or ("/" in self.display):

                for i in range(1, len(self.display)):
                    if (self.display[i] == "*") or (self.display[i] == "/"):
                        # Multiplying button
                        if self.display[i] == "*":
                            self.multiply(float(self.display[i - 1]), float(self.display[i + 1]))
                            self.endOperation = str(self.endOperation)
                            self.eq(self.endOperation, i, self.display)
                            break

                        # Dividing button
                        elif self.display[i] == "/":
                            self.divide(float(self.display[i - 1]), float(self.display[i + 1]))
                            self.endOperation = str(self.endOperation)
                            self.ins(self.endOperation, i, self.display)
                            break
                        break

            for i in range(1, len(self.display)):
                if (self.display[i] == "+") or (self.display[i] == "-"):

                    # Add button
                    if self.display[i] == "+":
                        self.add(float(self.display[i - 1]), float(self.display[i + 1]))
                        self.endOperation = str(self.endOperation)
                        self.eq(self.endOperation, i, self.display)
                        break
                    # Subtraction button
                    elif self.display[i] == "-":
                        self.subtract(float(self.display[i - 1]), float(self.display[i + 1]))
                        self.endOperation = str(self.endOperation)
                        self.eq(self.endOperation, i, self.display)
                        break

                    break

        self.finAnswer = self.display[0]
main()
