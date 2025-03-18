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
  # Всего будет 8 графиков, столько же результатов функций мы и получаем в функции.
  # Делаем холст с 3 графиками. Первый график - оригинальная функция.
  # Второй график - Аналитическое решение
  # Третий график - Производные по формулам из файла
  # Объединяем, чтобы нормально отобразить этот график сверху остальных
  plt.subplot(2, 2, (1, 2))
  # Сначала строим оригинальную функцию
  plt.plot(x, fx, linestyle='solid', linewidth=2, c="black", label="y(x)")
  plt.grid(True)  # включаем сетку, удобно
  plt.ylabel('y(x)')  # обозначение оси ординат (y)
  plt.xlabel('x')  # обозначение оси абсцисс (x)
  plt.legend()
  plt.title('Оригинальная функция', loc="center", pad=10)  # заголовок со смещением влево
  # Первый график (аналитический)
  plt.subplot(2, 2, 3)
  # Теперь строим аналитическую первую производную
  plt.plot(x, analytic_fx1, linestyle='solid', linewidth=1, c="red", label="y'(x)")
  # Теперь строим аналитическую вторую производную
  plt.plot(x, analytic_fx2, linestyle='solid', linewidth=1, c="green", label="y''(x)")
  # Теперь строим аналитическую третью производную
  plt.plot(x, analytic_fx3, linestyle='solid', linewidth=1, c="blue", label="y'''(x)")
  plt.ylabel('y(x)')  # обозначение оси ординат (y)
  plt.xlabel('x')  # обозначение оси абсцисс (x)
  plt.title('Аналитическое решение', loc="left", pad=10)  # заголовок со смещением влево
  plt.grid(True)
  plt.legend()
  # Второй график (производные)
  plt.subplot(2, 2, 4)
  # Строим график первой производной
  plt.plot(x, fx1, linestyle='solid', linewidth=1, c="red", label="f'(x)")
  # Строим график первой производной второго порядка точности
  plt.plot(x, fx1v2, linestyle='dashdot', linewidth=1, marker=".", c="#ff9628", label="f'(x) (второго порядка точности)")
  # Строим график третьей производной
  plt.plot(x, fx2, linestyle='solid', linewidth=1, c="green", label="f''(x)")
  # Строим график четвёртой производной
  plt.plot(x, fx3, linestyle='solid', linewidth=1, c="blue", label="f'''(x)")
  plt.ylabel('y(x)')  # обозначение оси ординат (y)
  plt.xlabel('x')  # обозначение оси абсцисс (x)
  plt.title('Решение производных', loc="right", pad=10)  # заголовок со смещением вправо
  plt.grid(True)
  plt.legend()
  # plt.show()
  if save_to_file:
    plt.savefig(f"result/{result_category}_{result_name}", dpi=1200)

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
    for i in range(n+1):
        fx.append(y(x[i]))
        analytic_fx1.append(a_y1(x[i]))
        analytic_fx2.append(a_y2(x[i]))
        analytic_fx3.append(a_y3(x[i]))
        fx1.append(f1(x[i], h))
        fx1v2.append(f1_v2(x[i], h))
        fx2.append(f2(x[i], h))
        fx3.append(f3(x[i], h))
    print(x)
    print(fx)
    print(analytic_fx1)
    print(analytic_fx2)
    print(analytic_fx3)
    return x, fx, analytic_fx1, analytic_fx2, analytic_fx3, fx1, fx1v2, fx2, fx3

graph(
f_diff(20, [-10, 10]), True, "[-10, 10]", "n200"
)
graph(
f_diff(200, [-10, 10]), True, "[-10, 10]", "n200"
)
graph(
f_diff(2000, [-10, 10]), True, "[-10, 10]", "n2000"
)
graph(
f_diff(200, [-100, 100]), True, "[-100, 100]", "n200"
)
graph(
f_diff(2000, [-100, 100]), True, "[-10, 10]", "n2000"
)
graph(
f_diff(20000, [-100, 100]), True, "[-10, 10]", "n20000"
)