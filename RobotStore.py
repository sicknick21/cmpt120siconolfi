#RobotStore.py
# CMPT 120 Intro to Programming
# Lab #9 - Working with Objects
# Author: Nicholas Siconolfi
# Created: 2018-11-7


class Products:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        

    def stock(quantity, price):
        if self.quantity >= count:
            return(True)
        else:
            return(False)
            
    def totalCost(quantity, price):
        cost = self.price * count
        return cost

productNames = [Products("Ultrasonic range finder", 2.50, 4),
         Products("Servo motor", 14.99, 10),
         Products("Servo controller", 44.95, 5),
         Products("Microcontroller Board", 34.95, 7),
         Products("Laser range finder", 149.99, 2),
         Products("Lithium polymer battery", 8.99, 8)]

def getCount():
    count = input("Please enter the amount of products you would like to purchase: ")

def printStock(productNames):
    print("Available Products")
    print("------------------")
    id = 0
    for i in productNames:
        if i.quantity > 0:
            print(id, i.name, "$", i.price)
            id += 1
    print("\n")
    
def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock(productNames)
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit":
            break
        
        prodId = int(vals[0])
        count = int(vals[1])
        product = productNames[prodId]
        if product.quantity >= count:
            if cash >= product.price:
                product.quantity -= count
                cash -= product.price * count
                print("You purchased", count, product.name+".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", product.name)
            
main()
