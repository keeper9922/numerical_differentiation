import matplotlib.pyplot as plt
from funcs import *

def graph(function_result: tuple[
    list[float | int], list[float | int], float | int, list[float | int], list[float | int], list[float | int], list[
        float | int], list[float | int]],
          save_to_file: bool = False,
          result_category: str = "result",
          result_name: str = "none"):
    """
    Вывод всех посчитанных графиков для выбранных значений.
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


def f_diff(divisions: int, section: list):
    a = section[0]
    b = section[1]
    h = (b - a) / divisions
    x = []
    for i in range(divisions + 1):
        x.append(a + i * h)
    fx = []
    delta1_left = []
    delta1_right = []
    delta1_center = []
    delta2 = []
    delta3 = []
    for i in range(divisions + 1):
        fx.append(y(x[i]))
        delta1_left.append((f1_left(x[i], h) - y(x[i])) / f1_left(x[i], h))
        delta1_right.append((f1_right(x[i], h) - y(x[i])) / f1_right(x[i], h))
        delta1_center.append((f1_center(x[i], h) - y(x[i])) / f1_center(x[i], h))
        delta2.append((f2(x[i], h) - y(x[i])) / f2(x[i], h))
        delta3.append((f3(x[i], h) - y(x[i])) / f3(x[i], h))
    # print(x)
    # print(fx)
    # print(analytic_fx1)
    # print(analytic_fx2)
    # print(analytic_fx3)
    return x, fx, divisions, delta1_left, delta1_right, delta1_center, delta2, delta3