#calculator.py
#This program reprsents the graphical interface of the calculator along with the functions to calculate arithmetic sequences.

from tkinter import *


class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False


    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)      
        if self.new_num:
            self.current = x=temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)

    #Finding the outcome of the sequence and creating the textbox in the calculator
    def calc_total(self):
        # JA: This was not what you had to do for the project
        # The idea was to create the logic to resolve the equations
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(text_box.get())

    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

    #Defining the operations for the calculator
    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "subtract":
            self.total -= self.current
        if self.op == "multiply":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    #Creating the operations
    def operation(self, op): 
        self.current = float(self.current)
        if self.op_pending:
            self.do_sum()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def cancel(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True

    def all_cancel(self):
        self.cancel()
        self.total = 0

    def sign(self):
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)

#Making the calculator in the graphics interface

sum1 = Calc()
root = Tk()
calc = Frame(root)
calc.grid()

root.title("Calculator Project")
text_box = Entry(calc, justify=RIGHT)
text_box.grid(row = 0, column = 0, columnspan = 3, pady = 3)
text_box.insert(0, "0")

numbers = "123456789"
i = 0
bttn = []
for p in range(1,4):
    for o in range(3):
        bttn.append(Button(calc, text = numbers[i]))
        bttn[i].grid(row = p, column = o, pady = 5)
        bttn[i]["command"] = lambda x = numbers[i]: sum1.num_press(x)
        i += 1

bttn_0 = Button(calc, text = "0")
bttn_0["command"] = lambda: sum1.num_press(0)
bttn_0.grid(row = 2, column = 1, pady = 3)

#Button for the division sign
bttn_div = Button(calc, text = "/")
bttn_div["command"] = lambda: sum1.operation("divide")
bttn_div.grid(row = 4, column = 3, pady = 3)

#Button for the multiplication sign
bttn_mult = Button(calc, text = "*")
bttn_mult["command"] = lambda: sum1.operation("multiply")
bttn_mult.grid(row = 3, column = 3, pady = 3)

#Button for the subtraction sign
minus = Button(calc, text = "-")
minus["command"] = lambda: sum1.operation("subtract")
minus.grid(row = 2, column = 3, pady = 3)

#Button to add in a decimal 
point = Button(calc, text = ".")
point["command"] = lambda: sum1.num_press(".")
point.grid(row = 4, column = 0, pady = 3)

#Button for the addition sign
add = Button(calc, text = "+")
add["command"] = lambda: sum1.operation("add")
add.grid(row = 1, column = 3, pady = 3)

#Button to delete your input and answer
clear = Button(calc, text = "Delete")
clear["command"] = sum1.cancel
clear.grid(row = 5, column = 1, pady = 3)

#Button for the equal sign and to display the answer
equals = Button(calc, text = "=")
equals["command"] = sum1.calc_total
equals.grid(row = 5, column = 3, pady = 3)

root.mainloop()
