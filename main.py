import matplotlib.pyplot as plt
from funcs import *

ab = [-10, 10]
N = 50
for i in (1, 2, 4):
    h = (ab[1]-ab[0])/i*N
    x = []
    for j in range(i*N+1):
        x.append(ab[0]+j*h)
    delta1_left = []
    delta1_right = []
    delta1_center = []
    delta2 = []
    delta3 = []
    for j in range(i*N+1):
        delta1_left.append((f1_left(x[j], h) - y(x[j])) / f1_left(x[j], h))
        delta1_right.append((f1_right(x[j], h) - y(x[j])) / f1_right(x[j], h))
        delta1_center.append((f1_center(x[j], h) - y(x[j])) / f1_center(x[j], h))
        delta2.append((f2(x[j], h) - y(x[j])) / f2(x[j], h))
        delta3.append((f3(x[j], h) - y(x[j])) / f3(x[j], h))
    plt.subplot(3, 1, 1)
    plt.title(f"N = {i*N}")
    plt.plot(x, delta1_left, label='left')
    plt.plot(x, delta1_right, label='right')
    plt.plot(x, delta1_center, label='center')
    plt.subplot(3, 1, 2)
    plt.plot(x, delta2)
    plt.subplot(3, 1, 3)
    plt.plot(x, delta3)
    plt.show()
    plt.close()