from numpy import load

data = load('out.npz')
lst = data.files
for item in lst:
    print(item)
    print(data[item])