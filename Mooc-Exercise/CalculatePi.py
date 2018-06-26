#使用蒙特卡洛方法计算圆周率

from random import random
from time import perf_counter

DARTS = 1000*1000
hits = 0.0
start = perf_counter()


for i in range(1, DARTS+1):
    x, y = random(), random()
    dist = pow(x**2 + y**2, 0.5)
    if dist <= 1.0:
        hits = hits+1

pi = 4*(hits/DARTS)
print("圆周率的值为：{}".format(pi))
print("运行的时间是：{}".format(perf_counter() - start))
