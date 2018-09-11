# rover.py
# Program to calculate the time for a photo to reach Earth from Mars

def main():
    speedLight = 186000
    distance = 34000000

    time = distance / speedLight
    print ("The time for a picture to reach Earth is", time, "seconds")

main()
