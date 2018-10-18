#ArithmeticEngine.py

# CMPT 120 - Lab #6
# Nicholas Siconolfi
# 16-Oct-2018
###
def showIntro():
        print("Welcome to the Arithmetic Engine!")
        print("=================================\n")

        
def showOutro():
        print("\nThank you for using the Arithmetic Engine…")
        print("\nPlease come back again soon!")
def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ")
        cmd = cmd.lower()
        
        print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")


        
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        if cmd == "add":
            result = num1 + num2
        elif cmd == "sub":
            result = num1 - num2
        elif cmd == "mult":
            result = num1 * num2
        elif cmd == "div":
            result = num1 // num2
        elif cmd == "quit":
             break
            
        else:
            print("\n",cmd , "is not a valid command.")
            break

        print("The result is " + str(result) + ".\n")


def main():
    showIntro()
    doLoop()
    showOutro()


main()
