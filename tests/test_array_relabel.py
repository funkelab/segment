import segment
import numpy as np

if __name__ == "__main__":

    print()
    a = np.array([0, 1, 2, 3, 4, 5])
    print(a)
    old = np.array([2, 3])
    new = np.array([20, 30])
    b = segment.arrays.replace_values(a, old, new)
    print(a)
    print(b)
    print(segment.arrays.relabel(b))

    print()
    a += 100
    print(a)
    old = np.array([2, 3, 102, 103])
    new = np.array([20, 30, 2, 3])
    b = segment.arrays.replace_values(a, old, new)
    print(a)
    print(b)
    print(segment.arrays.relabel(b))

    print()
    a = np.array([1e6, 1e7], dtype=np.uint64)
    print(a)
    old = np.array([1e6], dtype=np.uint64)
    new = np.array([1], dtype=np.uint64)
    b = segment.arrays.replace_values(a, old, new)
    print(a)
    print(b)
    print(segment.arrays.relabel(b))

    print()
    a = np.array([0, 1e6, 1e7], dtype=np.uint64)
    print(a)
    old = np.array([1e6], dtype=np.uint64)
    new = np.array([1], dtype=np.uint64)
    b = segment.arrays.replace_values(a, old, new)
    print(a)
    print(b)
    print(segment.arrays.relabel(b))

    print()
    print("Inplace replacement:")

    print()
    a = np.array([0, 1, 2, 3, 4, 5])
    print(a)
    old = np.array([2, 3])
    new = np.array([20, 30])
    b = segment.arrays.replace_values(a, old, new, inplace=True)
    print(a)
    print(b)
    print(segment.arrays.relabel(b, inplace=True))

    print()
    a = np.array([0, 1, 2, 3, 4, 5]) + 100
    print(a)
    old = np.array([2, 3, 102, 103])
    new = np.array([20, 30, 2, 3])
    b = segment.arrays.replace_values(a, old, new, inplace=True)
    print(a)
    print(b)
    print(segment.arrays.relabel(b, inplace=True))

    print()
    a = np.array([1e6, 1e7], dtype=np.uint64)
    print(a)
    old = np.array([1e6], dtype=np.uint64)
    new = np.array([1], dtype=np.uint64)
    b = segment.arrays.replace_values(a, old, new, inplace=True)
    print(a)
    print(b)
    print(segment.arrays.relabel(b, inplace=True))

    print()
    a = np.array([0, 1e6, 1e7], dtype=np.uint64)
    print(a)
    old = np.array([1e6], dtype=np.uint64)
    new = np.array([1], dtype=np.uint64)
    b = segment.arrays.replace_values(a, old, new, inplace=True)
    print(a)
    print(b)
    print(segment.arrays.relabel(b, inplace=True))
