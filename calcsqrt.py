#! /usr/bin/cnv python3

#Steven Joyce
# Calculate the square root of a number

def sqrt(x):
    """
    Calculate the square root of argument x.
    """
    #check that x if positive
    if x < 0:
        print("Error: negative value supplied")
        return -1
    
    # initial guess for square root
    z= x / 2.0

    # continuously improve the guess
    # adapted from https://tour.golang.org/flowcontrol/8
    while abs(x - (z*z)) > 0.00001:
        z = z - ((z*z - x) / (2 * z))

    return z
myVal = 63.0
print("The square root of", myVal, "is", sqrt(myVal))


