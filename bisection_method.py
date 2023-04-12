def bisection_method(f, a, b, tol=0.01, max_iter=100):
    """
    Решение нелинейного уравнения методом деления пополам.

    Аргументы:
    f - функция одной переменной для которой нужно решить уравнение
    a, b - начальные интервальные границы, где f(a) и f(b) имеют разные знаки
    tol - требуемая точность решения
    max_iter - максимальное количество итераций

    Возвращает корень уравнения и количество итераций.
    """

    # проверяем, что f(a) и f(b)
    if f(a) * f(b) >= 0:
        raise ValueError("Условие f(a) * f(b) < 0 не выполняется")

    # инициализируем переменные
    iteration = 0
    while iteration < max_iter:
        iteration += 1
        print("______________________________")
        print(f"Номер шага: {iteration}")

        # находим середину интервала
        c = (a + b) / 2
        print(f"Погрешность: {abs(b - a) / 2}")
        print(f"Значение x: {c}")
        # print(f"_____________________________")
        # проверяем, является ли середина корнем или достигли заданной точности
        if abs(f(c)) < tol or abs(b - a) / 2 < tol:
            return c, iteration

        # выбираем новый интервал для следующей итерации
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

    # если не достигли заданной точности за максимальное число итераций, выбрасываем ошибку
    raise ValueError("Не удалось найти корень за максимальное число итераций.")


def f(x):
    return x * x - 3


def solve(f, a, b):
    root, iterations = bisection_method(f, a, b)
    print("\nКорень уравнения: ", root)
    print("Количество итераций: ", iterations)


def read_interval():
    a: int
    b: int
    with open('input.txt') as f:
        a = int(f.read(1))
        b = int(f.read(2))
    return a, b


def bisection_solve(equation):
    def eq1(x):
        return x ** 2 - 3

    def eq2(x):
        return x ** 3 - 5 * x - 9

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
        solve(f=eq1, a=a, b=b)
    elif equation == 2:
        solve(f=eq2, a=a, b=b)
