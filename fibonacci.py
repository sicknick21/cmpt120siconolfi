#fibonacci.py
# Write a program that computes the nth Fibonacci number where n is a value input by the user.

import math
def main():

    print("The Fiboncaci sequence")
    n = int(input("Enter a value:"))
    x,fib = 1,1

    for i in range(0, n - 2):
        x, fib=fib, x+fib

    print("The nth Fibonacci number is", fib)
    
main()
    
