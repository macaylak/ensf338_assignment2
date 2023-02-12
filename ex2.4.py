# Change the code – if possible – to improve its performance on the input given in point 2.
import timeit
import matplotlib.pyplot as plt
import sys
import json
import random
sys.setrecursionlimit(20000)


def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)


def func2(array, start, end):
    # Choose a random pivot element
    pivot_index = random.randint(start, end)
    array[start], array[pivot_index] = array[pivot_index], array[start]
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


def test_sort(arr):
    return timeit.timeit(lambda: func1(arr, 0, len(arr) - 1), number=1)


def main():
    with open("file.json", "r") as f:
        for line in f:
            arrays = json.loads(line)
            results = []
            for array in arrays:
                results.append(test_sort(array))
                
            plt.plot(results)
    plt.show()


if __name__ == "__main__":
    main()
