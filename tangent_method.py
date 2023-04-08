from bisection_method import read_interval


def eq1(x):
    return x ** 2 - 3


def eq1_derivative(x):
    return 2 * x


def eq2(x):
    return x ** 3 - 2 * x - 5


def eq2_derivative(x):
    return 3 * x ** 2 - 2


def tangent_method(x0, tol=1e-6, max_iter=100, equation=None, equation_derivative=None):
    """Решение нелинейного уравнения методом касательных"""
    xn = x0
    for n in range(max_iter):
        fxn = equation(xn)
        f_deriv_xn = equation_derivative(xn)
        if abs(fxn) < tol:
            print(f"Решение найдено после {n} итераций: {xn}")
            return xn
        xn = xn - fxn / f_deriv_xn
        print(f'Номер шага: {n}')
    print("Решение не найдено")
    return None


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
        tangent_method(x0=b, equation=eq1, equation_derivative=eq1_derivative)
    elif equation == 2:
        tangent_method(x0=b, equation=eq2, equation_derivative=eq2_derivative)
