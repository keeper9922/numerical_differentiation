from graph_funcs import *
sec = [-100, 100] # отрезок
n = 50
# n = (abs(sec[0]) + abs(sec[1]))*10 # Кол-во разбиений (то есть для нашего sec это будет n=2000)
print("N =", n)
graph(n, f_diff(n, sec)) # графики n
graph(2*n, f_diff(2*n, sec)) # графики 2n
graph(4*n, f_diff(4*n, sec)) # графики 4n
# input("Press \"ENTER\" to continue...")
graph_delta(f_diff_delta(n, sec)) # графики n
graph_delta(f_diff_delta(2*n, sec)) # графики 2n
graph_delta(f_diff_delta(4*n, sec)) # графики 4n
plt.show() # показываем итоговый график погрешностей