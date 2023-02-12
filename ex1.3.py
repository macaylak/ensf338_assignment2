# Implement a version of the code above that use memoization to improve performance
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