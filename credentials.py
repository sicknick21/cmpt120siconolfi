# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Your Name Here
# Created: YYYY-MM-DD


def firstlastname():
    global uname, first, last
    
    first = input("Enter your first name: ")    
    last = input("Enter your last name: ")

def username():
    
    uname = first + last
    print("Hi" , first+"."+last)

def password():

    passwd = input("Create a new password: ")

    while False:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
    print("The force is strong in this one…")

    
    

def main():
    firstlastname()
    username()
    password()

main()
