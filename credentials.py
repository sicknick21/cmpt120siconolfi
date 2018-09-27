# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Your Name Here
# Created: YYYY-MM-DD


def firstlastname():
    global uname, first, last
    
    first = input("Enter your first name: ")    
    last = input("Enter your last name: ")
    first = first.lower()
    last = last.lower()

def username():
    global uname
    
    uname = first +"."+ last
   

def password():
    global passwd
    passwd = input("Create a new password: ")



def strength():
    if passwd.isupper():
        print("Password needs a lowercase letter")
    if passwd.islower():
        print("Password needs a capital letter")
              
    
    if len(passwd) <8:
           print("Fool of a Took! That password is feeble!")
    if len(passwd) >8:
        print("The force is strong in this one…")
           
def email():
    
    print("Account configured. Your new email address is", uname + "@marist.edu")

      
def main():
    firstlastname()
    username()
    password()
    strength()
    email()

main()
