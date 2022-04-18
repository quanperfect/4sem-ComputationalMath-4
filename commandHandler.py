import functions
import graph
import lagrange as lagrange
import printer as printer

def work():
    printer.print_welcome()
    point_list = []
    coef_list = []
    id = 0
    isLagrangeGenerated = 0

    while 1:
        inp = input()

        input_split = inp.split()

        if (len(input_split) == 2):
            if (check_if_number(input_split[0]) and check_if_number(input_split[1])):
                x_y = [float(input_split[0]), float(input_split[1])]
                point_list.append(x_y)
                isLagrangeGenerated = 0
            elif (input_split[0] == "calculate" and check_if_number(input_split[1])):
                #calculate y for inputted x
                if (isLagrangeGenerated):
                    value = lagrange_polynom(float(input_split[1]))
                    print("f(" + input_split[1] + ") = {:.4f}".format(value))
                else:
                    print("You need to type \"generate\" to generate polynom.")

            elif (input_split[0] == "graph" and input_split[1].isnumeric()):
                #graph with id
                id = int(input_split[1])
                if (id == 0):
                    print("You've selected to not graph a function.")
                print("You've selected to graph a function: " + functions.function_to_string(id))

        elif (len(input_split) == 1):
            if (input_split[0] == "generate"):
                if (len(point_list) >= 2):
                    isLagrangeGenerated = 1
                    lagrange_polynom = lagrange.create_Lagrange_polynomial(point_list)
                    print("Lagrange polynom generated.")
                else:
                    isLagrangeGenerated = 0
                    print("Too few points for generation, at least 2 needed.")
            elif (input_split[0] == "clear"):
                isLagrangeGenerated = 0
                point_list = []
                print("List of points cleared.")
            elif (input_split[0] == "show_graph"):
                if (isLagrangeGenerated):
                    print("Graph is opened in new window. Close graph for further work.")
                    graph.plot(lagrange_polynom, point_list, id)
                    print("Graph closed, waiting for further commands.")
                else:
                    print("Polynom is not generated, type \"generate\" first.")
            elif (input_split[0] == "quit"):
                print("Me quit, okay...")
                exit(0)
            elif (input_split[0] == "help"):
                printer.print_help()
            else:
                print("Command does not exist.")


def check_if_number(input: str):
    input = input.replace('.','',1)
    input = input.replace('-','',1)

    if (input.isnumeric()):
        return 1
    return 0
