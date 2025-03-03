import matplotlib.pyplot as plt


def graph(function_result: tuple[list[int | float],list[int | float],list[int | float],list[int | float],list[int | float]],
            save_to_file: bool = False,
            result_folder: str = "result",
            result_name: str = "none"):
  x, y1, y1_2, y2, y3 = function_result
  # plt.plot(x, y, linestyle='--', marker='o', c="red", label=func_name)
  plt.plot(x, y1, linestyle='--', linewidth=0.9, c="green", markersize=3, label="y1")
  plt.plot(x, y1_2, linestyle='--', linewidth=0.7, c="red", markersize=2, label="y1_2")
  plt.plot(x, y2, linestyle='--', linewidth=0.6, c="blue", markersize=1, label="y2")
  plt.plot(x, y3, linestyle='--', linewidth=0.5, c="purple", markersize=1, marker="o", label="y3")
  plt.xlabel('x')
  plt.ylabel('f(x)')
  plt.title(f'Численное дифференцирование')
  plt.grid(True)
  plt.legend()
  if save_to_file:
    plt.savefig(f"{result_folder}/{result_name}", dpi=300)
  plt.show()

def f(x):
    return (1 + x*x) / (2 * (1 + 2 * x*x)**1/2)
    # return (x + 7) / 6 * (x*x + 2*x + 7)**1/2

def f_diff(n: int, section: list, f):
    a = section[0]
    b = section[1]
    h = (b-a)/n
    x = []
    for i in range(n):
        x.append(a+i*h)
    y1 = []
    y1_2 = []
    y2 = []
    y3 = []
    for i in range(n):
        y1.append( (f(x[i]+h) - f(x[i])) / h )
        y1_2.append( (f(x[i]+h) - f(x[i]-h)) / 2*h )
        y2.append( (f(x[i]+h) - 2*f(x[i]) + f(x[i]-h)) / h*h )
        y3.append( (f(x[i]+2*h) - 2*f(x[i]+h) + 2*f(x[i]-h) - f(x[i]-2*h)) / 2*h*h*h )
    return x, y1, y1_2, y2, y3

graph(f_diff(10000, [1, 10000], f))
