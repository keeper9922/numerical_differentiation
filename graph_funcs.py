import matplotlib.pyplot as plt
from funcs import *


def find_x(divisions: int, section: list[int | float]):
    a = section[0]
    b = section[1]
    h = (b - a) / divisions
    x = []
    for i in range(divisions + 1):
        x.append(a + i * h)
    return x, h


def f_diff(divisions: int, section: list[int | float]):
    x, h = find_x(divisions, section)
    fx = []
    analytic_fx1 = []
    analytic_fx2 = []
    analytic_fx3 = []
    fx1_left = []
    fx1_right = []
    fx1_center = []
    fx2 = []
    fx3 = []
    for i in range(divisions+1):
        fx.append(y(x[i]))
        analytic_fx1.append(a_y1(x[i]))
        analytic_fx2.append(a_y2(x[i]))
        analytic_fx3.append(a_y3(x[i]))
        fx1_left.append(f1_left(x[i], h))
        fx1_right.append(f1_right(x[i], h))
        fx1_center.append(f1_center(x[i], h))
        fx2.append(f2(x[i], h))
        fx3.append(f3(x[i], h))
    # print(x)
    # print(fx)
    # print(analytic_fx1)
    # print(analytic_fx2)
    # print(analytic_fx3)
    return x, fx, analytic_fx1, analytic_fx2, analytic_fx3, fx1_left, fx1_right, fx1_center, fx2, fx3

def f_diff_delta(divisions: int, section: list[int | float]):
    x, h = find_x(divisions, section)
    fx = []
    delta1_left = []
    delta1_right = []
    delta1_center = []
    delta2 = []
    delta3 = []
    for i in range(divisions + 1):
        fx.append(y(x[i]))
        delta1_left.append(
            delta(f1_left, x[i], h)
        )
        delta1_right.append(
            delta(f1_right, x[i], h)
        )
        delta1_center.append(
            delta(f1_center, x[i], h)
        )
        delta2.append(
            delta(f2, x[i], h)
        )
        delta3.append(
            delta(f3, x[i], h)
        )
    return x, fx, divisions, delta1_left, delta1_right, delta1_center, delta2, delta3

def graph_delta(function_result: tuple[
    list[float | int], list[float | int], int, list[float | int], list[float | int], list[float | int], list[
        float | int], list[float | int]],
          save_to_file: bool = False,
          result_category: str = "result",
          result_name: str = "none"):
    """
    Вывод графиков погрешностей для каждой ф-ии.
    :param function_result: Результат в виде кортежа из 9 списков типа int или float. Первый список - сам x; 2, 3, 4 - аналитическое решение производных; 5, 6, 7, 8 - сами производные (где 6 - первая производная второго порядка точности)
    :param save_to_file: Сохранять ли в файл построенные графики?
    :param result_category: Как мы объединяем графики для разных N
    :param result_name: Название файла
    :return:
    """
    x, fx, N, delta1_left, delta1_right, delta1_center, delta2, delta3 = function_result

    plt.subplot(4, 2, (1, 2))
    plt.plot(x, fx)
    plt.subplot(4, 2, 3)
    # plt.title("f'(x)")
    plt.title("left")
    plt.plot(x, delta1_left, label=f"N = {N}")
    plt.legend()
    plt.subplot(4, 2, 4)
    plt.title("right")
    plt.plot(x, delta1_right, label=f"N = {N}")
    plt.legend()
    plt.subplot(4, 2, (5, 6))
    plt.title("center")
    plt.plot(x, delta1_center, label=f"N = {N}")
    plt.legend()
    plt.subplot(4, 2, 7)
    # plt.title("f''(x)")
    plt.plot(x, delta2, label=f"N={N}")
    plt.legend()
    plt.subplot(4, 2, 8)
    # plt.title("f'''(x)")
    plt.plot(x, delta3, label=f"N={N}")
    plt.legend()

    if save_to_file:
        plt.savefig(f"result/{result_category}_{result_name}", dpi=1200)
        plt.close()

