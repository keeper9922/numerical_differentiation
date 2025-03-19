import matplotlib.pyplot as plt
from funcs import *



def graph(function_result: tuple[list[int | float], list[int | float], list[int | float], list[int | float], list[int | float], list[int | float], list[int | float], list[int | float], list[int | float]],
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
  x, fx, analytic_fx1, analytic_fx2, analytic_fx3, fx1, fx1v2, fx2, fx3 = function_result
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
  plt.title('Оригинальная функция', loc="center", pad=10)  # заголовок со смещением влево
  # Первый график (аналитический)
  plt.subplot(3, 2, 3)
  # Строим график первой производной
  plt.plot(x, fx1, linestyle='solid', linewidth=1, c="red", marker='x', markersize=3, label="Численная")
  # Теперь строим аналитическую первую производную
  plt.plot(x, analytic_fx1, linestyle='solid', linewidth=1, c="blue", label="Аналитическая")
  plt.ylabel('y')  # обозначение оси ординат (y)
  plt.xlabel('x')  # обозначение оси абсцисс (x)
  plt.title('Первая производная', loc="left", pad=5)  # заголовок со смещением влево
  plt.grid(True)
  plt.legend()
  # Второй график (производные)
  plt.subplot(3, 2, 4)
  # Строим график первой производной второго порядка точности
  plt.plot(x, fx1v2, linestyle='solid', linewidth=1, c="red", marker='.', markersize=3, label="Численная")
  # Теперь строим аналитическую первую производную
  plt.plot(x, analytic_fx1, linestyle='solid', linewidth=1, c="blue", label="Аналитическая")
  plt.ylabel('y')  # обозначение оси ординат (y)
  plt.xlabel('x')  # обозначение оси абсцисс (x)
  plt.title('Первая производная (второй порядок точности)', loc="right", pad=5)  # заголовок со смещением влево
  plt.grid(True)
  plt.legend()
  # Третий график (производные)
  plt.subplot(3, 2, 5)
  # Строим график второй производной
  plt.plot(x, fx2, linestyle='solid', linewidth=1, c="red", marker='.', markersize=3,  label="Численная")
  # Теперь строим аналитическую вторую производную
  plt.plot(x, analytic_fx2, linestyle='solid', linewidth=1, c="blue", label="Аналитическая")
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
  plt.plot(x, analytic_fx3, linestyle='solid', linewidth=1, c="blue", label="Аналитическая")
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

def f_diff(n: int, section: list):
    a = section[0]
    b = section[1]
    h = (b-a)/n
    x = []
    for i in range(n+1):
        x.append(a+i*h)
    fx = []
    analytic_fx1 = []
    analytic_fx2 = []
    analytic_fx3 = []
    fx1 = []
    fx1v2 = []
    fx2 = []
    fx3 = []
    delta1 = []
    delta2 = []
    delta3 = []
    for i in range(n+1):
        fx.append(y(x[i]))
        analytic_fx1.append(a_y1(x[i]))
        analytic_fx2.append(a_y2(x[i]))
        analytic_fx3.append(a_y3(x[i]))
        fx1.append(f1(x[i], h))
        fx1v2.append(f1_v2(x[i], h))
        fx2.append(f2(x[i], h))
        fx3.append(f3(x[i], h))
        delta1.append((f1(x[i], h) - y(x[i]))/f1(x[i], h))
        delta2.append((f2(x[i], h) - y(x[i]))/f2(x[i], h))
        delta3.append((f3(x[i], h) - y(x[i]))/f3(x[i], h))
    # print(x)
    # print(fx)
    # print(analytic_fx1)
    # print(analytic_fx2)
    # print(analytic_fx3)
    # print(delta1[0] - delta1[1], delta1[1] - delta1[2], delta1[2] - delta1[3], delta1[3] - delta1[4], delta1[4] - delta1[5])
    # print(delta2[0] - delta2[1], delta2[1] - delta2[2], delta2[2] - delta2[3], delta2[3] - delta2[4], delta2[4] - delta2[5])
    # print(delta3[0] - delta3[1], delta3[1] - delta3[2], delta3[2] - delta3[3], delta3[3] - delta3[4], delta3[4] - delta3[5])
    return x, fx, analytic_fx1, analytic_fx2, analytic_fx3, fx1, fx1v2, fx2, fx3

sec = [-100, 100]
n = abs(sec[0]) + abs(sec[1])
graph(
    f_diff(10000, sec)
)
# graph(
#     f_diff(2*10000, sec)
# )
# graph(
#     f_diff(4*10000, sec)
# )