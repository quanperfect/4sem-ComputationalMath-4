import math

#todo
def function_to_string(id):
    if id == 1:
        return "[1] x^2"
    if id == 2:
        return "[2] 2*x+4"
    if id == 3:
        return "[3] sin(x)"

    return "function with this id does not exist"

def useFunction(x, id):
    if id == 1:
        return x**2
    if id == 2:
        return 2*x+4
    if id == 3:
        return math.sin(x)
    return 0