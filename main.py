import matplotlib.pyplot as plt
from funcs import *



def graph(function_result: tuple[list[float | int], list[float | int], list[float | int], list[float | int], list[float | int]],
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
  x, fx, fx_left, fx_right, fx_center = function_result

  plt.subplot(2, 1, 1)
  plt.plot(x, fx)
  plt.subplot(2, 1, 2)
  plt.plot(x, fx_left, label="left")
  plt.plot(x, fx_right, label="right")
  plt.plot(x, fx_center, label="center")
  plt.legend()

  if save_to_file:
    plt.savefig(f"result/{result_category}_{result_name}", dpi=1200)
    plt.close()
  else:
    plt.show()

def f_diff(divisions: int, section: list):
    a = section[0]
    b = section[1]
    h = (b-a)/divisions
    x = []
    for i in range(divisions+1):
        x.append(a+i*h)
    fx = []
    delta_left = []
    delta_right = []
    delta_center = []
    for i in range(divisions+1):
        fx.append(y(x[i]))
        delta_left.append((f1_left(x[i], h) - y(x[i])) / f1_left(x[i], h))
        delta_right.append((f1_right(x[i], h) - y(x[i])) / f1_right(x[i], h))
        delta_center.append((f1_center(x[i], h) - y(x[i])) / f1_center(x[i], h))
    # print(x)
    # print(fx)
    # print(analytic_fx1)
    # print(analytic_fx2)
    # print(analytic_fx3)
    return x, fx, delta_left, delta_right, delta_center

sec = [-10, 10]
n = 50 # abs(sec[0]) + abs(sec[1])
graph(
    f_diff(n, sec)
)
graph(
    f_diff(2*n, sec)
)
graph(
    f_diff(4*n, sec)
)
# graph(
#     f_diff(2*10000, sec)
# )
# graph(
#     f_diff(4*10000, sec)
# )