# Time the original code and your improved version, for all integers between 0 and 35, and plot the results in one graph
import time
import matplotlib.pyplot as plt

def func(n):
	if n == 0 or n == 1:
		return n
	else:
		return func(n-1) + func(n-2)

def func2(n, cache={}):
    if n == 0 or n == 1:
        return n
    else:
        if n in cache:
            return cache[n]
        else:
            cache[n] = func(n-1) + func(n-2)
            return cache[n]
def time_func(func, n):
    start = time.time()
    func(n)
    end = time.time()
    return end - start

def time_func2(func, n):
    start = time.time()
    func(n)
    end = time.time()
    return end - start

def plot_time(func, func2, n):
    x = []
    y = []
    y2 = []
    for i in range(n):
        x.append(i)
        y.append(time_func(func, i))
        y2.append(time_func2(func2, i))
    plt.plot(x, y, label='func')
    plt.plot(x, y2, label='func2')
    plt.xlabel('n')
    plt.ylabel('time')
    plt.legend()
    plt.show()

plot_time(func, func2, 35)