def graph(divisions: int, function_result: tuple[list[int | float], list[int | float], list[int | float], list[int | float], list[int | float], list[int | float], list[int | float], list[int | float], list[int | float], list[int | float]],
            save_to_file: bool = False,
            result_category: str = "result",
            result_name: str = "none"):
    """
    Вывод всех посчитанных графиков для выбранных значений.
    :param divisions: Кол-во разбиений
    :param function_result: Результат в виде кортежа из 9 списков типа int или float. Первый список - сам x; 2, 3, 4 - аналитическое решение производных; 5, 6, 7, 8 - сами производные (где 6 - первая производная второго порядка точности)
    :param save_to_file: Сохранять ли в файл построенные графики?
    :param result_category: Как мы объединяем графики для разных N
    :param result_name: Название файла
    :return:
    """
    (x,
     fx,
     analytic_fx1,
     analytic_fx2,
     analytic_fx3,
     fx1_left,
     fx1_right,
     fx1_center,
     fx2,
     fx3) = function_result
    # Всего будет 6 графиков, столько же результатов функций мы и получаем в функции.
    # Делаем холст с 3 графиками. Первый график - оригинальная функция.
    # Второй график - Аналитическая и численная первая производная
    # Третий график - Аналитическая и численная первая с вторым порядком точности производная
    # Четвёртый график - Аналитическая и численная вторая производная
    # Пятый график - Аналитическая и численная третья производная
    # Объединяем, чтобы нормально отобразить этот график сверху остальных
    plt.subplot(3, 2, (1, 2))
    # Сначала строим оригинальную функцию
    plt.plot(x, fx, linestyle='solid', linewidth=2, c="black", label="y(x)")
    plt.grid(True)  # включаем сетку, удобно
    plt.ylabel('y(x)')  # обозначение оси ординат (y)
    plt.xlabel('x')  # обозначение оси абсцисс (x)
    plt.legend()
    plt.title(f'N={divisions}', loc="center", pad=10)  # заголовок со смещением влево
    # Первый и второй график (левая, правая, центральная, аналитическая)
    plt.subplot(3, 2, (3, 4))
    # Строим график первой производной
    plt.plot(x, fx1_left, linestyle='solid', linewidth=1, c="green", marker='x', markersize=1, label="Левая")
    plt.plot(x, fx1_right, linestyle='solid', linewidth=1, c="blue", marker='x', markersize=1, label="Правая")
    plt.plot(x, fx1_center, linestyle='solid', linewidth=1, c="red", marker='x', markersize=1, label="Центральная")
    # Теперь строим аналитическую первую производную
    plt.plot(x, analytic_fx1, linestyle='solid', linewidth=1, c="black", marker='x', markersize=3, label="Аналитическая")
    plt.ylabel('y')  # обозначение оси ординат (y)
    plt.xlabel('x')  # обозначение оси абсцисс (x)
    plt.title('Первая производная', loc="left", pad=5)  # заголовок со смещением влево
    plt.grid(True)
    plt.legend()
    # Третий график (производные)
    plt.subplot(3, 2, 5)
    # Строим график второй производной
    plt.plot(x, fx2, linestyle='solid', linewidth=1, c="red", marker='.', markersize=3,  label="Численная")
    # Теперь строим аналитическую вторую производную
    plt.plot(x, analytic_fx2, linestyle='solid', linewidth=1, c="black", label="Аналитическая")
    plt.ylabel('y')  # обозначение оси ординат (y)
    plt.xlabel('x')  # обозначение оси абсцисс (x)
    plt.title('Вторая производная', loc="left", pad=5)  # заголовок со смещением влево
    plt.grid(True)
    plt.legend()
    # Четвёртый график (производные)
    plt.subplot(3, 2, 6)
    # Строим график второй производной
    plt.plot(x, fx3, linestyle='solid', linewidth=1, c="red", marker='.', markersize=3,  label="Численная")
    # Теперь строим аналитическую вторую производную
    plt.plot(x, analytic_fx3, linestyle='solid', linewidth=1, c="black", label="Аналитическая")
    plt.ylabel('y')  # обозначение оси ординат (y)
    plt.xlabel('x')  # обозначение оси абсцисс (x)
    plt.title('Третья производная', loc="right", pad=5)  # заголовок со смещением влево
    plt.grid(True)
    plt.legend()
    # plt.show()
    if save_to_file:
      plt.savefig(f"result/{result_category}_{result_name}", dpi=1200)
      plt.close()
    else:
      plt.show()
