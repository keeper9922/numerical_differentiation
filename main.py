from graph_funcs import *
sec = [-100, 100] # отрезок
n = (abs(sec[0]) + abs(sec[1]))*10 # кол-во разбиений
graph(f_diff(n, sec)) # графики n
graph(f_diff(2*n, sec)) # графики 2n
graph(f_diff(4*n, sec)) # графики 4n
plt.show() # показываем итоговый график