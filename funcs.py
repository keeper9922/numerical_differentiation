import numpy as np
# функции:
def y(x) -> float:
    """
    Оригинальная функция
    :param x: Входное значение (точка на отрезке)
    :return:
    """
    try:
        return (x + 7) / (6 * (x*x + 2*x + 7)**(1/2))
    except:
        return np.nan

def a_y1(x) -> float:
    """
    Аналитическое решение первой производной
    :param x: Входное значение (точка на отрезке)
    :return:
    """
    try:
        return - (x / ((x*x + 2*x + 7)**(3/2))) # -((x*((x*x) + 2*x + 7)**(1/2)) / ((x**4)+4*(x**3)+18*(x*x)+28*x+43))
    except:
        return np.nan


def a_y2(x) -> float:
    """
    Аналитическое решение второй производной
    :param x: Входное значение (точка на отрезке)
    :return:
    """
    try:
        return (2*(x**2) + x - 7) / ((x**2 + 2*x + 7)**(5/2))
    except:
        return np.nan

def a_y3(x) -> float:
    """
    Аналитическое решение третьей производной
    :param x: Входное значение (точка на отрезке)
    :return:
    """
    try:
        return - ((6*(x**3 + x**2 - 10*x - 7)) / ((x**2 + 2*x + 7)**(7/2)))
    except:
        return np.nan

# производные
def f1_left(x, h) -> float:
    """
    Решение первой производной
    :param x: Входное значение (точка на отрезке)
    :param h: Размер разбиения (чем меньше - тем выше точность)
    :return:
    """
    try:
        return (y(x+h) - y(x))/h
    except:
        return np.nan

def f1_right(x, h) -> float:
    """
    Решение первой производной
    :param x: Входное значение (точка на отрезке)
    :param h: Размер разбиения (чем меньше - тем выше точность)
    :return:
    """
    try:
        return (y(x) - y(x-h))/h
    except:
        return np.nan

def f1_center(x, h) -> float:
    """
    Решение первой производной второго порядка точности
    :param x: Входное значение (точка на отрезке)
    :param h: Размер разбиения (чем меньше - тем выше точность)
    :return:
    """
    try:
        return (y(x+h) - y(x-h))/(2*h)
    except:
        return np.nan

def f2(x, h) -> float:
    """
    Решение второй производной
    :param x: Входное значение (точка на отрезке)
    :param h: Размер разбиения (чем меньше - тем выше точность)
    :return:
    """
    try:
        return (y(x+h) - 2*y(x) + y(x-h))/(h*h)
    except:
        return np.nan

def f3(x, h) -> float:
    """
    Решение третьей производной
    :param x: Входное значение (точка на отрезке)
    :param h: Размер разбиения (чем меньше - тем выше точность)
    :return:
    """
    try:
        return (y(x+2*h) - 2*y(x+h) + 2*y(x-h) - y(x-2*h))/(2*(h**3))
    except:
        return np.nan

def delta(func, x, h):
    """
    Функция для вычисления погрешности.
    :param func:
    :param x:
    :param h:
    :return:
    """
    try:
        return abs(func(x, h) - y(x) / func(x, h))
    except:
        return np.nan
