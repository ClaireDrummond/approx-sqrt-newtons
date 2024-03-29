 # adapted from: https://tour.golang.org/flowcontrol/8

def sqrt(x):
    # initial guess.
    z = 1.0
    # Keep getting a better estimate for the square root of x until you are withintwo decimal places
    while abs(z*z - x) >= 0.01:
        # get a better approximation for the sqaure root
        z -= (z*z - x) / (2*z)

    return z

# calculate the square root of 8
z = (sqrt(8.0))
print (z)
#print the square of the sqaure root
print(z*z)
