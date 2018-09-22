#   Approximates the value of 'pi' by summing the terms of a series.

import math

def main():
    
    n = int(input("Enter the amount of terms? "))

    total = 0.0
    x = 1.0   
    for denominator in range(1, 2*n, 2):
        total = total + x * 4.0/denominator
        x = -x 

    print("Approximation to pi is:", total)
    print("Difference from math.pi:", math.pi - total)

main()
