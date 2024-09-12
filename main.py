import math
import random 
import numpy as np
import matplotlib.pyplot as plt
          	                                	 

# generate random mountains                                                                               	 

w = [.05, random.random()/3, random.random()/3]
h = [1.+math.sin(1+x/.6)*w[0]+math.sin(-.3+x/9.)*w[1]+math.sin(-.2+x/30.)*w[2] for x in range(100)]



# Create a function which take two parameter x and h.
# x is an integer representing the starting point
# y is a list of random mountains
# This function must to return x point representing the high point found.

def climb(x, h):

    high_list = {}

    # here, I loop over the current position of x  with 10 values to the left and 10 values to the right of x.
    for x_new in range(max(0, x-10), min(99, x+11)):
        high_list[f"{x_new}"] = h[x_new]

    # The python method max() search and return the max value of a list.
    max_value = max(high_list.values())

    # Then I implement a condition to verify if the value of the current x is strictly less than the current max value found.
    # If the value of the current x is the max in that case the function return x
    if h[x] < max_value :
        key_max_value = [key for key, val in high_list.items() if val == max_value]
        x = int(key_max_value[0])
        return climb(x, h)
    else :
        return x
    

def main(h):
    # start at a random place                                                                                  	 
    x0 = random.randint(1, 99)

    # Coordinate of the origin point
    x1 = x0
    y1 = h[x1]

    # call the function climb that return x
    x = climb(x0, h)
    
    # coordinate of the x point
    x2 = x
    y2 = h[x]

    # create a list and loop over the length of the h list
    lis = []
    for i in range(len(h)):
        lis.append(i)

    # Buid a chart that display the origin point and the x point in green
    xl = lis
    yl = np.array(h)
    plt.plot(xl, yl, 'r')
    plt.scatter(x1, y1)
    plt.scatter(x2, y2, c = 'green', marker = 'h')
    plt.show()


    return x0, x

# call the main function
main(h)