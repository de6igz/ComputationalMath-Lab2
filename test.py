import numpy as np


def newton_method(f, df, x0, tol=1e-6, max_iter=100):
    """Решение нелинейного уравнения методом Ньютона.

    Параметры:
        f: функция, для которой необходимо решить уравнение.
        df: производная функции f.
        x0: начальное приближение.
        tol: допустимая погрешность.
        max_iter: максимальное количество итераций.

    Возвращает кортеж, содержащий:
        x: приближенное решение уравнения.
        err: массив значений погрешности на каждом шаге.
        x_history: массив значений переменной x на каждом шаге.
    """
    x = x0
    err = []
    x_history = []

    for i in range(max_iter):
        x_history.append(x)

        fx = f(x)
        dfx = df(x)

        x_new = x - fx / dfx
        err.append(np.abs(x_new - x))
        print(f'Погрешность: {abs(x_new - x)}')
        print(f'Значение x: {x}')

        if err[-1] < tol:
            break

        x = x_new

    return x, err, x_history


def f(x):
    return x ** 2 - 2


def df(x):
    return 2 * x


x0 = 1.0
solution, error, x_history = newton_method(f, df, x0)
print("Решение: x = {}".format(solution))
print("Значения погрешности: {}".format(error))
print("Значения x на каждом шаге: {}".format(x_history))
