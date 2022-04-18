import functions

def print_welcome():
    print("/--------------------------\\")
    print("Lagrange polynomial calculator")
    print("Type \"help\" to get help, type \"quit\" to quit.")
    print_divider()
    return

def print_divider():
    print("--------------------------")


def print_help():
    print_divider()
    print(
        "USER MANUAL\n"
        "[x] [y]   -   add a point (two numbers separated by space);\n"
        "calculate [x]  -   calculate function value on this x;\n"
        "graph [id]   -   graph function with id from list below:")
    print("   [0] no additional graph of function")
    print_functions()
    print(
        #"0: remove the graph\n"
        "clear   -    delete all points;\n"
        "generate   -   generate the polynomial;\n"
        "help   -   display this message;\n"
        "quit   -   quit")
    print_divider()

def print_functions():
    for i in range(1,4):
        print("   " + functions.print_function(i))
