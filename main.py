import bisection_method,tangent_method

if __name__ == '__main__':
    print("Выберите уравнение: \n"
          " 1: x^2 - 3 = 0\n"
          " 2: x^3 - 5x - 9\n")

    equation = int(input())
    print("Выберите метод решения:\n"
          "1: Метод деления пополам\n"
          "2: Метод касательных")
    method = int(input())
    if method == 1:
        bisection_method.bisection_solve(equation=equation)
    elif method == 2:
        tangent_method.tangent_method_solve(equation=equation)
    else:
        exit("Нет такого метода")
