import matplotlib.pyplot as plt
import numpy as np

import commandHandler
import lagrange as lagrange

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def main():
    points = [ [1, 1],[2, 4],[-2, 4],[3, 9]]

    lag_pol = lagrange.create_Lagrange_polynomial(points)


    new_points = [ 0, 1, 2, 3, 4, 5, 6]

    for i in new_points:
        x = i
        print(x)
        print(" x = {:.4f}\t y = {:4f}".format(x, lag_pol(x)))

if __name__ == "__main__":
    commandHandler.work()