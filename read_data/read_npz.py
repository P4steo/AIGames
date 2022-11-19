import numpy

data = numpy.load('../npz/plik1.npz')
lst = data.files
for item in lst:
    print(item)
    print(data[item])
