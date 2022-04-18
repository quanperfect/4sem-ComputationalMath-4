import matplotlib.pyplot as plt
import numpy as np
import lagrange
import functions

def scan_x_for_minmax(points):
    max = points[0][0]
    min = points[0][1]

    for i in points:
        if i[0] > max:
            max = i[0]
        if i[0] < min:
            min = i[0]

    return [min, max]

def plot(lagrange_polynom, points, id):
    plt.title("Lagrange polynomial interpolation")
    minmax = scan_x_for_minmax(points)
    min = minmax[0]
    max = minmax[1]

    x = np.linspace(min, max, 10000)
    y = []

    for i in x:
        y.append(lagrange_polynom(i))

    plt.plot(x, y, color='red', zorder=2, label='polynom', linewidth=2)

    if (id >= 1 and id <= 3):
        print("plotting graph id")
        idfunction_x_points = x
        idfunction_y_points = []

        for i in idfunction_x_points:
            idfunction_y_points.append(functions.useFunction(i, id))

        label = "function (id = " + str(id) + ")"
        plt.plot(idfunction_x_points, idfunction_y_points, '--', color='green', zorder=4, label=label)

    x_points = []
    y_points = []
    for i in range(len(points)):
        x_points.append(points[i][0])
        y_points.append(points[i][1])
    plt.scatter(x_points, y_points, color='blue',zorder=3,label='points')
    plt.legend(loc='lower right')
    plt.show()