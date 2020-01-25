#! /usr/bin/env python3

# Tomas o'Malley
# Calculate the square root of  a number

def sqrt(x):
    # Initial guess for the square root.
    """
    Calculate the square root of argument x.
    """
    z= x/ 2.0


    # check if x is positive 
    if x < 0:
        print("Negative Value Supplied")
        return -1
    else:
        print("Here we go ....")


    # Continously improve the guess.
    # Adapted from [URL]
    while abs(x - (z*z))> 0.000001:
        
         z-=(( (z*z) - x) / (2*z))


    return z

print(sqrt(63.0))

