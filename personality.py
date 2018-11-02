#personality.py
# CMPT 120 Intro to Programming
# Lab #8 - Matrices & Lookup
# Author: Nicholas Siconolfi
# Created: 2018-10-31

#This program shows the emotional state of the AI


from random import random
#Randomizes the first emotion

def main():
    print("Hello AI Nick! What is your current emotion?\n")
    AIstates = ["angry", "disgusted", "fearful", "happy", "sad", "suprised"]
    AINickEmotion = int(random() * 6);
    C = [[1,0,4,3,3,3],
        [2,0,2,4,4,4],
        [0,1,2,4,4,2],
        [1,0,4,3,4,3]]

    def getInteraction():
        cmd = input('AI Nick is ' + AIstates[AINickEmotion] + ', change its emotion for better or worse: ')
        if cmd == "reward":
            return 0
        elif cmd == "punish":
            return 1
        elif cmd == "threaten":
            return 2
        elif cmd == "joke":
            return 3
        else:
            return -1 
        

    def lookupEmotion(currEmotion, userAction):
        return C[userAction][currEmotion]
    while True:
        interact = getInteraction()
        if interact != -1:
            AINickEmotion = lookupEmotion(AINickEmotion, interact)
        else:
            print("That is not a valid command, type again")

main()

          
          




    
