from numpy import load

data = load('datasets/VIL-2020-01-01-01_00Z.npz')
lst = data
for item in lst:
    print(item)
