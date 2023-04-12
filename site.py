import math
import os
import random
import re
import sys

k = 0.4
a = 0.9


def first_function(args: []) -> float:
    return math.sin(args[0])


def second_function(args: []) -> float:
    return (args[0] * args[1]) / 2


def third_function(args: []) -> float:
    return math.tan(args[0] * args[1] + k) - pow(args[0], 2)


def fourth_function(args: []) -> float:
    return a * pow(args[0], 2) + 2 * pow(args[1], 2) - 1


def fifth_function(args: []) -> float:
    return pow(args[0], 2) + pow(args[1], 2) + pow(args[2], 2) - 1


def six_function(args: []) -> float:
    return 2 * pow(args[0], 2) + pow(args[1], 2) - 4 * args[2]


def seven_function(args: []) -> float:
    return 3 * pow(args[0], 2) - 4 * args[1] + pow(args[2], 2)


def default_function(args: []) -> float:
    return 0.0


# How to use this function:
# funcs = Result.get_functions(4)
# funcs[0](0.01)
def get_functions(n: int):
    if n == 1:
        return [first_function, second_function]
    elif n == 2:
        k = 0.4
        a = 0.9
        return [third_function, fourth_function]
    elif n == 3:
        k = 0
        a = 0.5
        return [fifth_function, six_function, seven_function]
    else:
        return [default_function]


#
# Complete the 'solve_by_fixed_point_iterations' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts following parameters:
#  1. INTEGER system_id
#  2. INTEGER number_of_unknowns
#  3. DOUBLE_ARRAY initial_approximations
#

def solve_by_fixed_point_iterations(system_id, number_of_unknowns, initial_approximations):
    MAX_ITERATIONS = 1000
    TOLERANCE = 1e-5

    funcs = get_functions(system_id)
    f = lambda args: [func(args) for func in funcs]

    iterations = 0
    error = 1
    x = initial_approximations

    while error > TOLERANCE and iterations < MAX_ITERATIONS:
        x_next = []
        for i in range(number_of_unknowns):
            g_i = lambda x_i: x[i] + funcs[i](x) * TOLERANCE
            x_next.append(g_i(x[i]))
        error = max([abs(x_next[i] - x[i]) for i in range(number_of_unknowns)])
        x = x_next
        iterations += 1

    if iterations == MAX_ITERATIONS:
        print("Достигнут предел итерации")

    return x


if __name__ == '__main__':
    system_id = int(input().strip())

    number_of_unknowns = int(input().strip())

    initial_approximations = []

    for _ in range(number_of_unknowns):
        initial_approximations_item = float(input().strip())
        initial_approximations.append(initial_approximations_item)

    result = solve_by_fixed_point_iterations(system_id, number_of_unknowns, initial_approximations)
    print(result)
    print('\n'.join(map(str, result)))
    print('\n')
