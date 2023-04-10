from bisection_method import read_interval
import numpy as np


def eq1(x):
    return x ** 2 - 3


def eq1_derivative(x):
    return 2 * x


def eq2(x):
    return x ** 3 - 2 * x - 5


def eq2_derivative(x):
    return 3 * x ** 2 - 2


def tangent_method(equation, equation_derivative, x0, tol=0.01, max_iter=100):
    """Решение нелинейного уравнения методом Ньютона.

    Параметры:
        equation: функция, для которой необходимо решить уравнение.
        equation_derivative: производная функции f.
        x0: начальное приближение.
        tol: допустимая погрешность.
        max_iter: максимальное количество итераций.

    Возвращает следующие значения:
        x: приближенное решение уравнения.
        err: массив значений погрешности на каждом шаге.
    """
    x = x0
    err = []
    counter = 0

    for i in range(max_iter):
        counter += 1
        fx = equation(x)
        dfx = equation_derivative(x)

        x_new = x - fx / dfx
        err.append(np.abs(x_new - x))
        print(f'Номер попытки: {i+1}')
        print(f'Погрешность: {abs(x_new - x)}')
        print(f'Значение x: {x}')
        print("----------------------")

        if err[-1] < tol:
            break

        x = x_new

    return x, counter


def tangent_method_solve(equation):
    print("Введите метод ввода границ:\n"
          "1: Консоль\n"
          "2: Файл")
    interval_method = int(input())
    if interval_method == 1:
        print("Введите первую границу интервала")
        a = int(input())
        print("Введите вторую границу интервала")
        b = int(input())
    elif interval_method == 2:
        a, b = read_interval()
    else:
        exit("Нет такого метода")
    if equation == 1:
        root, iterations = tangent_method(x0=b, equation=eq1, equation_derivative=eq1_derivative)
        print("Корень уравнения: ", root)
        print("Количество итераций: ", iterations)
    elif equation == 2:
        root, iterations = tangent_method(x0=b, equation=eq2, equation_derivative=eq2_derivative)
        print("Корень уравнения: ", root)
        print("Количество итераций: ", iterations)
